<div align="center">

  <img src="https://img.shields.io/badge/Prompt_Forge-⚔️_Elite_Prompt_Engine-7B3FED?style=for-the-badge&logo=nvidia&logoColor=white" alt="Prompt Forge"/>

  <h1>⚔️ Prompt Forge</h1>
  <p><strong>Transform weak prompts into elite, production-ready prompts using NVIDIA Llama 3.1 70B</strong></p>

  <p>
    <a href="https://prompt-forge-o970.onrender.com">
      <img src="https://img.shields.io/badge/Live_Demo-Visit_Now-00C853?style=for-the-badge" alt="Live Demo"/>
    </a>
    <img src="https://img.shields.io/badge/Built_for-Google_Prompt_Wars_2026-FF6D00?style=for-the-badge" alt="Prompt Wars 2026"/>
    <img src="https://img.shields.io/badge/Model-Llama_3.1_70B-76B900?style=for-the-badge&logo=nvidia" alt="Llama 3.1 70B"/>
    <img src="https://img.shields.io/badge/License-MIT-blue?style=for-the-badge" alt="MIT License"/>
    <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python" alt="Python"/>
    <img src="https://img.shields.io/badge/Flask-Backend-black?style=for-the-badge&logo=flask" alt="Flask"/>
  </p>

  <p><em>Paste a rough idea → Hit "Forge It" → Get an elite prompt with power scoring, technique breakdown, and Warrior Analysis ✨</em></p>

</div>

---

## 🚀 Live Demo

**[→ Try Prompt Forge Live](https://prompt-forge-o970.onrender.com)**

Paste a weak prompt → Hit Forge It → Watch the magic ✨

---

## 📸 Screenshots

### ⚔️ Forge Interface — Prompt Engineering Tool with NVIDIA Llama 3.1

![Prompt Forge Interface](screenshots/prompt-forge.jpg)

---

## 🛠️ Built With — Python Flask, NVIDIA NIM API, Vanilla JS

| Layer | Technology |
|-------|-----------|
| Frontend | Vanilla HTML / CSS / JavaScript (single file) |
| Backend | Python · Flask · python-dotenv · requests |
| AI Model | NVIDIA Llama 3.1 70B Instruct (`meta/llama-3.1-70b-instruct`) |
| API | NVIDIA NIM API |
| Fonts | Bebas Neue · DM Sans · DM Mono (Google Fonts) |

---

## ✨ Features — Prompt Forging, Technique Detection, Power Scoring

**Prompt Forging Engine** — Rewrites any weak prompt into a detailed, elite-grade version (3–8× longer) using Llama 3.1 70B Instruct via the NVIDIA NIM API.

**8 Prompt Engineering Technique Tags** — Detects and highlights which techniques were applied:
`Context` · `Specificity` · `Constraints` · `Output Format` · `Persona` · `Examples` · `Chain-of-Thought` · `Negatives`

**Power Level Meter (1–10)** — Scores the upgrade from 1–10, visualised as a 10-bar indicator.

**Warrior Rank System** — Earn a rank based on your power level: `RECRUIT` → `BRONZE` → `SILVER` → `GOLD` → `LEGENDARY`

**Warrior Analysis Panel** — A 2–3 sentence explanation of every key improvement made to your prompt.

**Typewriter Output Animation** — Forged prompt streams in character-by-character for dramatic effect.

**One-Click Copy** — Instantly copy the forged prompt to clipboard.

**Quick-Fill Examples** — Pre-loaded starters: blog post, explain ML, resume help, marketing ideas.

**Keyboard Shortcut** — `Ctrl + Enter` / `Cmd + Enter` to forge instantly.

**Responsive Design** — Fully usable on mobile and tablet screens.

---

## 🗂 Project Structure

```
prompt_forge/
├── prompt_warrior.html   # Frontend — single-file UI (HTML + CSS + JS)
├── server.py             # Backend — Flask proxy to the NVIDIA NIM API
├── .env                  # Your API key (never committed)
├── .env.example          # Template for environment setup
├── .gitignore            # Standard Python/IDE ignore rules
└── README.md             # This file
```

---

## 🚀 Getting Started — Quick Setup Guide for Prompt Forge

### 1. Clone the repository

```bash
git clone https://github.com/Divyansh0208/Prompt_Forge.git
cd Prompt_Forge
```

### 2. Create and activate a virtual environment

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

```
NVIDIA_API_KEY=your-nvidia-api-key-here
```

Get your free API key at [build.nvidia.com](https://build.nvidia.com).

### 5. Run the server

```bash
python server.py
```

### 6. Open the app

Visit `http://localhost:8000` in your browser.

---

## 🔑 Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `NVIDIA_API_KEY` | ✅ Yes | API key from [build.nvidia.com](https://build.nvidia.com) |

The API key is loaded server-side via `python-dotenv` and is **never exposed to the browser**.

---

## 🧠 How It Works — Prompt Forging Pipeline Explained

1. Enter a weak or rough prompt in the left panel.
2. Click **Forge It** — frontend sends `POST /api/forge` to the Flask server.
3. Flask forwards the request to the **NVIDIA NIM API** with a detailed system prompt instructing Llama 3.1 70B to act as a master prompt engineer.
4. The model returns a structured JSON response:
   - `forged_prompt` — the upgraded prompt text
   - `techniques_used` — list of techniques applied
   - `power_level` — integer score from 1 to 10
   - `analysis` — explanation of improvements
5. Frontend renders the forged prompt with typewriter animation, lights up technique tags, fills the power meter, assigns a Warrior Rank, and shows the Warrior Analysis.

---

## 📡 API Reference — NVIDIA NIM Proxy Endpoint

### `POST /api/forge`

Proxies a chat completion request to the NVIDIA NIM API.

**Request Body:**

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

**Response:** Standard NVIDIA/OpenAI-compatible chat completion object.

---

## 🎖 Warrior Rank Scale — Prompt Power Level System

| Power Level | Warrior Rank |
|-------------|-------------|
| 0 | — |
| 1 – 2 | 🪖 RECRUIT |
| 3 – 4 | 🥉 BRONZE |
| 5 – 6 | 🥈 SILVER |
| 7 – 8 | 🥇 GOLD |
| 9 – 10 | 🏆 LEGENDARY |

---

## 🤝 Contributing

Contributions are welcome! Fork the repo, make your changes, and open a pull request. For major changes, open an issue first to discuss what you'd like to change.

---

## 📜 License — MIT License for Open Source

This project is licensed under the [MIT License](LICENSE).

Created for **Google Prompt Wars 2026**.

---

<div align="center">
  <strong>Powered by NVIDIA Llama 3.1 70B · Built with ⚔️ by <a href="https://github.com/Divyansh0208">Divyansh0208</a></strong>
</div>
