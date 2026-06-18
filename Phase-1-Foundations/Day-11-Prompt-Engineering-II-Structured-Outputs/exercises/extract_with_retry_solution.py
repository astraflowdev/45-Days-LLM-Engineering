"""
Solution -- Exercise 2: extract with validation + retry.

Run: python extract_with_retry_solution.py
"""

import os

from dotenv import load_dotenv
import google.generativeai as genai
from pydantic import BaseModel, Field, ValidationError

load_dotenv()
genai.configure(api_key=os.environ["GEMINI_API_KEY"])


class Event(BaseModel):
    title: str
    date: str
    attendees: int = Field(ge=0)


text = "The AI Builders Meetup is on 2026-07-15 with about 120 attendees."

model = genai.GenerativeModel(
    "gemini-2.0-flash",
    generation_config={"response_mime_type": "application/json"},
)

base_prompt = (
    "Extract the event as JSON with keys: title (string), date (string), "
    "attendees (integer >= 0).\n"
    f"Text: {text}"
)


def extract(max_tries=3):
    prompt = base_prompt
    for attempt in range(1, max_tries + 1):
        response = model.generate_content(prompt)
        try:
            return Event.model_validate_json(response.text)
        except ValidationError as err:
            print(f"  attempt {attempt} invalid -> retrying")
            prompt = base_prompt + f"\nYour previous answer was invalid: {err}. Return corrected JSON."
    raise RuntimeError("Could not get valid output after 3 tries.")


event = extract()
print("Validated event:", event)
