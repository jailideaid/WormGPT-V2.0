# 🐛 WormGPT CLI V2.0

A lightweight AI Command Line Interface powered by OpenRouter API.

This project provides a clean terminal-based AI interaction system with:

* Language selection (English / Indonesian)
* Session memory
* Token limiting
* API key validation
* Configurable model
* Clean terminal UI

## Preview WormGPT CLI V2.0
<p align="center">
  <img src="https://github.com/user-attachments/assets/4fb2dd51-3716-40bd-b090-d48abc5b165b" width="773"/>
  <img src="https://github.com/user-attachments/assets/8e4105f4-ed76-4190-a762-24b9b9a43565" width="773"/>
  <img src="https://github.com/user-attachments/assets/699824dd-6a30-4aa9-b5be-d9e7d5c61414" width="773"/>
</p>

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

### Install Git (if not installed)

Download from:
https://git-scm.com/

### Clone Repository

```bash
git clone https://github.com/jailideaid/WormGPT-V2.0
cd WormGPT-V2.0
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run

```bash
python main.py
```

---

### 🐧 Linux (Ubuntu/Debian/Kali)

### Install Dependencies

```bash
sudo apt update
sudo apt install git python3 python3-pip -y
```

### Clone

```bash
git clone https://github.com/jailideaid/WormGPT-V2.0
cd WormGPT-V2.0
```

### Install Python Dependency

```bash
pip3 install -r requirements.txt
```

### Run

```bash
python main.py
```

---

### 🍎 macOS

### Install Homebrew (if needed)

Download from:
https://brew.sh/

### Install Git & Python

```bash
brew install git python
```

### Clone

```bash
git clone https://github.com/jailideaid/WormGPT-V2.0
cd WormGPT-V2.0
```

### Install Dependency

```bash
pip3 install -r requirements.txt
```

### Run

```bash
python3 main.py
```

---

### 📱 Android (Termux)

### Install Termux

From F-Droid (recommended).

### Setup Environment

```bash
pkg update
pkg install git python -y
pip install -r requirements.txt
```

### Clone & Run

```bash
git clone https://github.com/jailideaid/WormGPT-V2.0
cd WormGPT-V2.0
python main.py
```

---

## 🔑 API Key Setup

When first running the program, it will ask for your OpenRouter API key.

You can create an account on the https://openrouter.ai page and create a key.

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
│   ├── .apikey (automatically creates a file when the key is entered!)
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

Use your API key securely, do not share it publicly.

## Another notes!

* don't misuse AI for personal gain to satisfy your crimes. 
* You can use wormgpt wisely without having to do or violate anything. 
* I am not responsible for that. Thank you for your support by favoriting this repository and following it.

If you use https://openrouter.ai with a free key, if you are hit by a token limit, I suggest changing to another free model or upgrading your key by subscribing.

---

Built for experimentation and CLI-based AI interaction.
Use responsibly.
