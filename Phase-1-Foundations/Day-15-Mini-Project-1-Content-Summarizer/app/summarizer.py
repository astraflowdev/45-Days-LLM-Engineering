"""
summarizer.py -- text -> a validated structured Summary, using Gemini.

Combines Day 9 (Gemini call), Day 11 (JSON mode + Pydantic + retry), and a
small token cap so huge inputs don't blow the budget.

Setup: pip install google-generativeai pydantic python-dotenv  (+ GEMINI_API_KEY)
"""

import os

from dotenv import load_dotenv
import google.generativeai as genai
from pydantic import BaseModel, ValidationError

load_dotenv()


class Summary(BaseModel):
    tldr: str
    key_points: list[str]
    action_items: list[str]


def _model():
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])
    return genai.GenerativeModel(
        "gemini-2.0-flash",
        generation_config={"response_mime_type": "application/json"},
    )


# Keep input within a sane size (rough char cap ~ token budget). Big docs are a
# Phase 2 / RAG problem; here we simply trim.
MAX_CHARS = 20000


def summarize(text: str, max_tries: int = 3) -> Summary:
    """Return a validated Summary for the given text (retries on bad output)."""
    text = text[:MAX_CHARS]
    base_prompt = (
        "Summarize the content between <content> tags. Return JSON with keys: "
        "tldr (one sentence), key_points (array of 3-6 short strings), "
        "action_items (array of strings; empty if none).\n"
        f"<content>\n{text}\n</content>"
    )

    model = _model()
    prompt = base_prompt
    for attempt in range(1, max_tries + 1):
        response = model.generate_content(prompt)
        try:
            return Summary.model_validate_json(response.text)
        except ValidationError as err:
            if attempt == max_tries:
                raise
            prompt = base_prompt + f"\nYour previous answer was invalid: {err}. Return corrected JSON."


if __name__ == "__main__":
    sample = (
        "Our Q2 sales rose 18% driven by the new mobile app. Support tickets fell "
        "after the onboarding redesign. We plan to expand to two new cities next "
        "quarter and hire three engineers."
    )
    result = summarize(sample)
    print("TL;DR:", result.tldr)
    print("Key points:", result.key_points)
    print("Action items:", result.action_items)
