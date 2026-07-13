"""
04 - A conversational chain with memory (the brain for our Streamlit app).

A RAG chain answers one question. A CHATBOT needs to remember the conversation
so "what did I just ask?" works. We build that with the Day-21 pieces:

    system prompt  +  MessagesPlaceholder("history")  +  the new human message
                       |__ a slot where we inject all past turns __|

The recipe:
    1. keep a `history` list of past messages (human + ai).
    2. each turn: run  chain.invoke({"history": history, "input": user_text}).
    3. append BOTH the user's message and the reply to history.

That's it -- the placeholder re-injects the whole history every turn, so the
model always sees the full conversation. (Module 06 stores this same history in
Streamlit's session_state instead of a plain list.)

Offline-safe: with no key we use a tiny fake model so you can still watch memory
work. This file runs a SCRIPTED conversation; module 05 makes it interactive.

Setup:
    pip install langchain langchain-groq python-dotenv
Run:
    python chatbot.py
"""

import os
from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage

load_dotenv()
MODEL = "llama-3.1-8b-instant"

# --- 1. The prompt with a memory slot -------------------------------------
# MessagesPlaceholder("history") is an empty slot we fill with past turns at
# invoke time. Everything before it (the system line) is the bot's persona.
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a friendly assistant for an Indian e-commerce store. Keep replies short."),
    MessagesPlaceholder("history"),      # <- all previous turns get injected here
    ("human", "{input}"),                # <- this turn's new message
])

# --- 2. Get a model (real Groq, or an offline stand-in) -------------------
if os.getenv("GROQ_API_KEY"):
    from langchain_groq import ChatGroq
    model = ChatGroq(model=MODEL, temperature=0.3)
    print(f"Using real Groq model: {MODEL}\n")
else:
    from langchain_core.runnables import RunnableLambda
    def fake(messages):
        # Proof of memory: count how many past human turns are in the prompt.
        humans = [m for m in messages.messages if isinstance(m, HumanMessage)]
        return AIMessage(content=f"(offline) I can see {len(humans)} of your messages so far.")
    model = RunnableLambda(fake)
    print("No GROQ_API_KEY -- using an offline stand-in so you can see memory work.\n")

# --- 3. The chain: same prompt | model | parser as Day 21 -----------------
chain = prompt | model | StrOutputParser()

# --- 4. Drive a conversation, carrying history ourselves ------------------
history = []      # grows as the chat goes; this IS the memory

def chat(user_text: str) -> None:
    reply = chain.invoke({"history": history, "input": user_text})
    print(f"You : {user_text}")
    print(f"Bot : {reply}\n")
    # Append BOTH sides so the next turn sees them via the placeholder.
    history.append(HumanMessage(content=user_text))
    history.append(AIMessage(content=reply))

chat("Hi! I'm Rohan and my order number is 8842.")
chat("What's my name?")                 # with a key -> "Rohan"
chat("And what order number did I give?")# with a key -> "8842"

print(f"history now holds {len(history)} messages "
      f"({len(history)//2} turns, both sides).")
print("The MessagesPlaceholder re-injects all of them every turn -- that's memory.")
print("Module 05 puts this exact chain behind a Streamlit chat UI.")
