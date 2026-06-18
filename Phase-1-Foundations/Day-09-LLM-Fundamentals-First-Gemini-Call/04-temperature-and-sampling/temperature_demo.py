"""
Temperature in action -- same prompt, low vs high temperature.

Low temperature -> consistent, predictable answers.
High temperature -> varied, creative answers.

Setup: pip install google-generativeai python-dotenv  (+ GEMINI_API_KEY in .env)
Run:   python temperature_demo.py
"""

import os

from dotenv import load_dotenv
import google.generativeai as genai
from google.generativeai.types import GenerationConfig

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise SystemExit("Set GEMINI_API_KEY in a .env file first (see the README).")

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.0-flash")

prompt = "Suggest a creative name for an AI tutoring app. Reply with just the name."

for temperature in (0.0, 1.2):
    print(f"--- temperature = {temperature} (run twice) ---")
    for _ in range(2):
        response = model.generate_content(
            prompt,
            generation_config=GenerationConfig(temperature=temperature),
        )
        print("  ", response.text.strip())
    print()

print("Low temperature tends to repeat the same answer; high temperature varies.")
