"""
EXERCISE 2 - Persona Chatbot.

A memory-carrying chatbot whose system persona you can swap. Fill in every TODO,
then run:
    python persona_chatbot.py
Compare with persona_chatbot_solution.py. Memory works with no key (an offline
stand-in shows the history growing); add GROQ_API_KEY for real replies.
"""

import os
from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage

load_dotenv()
MODEL = "llama-3.1-8b-instant"

PERSONA = "You are a cheerful travel guide for Rajasthan. Keep replies to 2 sentences."

# TODO 1: build a prompt with three parts:
#   ("system", PERSONA), MessagesPlaceholder("history"), ("human", "{input}")
prompt = ...

# --- model: real Groq, or an offline stand-in -----------------------------
if os.getenv("GROQ_API_KEY"):
    from langchain_groq import ChatGroq
    model = ChatGroq(model=MODEL, temperature=0.5)
else:
    from langchain_core.runnables import RunnableLambda
    def fake(pv):
        humans = [m for m in pv.messages if isinstance(m, HumanMessage)]
        return AIMessage(content=f"(offline) persona set; I recall {len(humans)} of your messages.")
    model = RunnableLambda(fake)

# TODO 2: build the chain: prompt | model | StrOutputParser()
chain = ...

history = []

def chat(user_text: str) -> None:
    # TODO 3: invoke the chain with {"history": history, "input": user_text},
    #         print "You"/"Bot", then append HumanMessage + AIMessage to history.
    ...

if __name__ == "__main__":
    chat("Hi, I'm visiting Jaipur next week.")
    chat("What did I say I'm visiting?")     # must recall "Jaipur"
    chat("Suggest one thing to eat there.")
    print(f"history holds {len(history)} messages.")
