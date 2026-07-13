"""
SOLUTION - Persona Chatbot.

Run:
    python persona_chatbot_solution.py
"""

import os
from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage

load_dotenv()
MODEL = "llama-3.1-8b-instant"

PERSONA = "You are a cheerful travel guide for Rajasthan. Keep replies to 2 sentences."

prompt = ChatPromptTemplate.from_messages([
    ("system", PERSONA),
    MessagesPlaceholder("history"),
    ("human", "{input}"),
])

if os.getenv("GROQ_API_KEY"):
    from langchain_groq import ChatGroq
    model = ChatGroq(model=MODEL, temperature=0.5)
else:
    from langchain_core.runnables import RunnableLambda
    def fake(pv):
        humans = [m for m in pv.messages if isinstance(m, HumanMessage)]
        return AIMessage(content=f"(offline) persona set; I recall {len(humans)} of your messages.")
    model = RunnableLambda(fake)

chain = prompt | model | StrOutputParser()

history = []

def chat(user_text: str) -> None:
    reply = chain.invoke({"history": history, "input": user_text})
    print(f"You : {user_text}")
    print(f"Bot : {reply}\n")
    history.append(HumanMessage(content=user_text))
    history.append(AIMessage(content=reply))

if __name__ == "__main__":
    chat("Hi, I'm visiting Jaipur next week.")
    chat("What did I say I'm visiting?")     # must recall "Jaipur"
    chat("Suggest one thing to eat there.")
    print(f"history holds {len(history)} messages.")
