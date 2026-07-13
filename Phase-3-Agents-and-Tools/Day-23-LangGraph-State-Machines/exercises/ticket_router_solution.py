"""
SOLUTION - Ticket Router (conditional edges).

Run:
    python ticket_router_solution.py
"""

from typing import TypedDict
from langgraph.graph import StateGraph, START, END


class State(TypedDict):
    message: str
    priority: str     # "high" or "low"
    reply: str


HIGH_WORDS = ("urgent", "down", "refund", "asap", "immediately", "charged twice")


def triage(state: State) -> dict:
    text = state["message"].lower()
    priority = "high" if any(w in text for w in HIGH_WORDS) else "low"
    return {"priority": priority}


def route(state: State) -> str:
    return state["priority"]          # "high" or "low" -> looked up in the edge map


def escalate(state: State) -> dict:
    return {"reply": "Escalated to an on-call engineer -- expect a call within 15 minutes."}


def auto_reply(state: State) -> dict:
    return {"reply": "Thanks! Here's our help centre; an agent will follow up within 2 days."}


# --- Build the graph ------------------------------------------------------
builder = StateGraph(State)
builder.add_node("triage", triage)
builder.add_node("escalate", escalate)
builder.add_node("auto_reply", auto_reply)

builder.add_edge(START, "triage")
builder.add_conditional_edges(
    "triage",
    route,
    {"high": "escalate", "low": "auto_reply"},
)
builder.add_edge("escalate", END)
builder.add_edge("auto_reply", END)

graph = builder.compile()


# --- Try it ---------------------------------------------------------------
if __name__ == "__main__":
    for msg in [
        "The payment page is DOWN and customers are angry",
        "How do I change my profile picture?",
    ]:
        result = graph.invoke({"message": msg, "priority": "", "reply": ""})
        print(f"[{result['priority']:4}] {msg}")
        print(f"       -> {result['reply']}\n")
