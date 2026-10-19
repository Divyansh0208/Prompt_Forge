import json
import os
import re

import requests
from dotenv import load_dotenv
from flask import Flask, jsonify, request, send_from_directory

load_dotenv()

NVIDIA_API_KEY = os.environ["NVIDIA_API_KEY"]  # fail fast if missing
MODEL = os.getenv("NVIDIA_MODEL", "deepseek-ai/deepseek-v4.1-flash")

SYSTEM_PROMPT = """You are a master prompt engineer — a "Prompt Warrior". Your job is to transform weak, vague prompts into powerful, elite prompts.

You MUST respond with ONLY valid JSON — no markdown, no backticks, no preamble. Format:
{
  "forged_prompt": "the upgraded prompt text here",
  "techniques_used": ["context","specificity","constraints","format","persona","examples","cot","negatives"],
  "power_level": 7,
  "analysis": "2-3 sentence explanation of the key improvements made"
}

Technique definitions (only list ones actually used):
- context: added background info or purpose
- specificity: made the request more precise and detailed  
- constraints: added limits (length, tone, audience, scope)
- format: specified output format (list, table, markdown, etc.)
- persona: added role or persona for the AI
- examples: added examples or few-shot patterns
- cot: added chain-of-thought or step-by-step reasoning instruction
- negatives: added what NOT to do

power_level: integer 1-10 based on how much you improved the prompt.
The forged_prompt should be substantive and impressive — 3-8x longer than the original."""

app = Flask(__name__, static_folder=None)


@app.get("/")
def index():
    return send_from_directory("static", "prompt_warrior.html")


@app.post("/api/forge")
def forge():
    weak = str((request.get_json(silent=True) or {}).get("weak", "")).strip()[:2000]
    if not weak:
        return jsonify(error="Empty prompt"), 400
    try:
        r = requests.post(
            "https://integrate.api.nvidia.com/v1/chat/completions",
            headers={"Authorization": f"Bearer {NVIDIA_API_KEY}"},
            json={
                "model": MODEL,
                "max_tokens": 2000,
                "messages": [
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": f"Weak prompt to forge:\n<<<\n{weak}\n>>>"},
                ],
            },
            timeout=60,
        )
    except requests.Timeout:
        return jsonify(error="NVIDIA API timed out"), 504
    except requests.RequestException as e:
        return jsonify(error=str(e)), 502
    if not r.ok:
        return jsonify(error=f"NVIDIA {r.status_code}: {r.text[:300]}"), 502
    text = r.json()["choices"][0]["message"].get("content") or ""
    text = re.sub(r"<think>.*?</think>", "", text, flags=re.S)
    m = re.search(r"\{.*\}", text, re.S)
    try:
        return jsonify(json.loads(m.group(0)))
    except Exception:
        return jsonify(error="Model returned unparseable output"), 502


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
