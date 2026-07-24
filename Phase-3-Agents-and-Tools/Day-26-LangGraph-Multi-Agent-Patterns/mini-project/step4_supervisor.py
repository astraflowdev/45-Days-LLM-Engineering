"""
SoftDesk Content Crew -- Step 4: a supervisor decides the order

Up to now the order was hard-wired. Now a Supervisor agent looks at what's done so
far and DECIDES the next step -- research, write, edit, or FINISH -- routing to that
worker and looping back to itself. This is the supervisor pattern from Module 03.

              +----------------+
     +------> |   supervisor   | <------+
     |        +-------+--------+        |
     v            |        |            v
 [researcher]  [writer]  [editor]  ... -> FINISH -> END

Why bother if the order looks fixed? Because the boss is now data-driven: give it a
draft that's already written and it will skip straight to editing. The routing lives
in ONE place, not smeared across edges.

Run it (needs GROQ_API_KEY in a .env file in this folder):
    python step4_supervisor.py
"""

from typing import TypedDict

from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, START, END

load_dotenv()
llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0)

ACTIONS = ["research", "write", "edit", "FINISH"]


class State(TypedDict):
    topic: str
    research: str
    draft: str
    blurb: str
    next: str


def _ask(system: str, user: str) -> str:
    return llm.invoke([SystemMessage(content=system), HumanMessage(content=user)]).content.strip()


def supervisor(state: State) -> dict:
    """Decide the next action from what's already in the state."""
    status = (
        f"research done: {bool(state['research'])}, "
        f"draft written: {bool(state['draft'])}, "
        f"final edited: {bool(state['blurb'])}"
    )
    system = (
        "You are the Editor-in-Chief of a content crew. Given the progress, choose the "
        "SINGLE next step: 'research' (if no research yet), 'write' (research done, no "
        "draft), 'edit' (draft done, not yet finalised), or 'FINISH' (final is ready). "
        "Reply with ONLY that one word."
    )
    choice = _ask(system, f"Topic: {state['topic']}. Progress -> {status}").lower()
    choice = next((a for a in ACTIONS if a.lower() in choice), "FINISH")
    print(f"[supervisor] progress: {status}  ->  next: {choice}")
    return {"next": choice}


def researcher(state: State) -> dict:
    system = "You are a Researcher. List 3 short factual selling points for the topic. Bullets only."
    return {"research": _ask(system, state["topic"])}


def writer(state: State) -> dict:
    system = "You are a marketing Writer. Using ONLY these points, write a punchy 2-sentence blurb."
    return {"draft": _ask(system, f"Topic: {state['topic']}\nPoints:\n{state['research']}")}


def editor(state: State) -> dict:
    system = "You are an Editor. Tighten this blurb, keep it to 2 sentences, return only the blurb."
    return {"blurb": _ask(system, state["draft"])}


def route(state: State) -> str:
    """Map the supervisor's decision to a worker node (or END)."""
    if state["next"] == "FINISH":
        return END
    return {"research": "researcher", "write": "writer", "edit": "editor"}[state["next"]]


def build_crew():
    g = StateGraph(State)
    g.add_node("supervisor", supervisor)
    g.add_node("researcher", researcher)
    g.add_node("writer", writer)
    g.add_node("editor", editor)

    g.add_edge(START, "supervisor")
    g.add_conditional_edges("supervisor", route, ["researcher", "writer", "editor", END])
    # Every worker reports back to the boss -> the supervisor loop.
    g.add_edge("researcher", "supervisor")
    g.add_edge("writer", "supervisor")
    g.add_edge("editor", "supervisor")
    return g.compile()


if __name__ == "__main__":
    crew = build_crew()
    # recursion_limit is the safety belt from Day 24 -- caps the supervisor loop.
    result = crew.invoke(
        {"topic": "a free 45-day AI engineering bootcamp",
         "research": "", "draft": "", "blurb": "", "next": ""},
        {"recursion_limit": 12},
    )
    print("\nFINAL BLURB:\n" + result["blurb"])
    print("\n(A boss now drives the crew. Next: add a parallel review panel -> step5.)")
