"""
Exercise 2 -- extract with validation + retry.

Setup: pip install google-generativeai pydantic python-dotenv  (+ GEMINI_API_KEY in .env)
Run:   python extract_with_retry.py
"""

import os

from dotenv import load_dotenv
import google.generativeai as genai
from pydantic import BaseModel, Field, ValidationError

load_dotenv()
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

text = "The AI Builders Meetup is on 2026-07-15 with about 120 attendees."

# TODO 1: define an Event model: title: str, date: str, attendees: int (Field(ge=0))
# TODO 2: make a JSON-mode model and a base prompt that asks for those keys
# TODO 3: loop up to 3 times: generate -> Event.model_validate_json(...)
#         on ValidationError, append the error to the prompt and retry
# TODO 4: print the validated Event, or a clear failure message after 3 tries
