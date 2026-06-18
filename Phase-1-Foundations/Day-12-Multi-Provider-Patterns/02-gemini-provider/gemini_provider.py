"""
A Gemini provider function -- prompt in, string out.

Setup: pip install google-generativeai python-dotenv  (+ GEMINI_API_KEY in .env)
Run:   python gemini_provider.py
"""

import os

from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()


def ask_gemini(prompt: str) -> str:
    """Send a prompt to Gemini, return the answer text. Uniform signature."""
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])
    model = genai.GenerativeModel("gemini-2.0-flash")
    return model.generate_content(prompt).text.strip()


if __name__ == "__main__":
    print(ask_gemini("In one sentence, what is Groq known for?"))
