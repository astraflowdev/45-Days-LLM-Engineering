"""
A Groq provider function -- same prompt-in/string-out shape as Gemini.

Setup: pip install groq python-dotenv  (+ GROQ_API_KEY in .env from console.groq.com/keys)
Run:   python groq_provider.py
"""

import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()


def ask_groq(prompt: str) -> str:
    """Send a prompt to Groq (chat-completions format), return the answer text."""
    client = Groq(api_key=os.environ["GROQ_API_KEY"])
    chat = client.chat.completions.create(
        model="llama-3.3-70b-versatile",                 # see README if this name changes
        messages=[{"role": "user", "content": prompt}],
    )
    return chat.choices[0].message.content.strip()


if __name__ == "__main__":
    print(ask_groq("In one sentence, what makes Groq fast?"))
