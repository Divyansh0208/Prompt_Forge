from flask import Flask, request, jsonify, send_from_directory
from dotenv import load_dotenv
import requests
import json
import os

load_dotenv()

app = Flask(__name__, static_folder=".")

NVIDIA_API_KEY = os.getenv("NVIDIA_API_KEY")

@app.route("/")
def index():
    return send_from_directory(".", "prompt_warrior (1).html")


@app.route("/api/forge", methods=["POST"])
def forge():
    """Proxy endpoint that forwards requests to the NVIDIA API."""
    try:
        payload = request.get_json()

        response = requests.post(
            "https://integrate.api.nvidia.com/v1/chat/completions",
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {NVIDIA_API_KEY}",
            },
            json=payload,
            timeout=60,
        )

        # Log the response for debugging
        print(f"[NVIDIA] Status: {response.status_code}")
        print(f"[NVIDIA] Response: {response.text[:500]}")

        # Return whatever NVIDIA sent back (including errors)
        try:
            data = response.json()
        except Exception:
            data = {"error": f"NVIDIA returned non-JSON: {response.text[:300]}"}

        return jsonify(data), response.status_code

    except requests.exceptions.Timeout:
        print("[ERROR] Request to NVIDIA timed out")
        return jsonify({"error": "Request to NVIDIA API timed out"}), 504

    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Request failed: {e}")
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(port=8000, debug=True)
