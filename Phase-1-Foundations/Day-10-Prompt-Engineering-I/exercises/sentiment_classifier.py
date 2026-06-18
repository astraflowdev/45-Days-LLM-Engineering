"""
Exercise 1 -- few-shot sentiment classifier.

Setup: pip install google-generativeai python-dotenv  (+ GEMINI_API_KEY in .env)
Run:   python sentiment_classifier.py
"""

import os

from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-2.0-flash")

reviews = [
    "Absolutely loved the experience!",
    "Terrible, I want a refund.",
    "It was fine, nothing special.",
]

# TODO 1: write a FEW-SHOT prompt with 3 labelled examples (positive/negative/neutral)
#         and one blank slot for {review}
# TODO 2: for each review, format the prompt, call the model, and print the label
