"""
SoftDesk Content Crew -- Step 3: a longer line (researcher -> writer -> editor)

Adding a third agent to the line costs one node + one edge. The Editor tightens the
writer's blurb. Still the sequential pattern -- just longer.

    START -> [researcher] -> [writer] -> [editor] -> END

Run it (needs GROQ_API_KEY in a .env file in this folder):
    python step3_add_editor.py
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
    draft: str
    blurb: str


def _ask(system: str, user: str) -> str:
    return llm.invoke([SystemMessage(content=system), HumanMessage(content=user)]).content.strip()


def researcher(state: State) -> dict:
    system = "You are a Researcher. List 3 short factual selling points for the topic. Bullets only."
    return {"research": _ask(system, state["topic"])}


def writer(state: State) -> dict:
    system = "You are a marketing Writer. Using ONLY these points, write a punchy 2-sentence blurb."
    return {"draft": _ask(system, f"Topic: {state['topic']}\nPoints:\n{state['research']}")}


def editor(state: State) -> dict:
    system = "You are an Editor. Tighten this blurb, keep it to 2 sentences, return only the blurb."
    return {"blurb": _ask(system, state["draft"])}


def build_crew():
    g = StateGraph(State)
    g.add_node("researcher", researcher)
    g.add_node("writer", writer)
    g.add_node("editor", editor)
    g.add_edge(START, "researcher")
    g.add_edge("researcher", "writer")
    g.add_edge("writer", "editor")
    g.add_edge("editor", END)
    return g.compile()


if __name__ == "__main__":
    crew = build_crew()
    result = crew.invoke(
        {"topic": "a free 45-day AI engineering bootcamp", "research": "", "draft": "", "blurb": ""}
    )
    print("DRAFT (writer):\n" + result["draft"])
    print("\nFINAL (editor):\n" + result["blurb"])
    print("\n(3 agents in a line. Next: let a supervisor decide the order -> step4.)")
