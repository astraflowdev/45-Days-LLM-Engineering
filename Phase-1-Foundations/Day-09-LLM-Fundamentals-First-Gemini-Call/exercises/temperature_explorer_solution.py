"""
Solution -- Exercise 2: temperature explorer.

Run: python temperature_explorer_solution.py
"""

import os

from dotenv import load_dotenv
import google.generativeai as genai
from google.generativeai.types import GenerationConfig

load_dotenv()
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-2.0-flash")

prompt = "Write a one-line tagline for a chai startup."

for temperature in (0.0, 0.7, 1.4):
    response = model.generate_content(
        prompt,
        generation_config=GenerationConfig(temperature=temperature),
    )
    print(f"temperature {temperature}:")
    print("  ", response.text.strip())
    print()

print("Higher temperature -> more variety and surprise in the taglines.")
