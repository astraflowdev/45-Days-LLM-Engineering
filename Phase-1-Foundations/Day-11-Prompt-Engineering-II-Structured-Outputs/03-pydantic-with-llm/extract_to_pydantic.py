"""
Pydantic + LLM -- turn model JSON into a validated, typed object.

Setup: pip install google-generativeai pydantic python-dotenv  (+ GEMINI_API_KEY in .env)
Run:   python extract_to_pydantic.py
"""

import json
import os

from dotenv import load_dotenv
import google.generativeai as genai
from pydantic import BaseModel

load_dotenv()
genai.configure(api_key=os.environ["GEMINI_API_KEY"])


# The shape we want -- defined once, used as both contract and validator.
class Person(BaseModel):
    name: str
    age: int
    city: str


model = genai.GenerativeModel(
    "gemini-2.0-flash",
    generation_config={"response_mime_type": "application/json"},
)

text = "Priya Verma, 23, lives in Pune and works as a data analyst."
prompt = (
    "Extract the person. Return JSON with keys: name (string), age (integer), city (string).\n"
    f"Text: {text}"
)

response = model.generate_content(prompt)

# JSON string -> dict -> validated Person object.
data = json.loads(response.text)
person = Person(**data)

print("Validated object:", person)
print("Typed access -> next year she'll be", person.age + 1)   # real int maths
