"""
JSON mode -- force a clean, parseable JSON response from Gemini.

Setup: pip install google-generativeai python-dotenv  (+ GEMINI_API_KEY in .env)
Run:   python json_mode.py
"""

import json
import os

from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# response_mime_type=application/json -> the reply is clean JSON (no ``` fences).
model = genai.GenerativeModel(
    "gemini-2.0-flash",
    generation_config={"response_mime_type": "application/json"},
)

text = "Aarav Sharma is 21 years old and studies computer science in Lucknow."
prompt = (
    "Extract the person's details from the text. "
    "Return JSON with keys: name (string), age (integer), field (string), city (string).\n"
    f"Text: {text}"
)

response = model.generate_content(prompt)

print("Raw response text (already clean JSON):")
print(response.text)

data = json.loads(response.text)     # safe to parse -- it's guaranteed JSON
print()
print("Parsed dict:", data)
print("data['age'] =", data["age"], f"({type(data['age']).__name__})")
