"""
Zero-shot prompting -- ask with no examples.

Shows a vague prompt vs a specific one. Being specific is the cheapest way to
make zero-shot reliable.

Setup: pip install google-generativeai python-dotenv  (+ GEMINI_API_KEY in .env)
Run:   python zero_shot.py
"""

import os

from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-2.0-flash")

review = "The delivery was late but the food was delicious."

# Vague: the model may answer in any format / with extra words.
vague = model.generate_content(f"Is this review good? {review}")

# Specific: tell it the EXACT output you want.
specific = model.generate_content(
    f"Classify the review as exactly one word -- positive, negative, or mixed.\nReview: {review}"
)

print("Vague prompt    ->", vague.text.strip())
print("Specific prompt ->", specific.text.strip())
print()
print("Same task, but the specific prompt gives a clean, predictable answer.")
