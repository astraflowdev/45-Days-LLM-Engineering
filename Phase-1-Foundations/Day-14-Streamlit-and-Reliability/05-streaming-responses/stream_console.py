"""
Streaming a Gemini response to the console, token by token.

Setup: pip install google-generativeai python-dotenv  (+ GEMINI_API_KEY in .env)
Run:   python stream_console.py
"""

import os

from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-2.0-flash")

# stream=True -> we get pieces as they're generated instead of one final blob.
response = model.generate_content(
    "Write a 4-line poem about learning to code.",
    stream=True,
)

print("Streaming answer:\n")
full = []
for chunk in response:
    piece = chunk.text
    print(piece, end="", flush=True)     # show it immediately
    full.append(piece)

print()
print("\n(Full answer length:", len("".join(full)), "chars)")
