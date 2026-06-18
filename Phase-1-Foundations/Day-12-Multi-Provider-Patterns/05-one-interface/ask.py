"""
One interface over all providers, with a fallback chain.

Each provider function has the same shape: ask_x(prompt: str) -> str. Here we
register them in a dict and dispatch / fall back.

Setup: pip install google-generativeai groq ollama python-dotenv
       (.env: GEMINI_API_KEY, GROQ_API_KEY; Ollama installed + a model pulled)
Run:   python ask.py
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


def ask_ollama(prompt: str) -> str:
    import ollama
    return ollama.chat(
        model="llama3.2", messages=[{"role": "user", "content": prompt}]
    )["message"]["content"].strip()


# Add a provider = add one entry. The rest of the app only calls ask().
PROVIDERS = {"gemini": ask_gemini, "groq": ask_groq, "ollama": ask_ollama}


def ask(prompt: str, provider: str = "gemini") -> str:
    return PROVIDERS[provider](prompt)


def ask_with_fallback(prompt: str, order=("gemini", "groq", "ollama")) -> str:
    for name in order:
        try:
            return PROVIDERS[name](prompt)
        except Exception as err:                 # outage, rate limit, missing key...
            print(f"  {name} failed ({type(err).__name__}); trying next...")
    raise RuntimeError("All providers failed.")


if __name__ == "__main__":
    answer = ask_with_fallback("Say hello in one short sentence.")
    print("Answer:", answer)
