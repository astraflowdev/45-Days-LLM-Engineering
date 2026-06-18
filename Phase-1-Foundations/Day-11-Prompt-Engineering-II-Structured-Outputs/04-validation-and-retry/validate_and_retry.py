"""
Validation + retry -- only let CORRECT data through.

Asks the model for JSON, validates into Pydantic, and retries with the error
message if validation fails.

Setup: pip install google-generativeai pydantic python-dotenv  (+ GEMINI_API_KEY in .env)
Run:   python validate_and_retry.py
"""

import os

from dotenv import load_dotenv
import google.generativeai as genai
from pydantic import BaseModel, Field, ValidationError

load_dotenv()
genai.configure(api_key=os.environ["GEMINI_API_KEY"])


class Product(BaseModel):
    name: str
    price_inr: float = Field(gt=0)        # must be positive
    in_stock: bool


model = genai.GenerativeModel(
    "gemini-2.0-flash",
    generation_config={"response_mime_type": "application/json"},
)

base_prompt = (
    "Extract the product as JSON with keys: name (string), price_inr (number > 0), "
    "in_stock (boolean).\n"
    "Text: The Acme gel pen costs Rs 25 and is available now."
)


def extract_product(max_tries=3):
    prompt = base_prompt
    for attempt in range(1, max_tries + 1):
        response = model.generate_content(prompt)
        try:
            # Parses the JSON string AND validates it in one step.
            return Product.model_validate_json(response.text)
        except ValidationError as err:
            print(f"  attempt {attempt} invalid -> retrying")
            prompt = base_prompt + f"\nYour previous answer was invalid: {err}. Return corrected JSON."
    raise RuntimeError("Model failed to produce valid output after retries.")


product = extract_product()
print("Validated product:", product)
