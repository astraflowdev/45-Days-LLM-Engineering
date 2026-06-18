"""
Few-shot prompting -- show examples, the model copies the pattern.

Setup: pip install google-generativeai python-dotenv  (+ GEMINI_API_KEY in .env)
Run:   python few_shot.py
"""

import os

from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-2.0-flash")

new_review = "The food was cold and the delivery was late."

# Three examples establish the task, the label set, and the exact format.
prompt = f"""Classify the sentiment. Reply with exactly one word: positive, negative, or neutral.

Review: "Loved it, will come again!"    Sentiment: positive
Review: "Worst service ever."           Sentiment: negative
Review: "It was okay, nothing special." Sentiment: neutral
Review: "{new_review}"   Sentiment:"""

response = model.generate_content(prompt)
print("Review    :", new_review)
print("Sentiment :", response.text.strip())
print()
print("The 3 examples locked the format -- we get a clean one-word label.")
