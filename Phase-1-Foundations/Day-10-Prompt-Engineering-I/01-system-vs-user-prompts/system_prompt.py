"""
System prompts vs user prompts.

The system_instruction sets persistent behaviour; the user prompt is the task.

Setup: pip install google-generativeai python-dotenv  (+ GEMINI_API_KEY in .env)
Run:   python system_prompt.py
"""

import os

from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# The system_instruction applies to EVERY message sent to this model object.
tutor = genai.GenerativeModel(
    "gemini-2.0-flash",
    system_instruction="You are a friendly tutor. Explain like I'm 15, in exactly 2 sentences.",
)

# The same user question, but the persona/format come from the system instruction.
for question in ["What is an API?", "What is a database?"]:
    answer = tutor.generate_content(question).text.strip()
    print("Q:", question)
    print("A:", answer)
    print()

print("Notice: we never repeated 'explain like I'm 15' -- the system prompt did that.")
