"""
EXERCISE 1 - Ticket Router (conditional edges).

Build a graph that reads a support message, decides a priority, and BRANCHES
to the matching handler node. This is the module-03 pattern on your own.

Fill in every TODO, then run:
    python ticket_router.py
Compare with ticket_router_solution.py. No API key needed.
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
    # TODO: set priority to "high" if any HIGH_WORDS appear in text, else "low".
    #       Return {"priority": ...}
    ...


def route(state: State) -> str:
    # TODO: return the routing key -- "high" or "low" -- based on state["priority"].
    ...


def escalate(state: State) -> dict:
    # TODO: return {"reply": "..."} for a high-priority ticket (e.g. paged a human).
    ...


def auto_reply(state: State) -> dict:
    # TODO: return {"reply": "..."} for a low-priority ticket (a friendly auto-response).
    ...


# --- Build the graph ------------------------------------------------------
builder = StateGraph(State)
# TODO: add the four nodes: triage, escalate, auto_reply.
# TODO: add_edge(START, "triage")
# TODO: add_conditional_edges("triage", route, {"high": "escalate", "low": "auto_reply"})
# TODO: send both handlers to END.

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
