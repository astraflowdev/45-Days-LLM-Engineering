"""
Your first Gemini API call.

Setup:
    pip install google-generativeai python-dotenv
    # put GEMINI_API_KEY=... in a .env file (get a free key at aistudio.google.com/apikey)
Run:
    python first_call.py
"""

import os

from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise SystemExit("Set GEMINI_API_KEY in a .env file first (see the README).")

genai.configure(api_key=api_key)

# gemini-2.0-flash: fast and free. (Model names change -- see the README.)
model = genai.GenerativeModel("gemini-2.0-flash")

response = model.generate_content("Explain what an API is in one simple sentence.")

print("Model's answer:")
print(response.text)

# The response also carries token usage -- handy for cost/limits later.
usage = response.usage_metadata
print()
print("Prompt tokens    :", usage.prompt_token_count)
print("Response tokens  :", usage.candidates_token_count)
print("Total tokens     :", usage.total_token_count)
