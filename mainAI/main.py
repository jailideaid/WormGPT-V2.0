import os
import sys
import time
import itertools
import threading
from ai_client import ask_ai, validate_key, save_key, load_key

# =========================
# COLORS
# =========================
ASH = "\033[1;90m"
RED = "\033[1;91m"
GREEN = "\033[1;92m"
YELLOW = "\033[1;93m"
CYAN = "\033[1;96m"
WHITE = "\033[1;97m"
RESET = "\033[0m"


# =========================
# COLORS MARKDOWN
# =========================
BOLD = "\033[1m"
RESET = "\033[0m"


# =========================
# CLEAR SCREEN (CROSS PLATFORM)
# =========================
def clear():
    os.system("cls" if os.name == "nt" else "clear")


# =========================
# SPINNER
# =========================
def spinner(stop_event, text="Checking"):
    for char in itertools.cycle(["⠋","⠙","⠹","⠸","⠼","⠴","⠦","⠧","⠇","⠏"]):
        if stop_event.is_set():
            break
        sys.stdout.write(f"\r{CYAN}{text} {char}{RESET}")
        sys.stdout.flush()
        time.sleep(0.08)
    sys.stdout.write("\r" + " " * 40 + "\r")


# =========================
# BANNER
# =========================
def print_banner():
    banner = r"""
██╗    ██╗ ██████╗ ██████╗ ███╗   ███╗  ██████╗  ██████╗ ████████╗
██║    ██║██╔═══██╗██╔══██╗████╗ ████║ ██╔════╝  ██╔══██╗╚══██╔══╝
██║ █╗ ██║██║   ██║██████╔╝██╔████╔██║ ██║  ███╗ ██████╔╝   ██║   
██║███╗██║██║   ██║██╔══██╗██║╚██╔╝██║ ██║   ██║ ██╔═══╝    ██║   
╚███╔███╔╝╚██████╔╝██║  ██║██║ ╚═╝ ██║ ╚██████╔╝ ██║        ██║   
 ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝  ╚═════╝  ╚═╝        ╚═╝   

                    ██╗   ██╗██████╗     ██████╗ 
                    ██║   ██║╚════██╗   ██╔═████╗
                    ██║   ██║ █████╔╝   ██║██╔██║
                    ╚██╗ ██╔╝██╔═══╝    ████╔╝██║
                     ╚████╔╝ ███████╗██╗╚██████╔╝
                      ╚═══╝  ╚══════╝╚═╝ ╚═════╝ 
    """
    print(RED + banner + RESET)
    print(ASH + "Type 'exit' or 'quit' to close.\n" + RESET)


# =========================
# API KEY HANDLER
# =========================
def get_api_key():
    while True:
        key = load_key()

        if key:
            stop = threading.Event()
            t = threading.Thread(target=spinner, args=(stop, "Validating"))
            t.start()

            valid = validate_key(key)

            stop.set()
            t.join()

            if valid:
                clear()
                print_banner()
                print(GREEN + "✔ API Key Verified Successfully!" + RESET)
                time.sleep(1.5)
                clear()
                print_banner()
                return key

        key = input(CYAN + "Enter your OpenRouter API key: " + RESET).strip()

        stop = threading.Event()
        t = threading.Thread(target=spinner, args=(stop, "Checking"))
        t.start()

        valid = validate_key(key)

        stop.set()
        t.join()

        if valid:
            save_key(key)
            clear()
            print_banner()
            print(GREEN + "✔ API Key Saved & Verified!" + RESET)
            time.sleep(1.5)
            clear()
            print_banner()
            return key
        else:
            clear()
            print_banner()
            print(RED + "✖ Invalid API Key. Please try again.\n" + RESET)


# =========================
# MAIN LOOP
# =========================
def select_language():
    while True:
        clear()
        print_banner()

        print("\nSelect Language:")
        print("1. Bahasa Indonesia")
        print("2. English")

        choice = input("Choice > ").strip()

        if choice == "1":
            return "id"
        elif choice == "2":
            return "en"
        else:
            print(RED + "\nInvalid choice!" + RESET)
            time.sleep(1.2)
            
def print_chat_header(language):
    if language == "id":
        print(CYAN + "Tanyakan apa saja kepada AI\n" + RESET)
    else:
        print(CYAN + "Ask anything to the AI\n" + RESET)

import re

def format_bold(text):
    return re.sub(
        r"\*\*(.*?)\*\*",
        r"\033[1m\1\033[0m",
        text
    )

def run_cli():
    clear()
    print_banner()

    api_key = get_api_key()
    language = select_language()

    clear()
    print_banner()

    if language == "id":
        print(GREEN + "✔ Bahasa diatur ke: Indonesia\n" + RESET)
    else:
        print(GREEN + "✔ Language set to: English\n" + RESET)

    time.sleep(1.2)
    clear()
    print_banner()
    print_chat_header(language)

    chat_history = []

    while True:
        try:
            user_input = input(WHITE + "You > " + RESET).strip()

            if not user_input:
                continue

            if user_input.lower() in ["exit", "quit"]:
                print(GREEN + "\nGoodbye!" + RESET)
                break

            stop = threading.Event()
            t = threading.Thread(
                target=spinner,
                args=(stop, "Thinking...")
            )
            t.start()

            reply = ask_ai(user_input, api_key, language, chat_history)

            stop.set()
            t.join()

            formatted_reply = format_bold(reply)
            print(GREEN + "AI Answer > " + RESET + formatted_reply)

            # SAFE MEMORY CHAT HISTORY
            chat_history.append({"role": "user", "content": user_input})
            chat_history.append({"role": "assistant", "content": reply})

            # limit memory so it doesn't get overloaded
            if len(chat_history) > 20:
                chat_history = chat_history[-20:]

        except KeyboardInterrupt:
            print(RED + "\n\nSession terminated." + RESET)
            sys.exit()

        except Exception as e:
            print(RED + f"\n[Error]: {e}" + RESET)

if __name__ == "__main__":
    run_cli()