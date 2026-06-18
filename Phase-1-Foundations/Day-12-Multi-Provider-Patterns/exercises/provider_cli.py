"""
Exercise 1 -- provider-switching CLI (pick the backend from an env var).

Setup: pip install google-generativeai groq python-dotenv
Run:   python provider_cli.py
       LLM_PROVIDER=groq python provider_cli.py
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


# TODO 1: build a PROVIDERS dict mapping "gemini"/"groq" to the functions above
# TODO 2: read LLM_PROVIDER from os.environ (default "gemini")
# TODO 3: call the chosen function with a prompt and print the answer + which provider ran
