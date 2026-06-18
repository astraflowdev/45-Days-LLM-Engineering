"""
Solution -- Exercise 1: few-shot sentiment classifier.

Run: python sentiment_classifier_solution.py
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

# Few-shot template: 3 examples set the label set + format; {review} is the input.
TEMPLATE = """Classify the sentiment. Reply with exactly one word: positive, negative, or neutral.

Review: "Best purchase this year!"      Sentiment: positive
Review: "Broke after one day."          Sentiment: negative
Review: "Average, does the job."        Sentiment: neutral
Review: "{review}"   Sentiment:"""

for review in reviews:
    prompt = TEMPLATE.format(review=review)
    label = model.generate_content(prompt).text.strip()
    print(f"{label:9} <- {review}")
