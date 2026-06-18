"""
Exercise 2 -- word-problem solver with chain-of-thought.

Setup: pip install google-generativeai python-dotenv  (+ GEMINI_API_KEY in .env)
Run:   python word_problem.py
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

# TODO 1: ask the model to solve the problem step by step, ending with 'Final answer: <x>'
# TODO 2: print the full reasoning
# TODO 3: extract and print only the line starting with 'Final answer'
