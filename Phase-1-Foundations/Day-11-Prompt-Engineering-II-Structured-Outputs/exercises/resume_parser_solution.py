"""
Solution -- Exercise 1: resume parser.

Run: python resume_parser_solution.py
"""

import os

from dotenv import load_dotenv
import google.generativeai as genai
from pydantic import BaseModel

load_dotenv()
genai.configure(api_key=os.environ["GEMINI_API_KEY"])


class Candidate(BaseModel):
    name: str
    years_experience: int
    skills: list[str]


resume = (
    "Rohan Gupta is a backend developer with 4 years of experience. "
    "He works with Python, FastAPI, PostgreSQL, and Docker."
)

model = genai.GenerativeModel(
    "gemini-2.0-flash",
    generation_config={"response_mime_type": "application/json"},
)

prompt = (
    "Extract the candidate as JSON with keys: name (string), "
    "years_experience (integer), skills (array of strings).\n"
    f"Resume: {resume}"
)

response = model.generate_content(prompt)
candidate = Candidate.model_validate_json(response.text)

print("Name       :", candidate.name)
print("Experience :", candidate.years_experience, "years")
print("Skills     :", ", ".join(candidate.skills))
