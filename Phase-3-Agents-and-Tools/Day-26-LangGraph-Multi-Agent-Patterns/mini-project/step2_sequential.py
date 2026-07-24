"""
SoftDesk Content Crew -- Step 2: sequential (researcher -> writer)

A blurb is better when it's grounded in facts. So we put a Researcher agent BEFORE
the writer. The researcher's notes flow to the writer through the shared state --
the sequential pattern from Module 02.

    START -> [researcher] -> [writer] -> END

Run it (needs GROQ_API_KEY in a .env file in this folder):
    python step2_sequential.py
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
    research: str
    blurb: str


def _ask(system: str, user: str) -> str:
    return llm.invoke([SystemMessage(content=system), HumanMessage(content=user)]).content.strip()


def researcher(state: State) -> dict:
    system = "You are a Researcher. List 3 short factual selling points for the topic. Bullets only."
    return {"research": _ask(system, state["topic"])}


def writer(state: State) -> dict:
    system = "You are a marketing Writer. Using ONLY these points, write a punchy 2-sentence blurb."
    return {"blurb": _ask(system, f"Topic: {state['topic']}\nPoints:\n{state['research']}")}


def build_crew():
    g = StateGraph(State)
    g.add_node("researcher", researcher)
    g.add_node("writer", writer)
    g.add_edge(START, "researcher")
    g.add_edge("researcher", "writer")
    g.add_edge("writer", END)
    return g.compile()


if __name__ == "__main__":
    crew = build_crew()
    result = crew.invoke(
        {"topic": "a free 45-day AI engineering bootcamp", "research": "", "blurb": ""}
    )
    print("RESEARCH:\n" + result["research"])
    print("\nBLURB:\n" + result["blurb"])
    print("\n(2 agents in a line. Next: add an editor -> step3.)")
