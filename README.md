# 🐛 WormGPT CLI V2.0

A lightweight AI Command Line Interface powered by OpenRouter API.

This project provides a clean terminal-based AI interaction system with:

* Language selection (English / Indonesian)
* Session memory
* Token limiting
* API key validation
* Configurable model
* Clean terminal UI

---

## 📦 Requirements

* Python 3.9+
* Git
* Internet connection
* OpenRouter API key

---

## 🚀 Installation (All Operating Systems)

This project uses Git for installation across Windows, Linux, macOS, and Android (Termux).

---

### 🖥 Windows (PowerShell or Windows Terminal)

#### 1. Install Git (if not installed)

Download from:
https://git-scm.com/

#### 2. Clone Repository

```bash
git clone https://github.com/USERNAME/wormgpt-cli.git
cd wormgpt-cli
```

#### 3. Install Dependencies

```bash
pip install requests
```

#### 4. Run

```bash
python mainAI/main.py
```

---

### 🐧 Linux (Ubuntu/Debian/Kali)

#### 1. Install Dependencies

```bash
sudo apt update
sudo apt install git python3 python3-pip -y
```

#### 2. Clone

```bash
git clone https://github.com/USERNAME/wormgpt-cli.git
cd wormgpt-cli
```

#### 3. Install Python Dependency

```bash
pip3 install requests
```

#### 4. Run

```bash
python3 mainAI/main.py
```

---

### 🍎 macOS

#### 1. Install Homebrew (if needed)

Download from:
https://brew.sh/

#### 2. Install Git & Python

```bash
brew install git python
```

#### 3. Clone

```bash
git clone https://github.com/USERNAME/wormgpt-cli.git
cd wormgpt-cli
```

#### 4. Install Dependency

```bash
pip3 install requests
```

#### 5. Run

```bash
python3 mainAI/main.py
```

---

### 📱 Android (Termux)

#### 1. Install Termux

From F-Droid (recommended).

#### 2. Setup Environment

```bash
pkg update
pkg install git python -y
pip install requests
```

#### 3. Clone & Run

```bash
git clone https://github.com/USERNAME/wormgpt-cli.git
cd wormgpt-cli
python mainAI/main.py
```

---

## 🔑 API Key Setup

When first running the program, it will ask for your OpenRouter API key.

The key is stored locally at:

```
mainAI/.apikey
```

You can manually edit it anytime.

⚠ Never upload `.apikey` to GitHub.

Add this to `.gitignore`:

```
mainAI/.apikey
```

---

## 🌍 Language System

After API key verification, you will select:

1. Bahasa Indonesia
2. English

The system enforces response language strictly using system prompts.

All interface text adapts to the selected language.

---

## ⚙ Configuration

Edit:

```
mainAI/config.json
```

Example:

```json
{
  "base_url": "https://openrouter.ai/api/v1",
  "model": "mistralai/mistral-7b-instruct",
  "site_url": "http://localhost",
  "site_name": "WormGPT CLI"
}
```

You can change the model anytime.

---

## 🧠 How It Works

### 1. System Prompt Loader

Each language has its own system prompt file:

```
mainAI/system-prompts/
    en.txt
    id.txt
```

When language is selected, the corresponding file is loaded and sent as the system message.

---

### 2. Message Flow

Each request sends:

* System prompt
* Chat history (limited)
* Current user input

To OpenRouter API using:

```
POST /chat/completions
```

---

### 3. Session Memory

* Chat history is stored in memory during runtime.
* Limited to prevent token overflow.
* Automatically trims old messages.
* Not persistent after program closes.

---

### 4. Token Control

The system uses:

* `max_tokens` for response limit
* History trimming to avoid context overflow

This prevents:

* API errors
* Context length exceeded
* Excess cost

---

### 5. API Key Validation

Before entering chat mode:

* The key is validated via OpenRouter auth endpoint.
* If invalid → user is prompted again.
* If valid → stored locally.

---

## 🛑 Common Errors

| Error                   | Meaning                         |
| ----------------------- | ------------------------------- |
| 401                     | Invalid API key                 |
| 429                     | Rate limit (usually free model) |
| Context length exceeded | Too many tokens                 |

If using free-tier models, temporary 429 errors may occur.

---

## 📂 Project Structure

```
wormgpt-cli/
│
├── mainAI/
│   ├── main.py
│   ├── ai_client.py
│   ├── config.json
│   ├── .apikey
│   └── system-prompts/
│       ├── en.txt
│       └── id.txt
│
└── README.md
```

---

## 🔮 Future Improvements

* Persistent memory (cross-session)
* Auto-summarization
* Cost tracking
* Multi-model switch
* Plugin architecture

---

## 📌 Notes

This project is intended for:

* Learning API integration
* Understanding CLI architecture
* Experimenting with language enforcement
* Building AI tools responsibly

Use your API key securely.
Do not share it publicly.

---

Built for experimentation and CLI-based AI interaction.
Use responsibly.
