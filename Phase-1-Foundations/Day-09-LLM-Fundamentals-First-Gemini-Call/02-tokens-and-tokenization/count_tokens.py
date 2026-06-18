"""
Counting tokens with Gemini.

Tokens drive cost, context limits, and speed -- so it helps to see how text
maps to token counts.

Setup: pip install google-generativeai python-dotenv  (+ GEMINI_API_KEY in .env)
Run:   python count_tokens.py
"""

import os

from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise SystemExit("Set GEMINI_API_KEY in a .env file first (see the README).")

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.0-flash")

samples = [
    "Hello",
    "I love learning about AI.",
    "Antidisestablishmentarianism",          # one long word -> several tokens
    "namaste, kaise ho aap?",                # Hindi-in-Latin often costs more
]

print("text -> token count")
for text in samples:
    count = model.count_tokens(text).total_tokens
    print(f"  {count:>3}  <- {text!r}")

print()
print("Notice: token count is NOT the same as word count or character count.")
print("Long/rare words and non-English text use more tokens.")
