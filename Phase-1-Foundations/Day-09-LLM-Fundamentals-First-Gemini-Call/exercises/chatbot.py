"""
Exercise 1 -- a command-line chatbot that remembers the conversation.

Setup: pip install google-generativeai python-dotenv  (+ GEMINI_API_KEY in .env)
Run:   python chatbot.py
"""

import os

from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-2.0-flash")

# TODO 1: start a chat session that keeps history:  chat = model.start_chat()
# TODO 2: loop forever:
#           - read the user's message with input("You: ")
#           - if it is "quit", break
#           - send it with chat.send_message(...) and print the reply (response.text)
