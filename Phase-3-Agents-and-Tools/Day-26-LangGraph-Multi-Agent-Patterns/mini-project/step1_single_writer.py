"""
SoftDesk Content Crew -- Step 1: a single writer agent

We're going to build a small "content crew" that turns a TOPIC into a short,
polished marketing blurb. We'll grow it one agent (one pattern) at a time, exactly
mirroring today's modules. This step is the seed: ONE agent, ONE node.

    START -> [writer] -> END

Run it (needs a free GROQ_API_KEY in a .env file in this folder):
    python step1_single_writer.py
"""

from typing import TypedDict

from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, START, END

load_dotenv()
llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0)


class State(TypedDict):
    topic: str
    blurb: str


def writer(state: State) -> dict:
    system = "You are a marketing Writer. Write a punchy 2-sentence blurb for the topic."
    blurb = llm.invoke(
        [SystemMessage(content=system), HumanMessage(content=state["topic"])]
    ).content.strip()
    return {"blurb": blurb}


def build_crew():
    g = StateGraph(State)
    g.add_node("writer", writer)
    g.add_edge(START, "writer")
    g.add_edge("writer", END)
    return g.compile()


if __name__ == "__main__":
    crew = build_crew()
    result = crew.invoke({"topic": "a free 45-day AI engineering bootcamp", "blurb": ""})
    print("BLURB:\n" + result["blurb"])
    print("\n(1 agent. Next: hand it some research first -> step2.)")
