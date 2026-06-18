"""
Loading secrets from a .env file with python-dotenv.

Demonstrates the safe pattern you'll use for your Gemini key on Day 9:
keys live in .env (never in code, never in Git), loaded into the environment.

Setup: pip install python-dotenv
Run:   python dotenv_secrets.py

Optional: make a file named .env next to this script containing:
    DEMO_API_KEY=hello-from-dotenv
"""

import os

from dotenv import load_dotenv

# Reads a .env file (in this folder or a parent) into the environment.
# If there's no .env, it just does nothing -- no error.
load_dotenv()

# .get() returns None instead of crashing when the variable is missing.
demo_key = os.environ.get("DEMO_API_KEY")

if demo_key:
    print("Loaded DEMO_API_KEY from the environment:", demo_key)
else:
    print("DEMO_API_KEY is not set.")
    print("Create a .env file with:  DEMO_API_KEY=hello-from-dotenv")

print()
print("Notice: the key is NEVER written in this file -- only read from the")
print("environment. That is how every API key in this course is handled.")
