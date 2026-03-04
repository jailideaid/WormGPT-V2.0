import requests
import json
from pathlib import Path

# =========================
# BASE PATH
# =========================
BASE_DIR = Path(__file__).resolve().parent
CONFIG_PATH = BASE_DIR / "config.json"
KEY_PATH = BASE_DIR / ".apikey"

CONFIG = json.load(open(CONFIG_PATH, "r", encoding="utf-8"))


# =========================
# SYSTEM PROMPT LOADER
# =========================
def load_system_prompt(language):
    prompt_path = BASE_DIR / "system-prompts" / f"{language}.txt"
    return prompt_path.read_text(encoding="utf-8").strip()

# =========================
# API KEY HANDLER
# =========================
def load_key():
    if KEY_PATH.exists():
        return KEY_PATH.read_text().strip()
    return None


def save_key(key):
    KEY_PATH.write_text(key)


def validate_key(key):
    headers = {"Authorization": f"Bearer {key}"}
    res = requests.get(
        "https://openrouter.ai/api/v1/auth/key",
        headers=headers,
        timeout=15
    )
    return res.status_code == 200


# =========================
# AI REQUEST
# =========================
def ask_ai(message: str, api_key: str, language: str, chat_history: list):

    system_prompt = load_system_prompt(language)

    if language == "en":
        enforced_message = f"Reply strictly and only in English.\n\nUser message:\n{message}"
    else:
        enforced_message = f"Jawab secara tegas dan hanya dalam Bahasa Indonesia.\n\nPesan pengguna:\n{message}"

    messages = [
        {"role": "system", "content": system_prompt}
    ]

    # add old history
    messages.extend(chat_history)

    # add latest message
    messages.append({"role": "user", "content": enforced_message})

    payload = {
        "model": CONFIG["model"],
        "messages": messages,
        "temperature": 0.2,
        "max_tokens": 500
    }

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": CONFIG["site_url"],
        "X-Title": CONFIG["site_name"]
    }

    res = requests.post(
        f"{CONFIG['base_url']}/chat/completions",
        headers=headers,
        json=payload,
        timeout=60
    )

    if res.status_code != 200:
        return f"API Error {res.status_code}: {res.text}"

    data = res.json()
    return data["choices"][0]["message"]["content"]
