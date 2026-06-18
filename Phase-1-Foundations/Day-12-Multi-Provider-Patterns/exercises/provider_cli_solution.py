"""
Solution -- Exercise 1: provider-switching CLI.

Run: python provider_cli_solution.py
     LLM_PROVIDER=groq python provider_cli_solution.py
"""

import os

from dotenv import load_dotenv

load_dotenv()


def ask_gemini(prompt: str) -> str:
    import google.generativeai as genai
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])
    return genai.GenerativeModel("gemini-2.0-flash").generate_content(prompt).text.strip()


def ask_groq(prompt: str) -> str:
    from groq import Groq
    client = Groq(api_key=os.environ["GROQ_API_KEY"])
    chat = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
    )
    return chat.choices[0].message.content.strip()


PROVIDERS = {"gemini": ask_gemini, "groq": ask_groq}

provider = os.environ.get("LLM_PROVIDER", "gemini")
if provider not in PROVIDERS:
    raise SystemExit(f"Unknown LLM_PROVIDER={provider!r}. Choose from {list(PROVIDERS)}.")

answer = PROVIDERS[provider]("Give a one-line tip for learning to code.")
print(f"[{provider}] {answer}")
