"""
Chain-of-thought -- let the model think step by step before answering.

Setup: pip install google-generativeai python-dotenv  (+ GEMINI_API_KEY in .env)
Run:   python chain_of_thought.py
"""

import os

from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-2.0-flash")

problem = (
    "A shop sells pens at Rs 12 each. I buy 5 pens and a Rs 30 notebook, "
    "and pay with a Rs 200 note. How much change do I get?"
)

# Without CoT: ask for just the number (more error-prone on multi-step maths).
direct = model.generate_content(problem + " Reply with only the final amount.")

# With CoT: let it reason, and ask it to end with a parseable final line.
cot = model.generate_content(
    problem + " Let's think step by step, then end with 'Final answer: Rs <amount>'."
)

print("--- Direct answer ---")
print(direct.text.strip())
print()
print("--- Chain-of-thought ---")
print(cot.text.strip())
print()
print("CoT shows its working (5*12=60, +30=90, 200-90=110) -> more reliable.")
