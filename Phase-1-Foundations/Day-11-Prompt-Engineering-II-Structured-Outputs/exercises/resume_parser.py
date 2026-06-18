"""
Exercise 1 -- resume parser (structured extraction).

Setup: pip install google-generativeai pydantic python-dotenv  (+ GEMINI_API_KEY in .env)
Run:   python resume_parser.py
"""

import os

from dotenv import load_dotenv
import google.generativeai as genai
from pydantic import BaseModel

load_dotenv()
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

resume = (
    "Rohan Gupta is a backend developer with 4 years of experience. "
    "He works with Python, FastAPI, PostgreSQL, and Docker."
)

# TODO 1: define a Candidate model: name: str, years_experience: int, skills: list[str]
# TODO 2: make a model with response_mime_type=application/json
# TODO 3: prompt it to extract the fields as JSON from `resume`
# TODO 4: validate with Candidate.model_validate_json(...) and print the object
