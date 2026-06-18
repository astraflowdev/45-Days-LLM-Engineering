"""
Solution -- Exercise 2: word-problem solver with chain-of-thought.

Run: python word_problem_solution.py
"""

import os

from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-2.0-flash")

problem = (
    "A train travels 60 km in the first hour and 90 km in the next hour. "
    "What is its average speed over the two hours?"
)

response = model.generate_content(
    problem + " Let's think step by step, then end with a line 'Final answer: <value>'."
)
text = response.text.strip()

print("--- Full reasoning ---")
print(text)

# Pull out just the final-answer line for programmatic use.
final = next((line for line in text.splitlines() if line.lower().startswith("final answer")), None)
print()
print("Extracted:", final)   # average speed = 150 km / 2 h = 75 km/h
