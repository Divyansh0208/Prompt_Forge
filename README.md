# ⚔ Prompt Forge

> **Forge Elite Prompts — Mini Challenge · I am a Prompt Warrior**

Prompt Forge is a single-page web app that transforms weak, vague prompts into powerful, production-ready prompts using **NVIDIA Llama 3.1 70B**. Paste in a rough idea, hit **Forge It**, and get back a structurally complete prompt with a power score, technique breakdown, and a Warrior Analysis explaining every upgrade made.

Built for **Google Prompt Wars 2026**.

---

## ✨ Features

- **Prompt Forging** — Rewrites any weak prompt into a detailed, elite-grade version (3–8× longer) using Llama 3.1 70B Instruct via the NVIDIA API
- **8 Technique Tags** — Detects and highlights which prompt engineering techniques were applied:
  - `Context` · `Specificity` · `Constraints` · `Output Format` · `Persona` · `Examples` · `Chain-of-Thought` · `Negatives`
- **Power Level Meter** — Scores the upgrade from 1–10, visualised as a 10-bar indicator
- **Warrior Rank System** — Earn a rank based on your power level: `RECRUIT` → `BRONZE` → `SILVER` → `GOLD` → `LEGENDARY`
- **Warrior Analysis Panel** — A 2–3 sentence explanation of the key improvements made to your prompt
- **Typewriter Output Animation** — Forged prompt streams in character-by-character for dramatic effect
- **Copy to Clipboard** — One-click copy of the forged prompt
- **Quick-Fill Examples** — Pre-loaded starter prompts: blog post, explain ML, resume help, marketing ideas
- **Keyboard Shortcut** — `Ctrl + Enter` / `Cmd + Enter` to forge
- **Responsive Design** — Fully usable on mobile and tablet screens

---

## 🗂 Project Structure

```
prompt_forge/
├── prompt_warrior.html   # Frontend — single-file UI (HTML + CSS + JS)
├── server.py             # Backend — Flask proxy to the NVIDIA API
├── .env                  # Your API key (never committed)
├── .env.example          # Template for environment setup
├── .gitignore            # Standard Python/IDE ignore rules
└── README.md             # This file
```

---

## 🛠 Tech Stack

| Layer     | Technology                                      |
|-----------|-------------------------------------------------|
| Frontend  | Vanilla HTML / CSS / JavaScript (single file)   |
| Backend   | Python · Flask · python-dotenv · requests       |
| AI Model  | NVIDIA Llama 3.1 70B Instruct (`meta/llama-3.1-70b-instruct`) |
| API       | [NVIDIA NIM API](https://build.nvidia.com/)     |
| Fonts     | Bebas Neue · DM Sans · DM Mono (Google Fonts)   |

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/prompt_forge.git
cd prompt_forge
```

### 2. Create and activate a virtual environment (recommended)

```bash
python -m venv venv
# macOS / Linux
source venv/bin/activate
# Windows
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install flask python-dotenv requests
```

### 4. Set up environment variables

```bash
cp .env.example .env
```

Open `.env` and add your NVIDIA API key:

```env
NVIDIA_API_KEY=your-nvidia-api-key-here
```

> Get your free API key at [build.nvidia.com](https://build.nvidia.com/).

### 5. Run the server

```bash
python server.py
```

### 6. Open the app

Visit [http://localhost:8000](http://localhost:8000) in your browser.

---

## 🔑 Environment Variables

| Variable         | Required | Description                                      |
|------------------|----------|--------------------------------------------------|
| `NVIDIA_API_KEY` | ✅ Yes   | API key from [build.nvidia.com](https://build.nvidia.com/) |

The API key is loaded server-side via `python-dotenv` and is never exposed to the browser.

---

## 🧠 How It Works

1. You enter a weak or rough prompt in the left panel.
2. On clicking **Forge It**, the frontend sends a `POST /api/forge` request to the Flask server.
3. The Flask server forwards the request to the NVIDIA NIM API with a detailed system prompt instructing Llama 3.1 70B to act as a master prompt engineer.
4. The model returns a structured JSON response containing:
   - `forged_prompt` — the upgraded prompt text
   - `techniques_used` — list of techniques applied
   - `power_level` — integer score from 1 to 10
   - `analysis` — explanation of improvements
5. The frontend parses the response and renders the forged prompt with a typewriter animation, lights up the relevant technique tags, fills the power meter, assigns a Warrior Rank, and shows the Warrior Analysis.

---

## 📡 API Reference

### `POST /api/forge`

Proxies a chat completion request to the NVIDIA API.

**Request Body** (forwarded directly to NVIDIA):

```json
{
  "model": "meta/llama-3.1-70b-instruct",
  "max_tokens": 1000,
  "messages": [
    { "role": "system", "content": "..." },
    { "role": "user",   "content": "Weak prompt to forge: \"...\"" }
  ]
}
```

**Response**: Standard NVIDIA/OpenAI-compatible chat completion object.

---

## 🎖 Warrior Rank Scale

| Power Level | Rank       |
|-------------|------------|
| 0           | —          |
| 1 – 2       | RECRUIT    |
| 3 – 4       | BRONZE     |
| 5 – 6       | SILVER     |
| 7 – 8       | GOLD       |
| 9 – 10      | LEGENDARY  |

---

## 📜 License

This project was created as part of **Google Prompt Wars 2026**. Feel free to fork and build upon it.

---

<p align="center">Powered by <strong>NVIDIA Llama 3.1 70B</strong></p>
