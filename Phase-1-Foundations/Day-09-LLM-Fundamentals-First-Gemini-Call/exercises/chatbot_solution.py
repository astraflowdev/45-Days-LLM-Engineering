"""
Solution -- Exercise 1: a command-line chatbot with memory.

Run: python chatbot_solution.py   (type 'quit' to exit)
"""

import os

from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-2.0-flash")

# start_chat() keeps the running history for us, so the bot remembers context.
chat = model.start_chat()

print("Chatbot ready. Type 'quit' to exit.")
while True:
    user_message = input("You: ")
    if user_message.strip().lower() == "quit":
        print("Bye!")
        break
    response = chat.send_message(user_message)
    print("Bot:", response.text.strip())
