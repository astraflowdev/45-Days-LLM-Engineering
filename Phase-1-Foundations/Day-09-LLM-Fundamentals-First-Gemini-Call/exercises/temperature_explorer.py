"""
Exercise 2 -- temperature explorer.

Setup: pip install google-generativeai python-dotenv  (+ GEMINI_API_KEY in .env)
Run:   python temperature_explorer.py
"""

import os

from dotenv import load_dotenv
import google.generativeai as genai
from google.generativeai.types import GenerationConfig

load_dotenv()
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-2.0-flash")

prompt = "Write a one-line tagline for a chai startup."

# TODO 1: for each temperature in (0.0, 0.7, 1.4):
#           - call model.generate_content(prompt, generation_config=GenerationConfig(temperature=t))
#           - print the temperature and the answer
