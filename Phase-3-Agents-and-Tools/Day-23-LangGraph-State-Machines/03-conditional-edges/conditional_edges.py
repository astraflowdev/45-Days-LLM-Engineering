"""
03 - Conditional edges: let the graph CHOOSE the next node.

A normal edge is fixed:  add_edge("a", "b")  always goes a -> b.
A CONDITIONAL edge runs a little "router" function that looks at the state and
RETURNS THE NAME of where to go next. This is the branching a | chain can't do.

    add_conditional_edges("classify", route, {"billing": "billing", ...})
                           ^source     ^router  ^map: router's return -> node

We build a support-desk router: classify a message, then branch to the matching
handler node. Pure Python (rule-based) so it runs with no API key -- the point
is the GRAPH SHAPE, not the classifier. (A real app would classify with a model.)

Setup:
    pip install langgraph
Run:
    python conditional_edges.py
"""

from typing import TypedDict
from langgraph.graph import StateGraph, START, END


class State(TypedDict):
    message: str      # the incoming support message
    category: str     # set by classify()
    reply: str        # set by one of the handler nodes


# --- 1. A node that inspects the input ------------------------------------
# It only records a category; it does NOT decide the edge. (Deciding is the
# router's job -- keeping them separate keeps nodes reusable.)
def classify(state: State) -> dict:
    text = state["message"].lower()
    if any(w in text for w in ("refund", "charge", "invoice", "payment")):
        category = "billing"
    elif any(w in text for w in ("error", "crash", "bug", "login", "broken")):
        category = "technical"
    else:
        category = "general"
    print(f"[classify] '{state['message']}' -> {category}")
    return {"category": category}


# --- 2. The router function -----------------------------------------------
# It looks at the state and RETURNS A STRING. That string is looked up in the
# mapping we pass to add_conditional_edges to pick the next node. The router
# returns a routing key -- it does not change the state.
def route(state: State) -> str:
    return state["category"]      # "billing" | "technical" | "general"


# --- 3. One handler node per branch ---------------------------------------
def billing(state: State) -> dict:
    return {"reply": "Billing team here -- we'll review your charge within 24h."}

def technical(state: State) -> dict:
    return {"reply": "Tech support here -- please share your app version & a screenshot."}

def general(state: State) -> dict:
    return {"reply": "Thanks for reaching out! A team member will get back to you."}


# --- 4. Wire the branch ---------------------------------------------------
builder = StateGraph(State)
builder.add_node("classify", classify)
builder.add_node("billing", billing)
builder.add_node("technical", technical)
builder.add_node("general", general)

builder.add_edge(START, "classify")

# The star of the show: after "classify", run route(state); its return value
# is looked up in this dict to choose the next node.
builder.add_conditional_edges(
    "classify",
    route,
    {
        "billing": "billing",       # route() returns "billing" -> go to billing node
        "technical": "technical",
        "general": "general",
    },
)

# All three branches lead to the exit.
builder.add_edge("billing", END)
builder.add_edge("technical", END)
builder.add_edge("general", END)

graph = builder.compile()


# --- 5. Try a few messages: same graph, different paths -------------------
for msg in [
    "I want a refund for my last invoice",
    "The app keeps crashing on login",
    "Do you have an office in Pune?",
]:
    result = graph.invoke({"message": msg, "category": "", "reply": ""})
    print(f"  [{result['category']:9}] {result['reply']}")
    print()

print("Same compiled graph, three different routes -- decided at runtime by the")
print("data. That branching is exactly what LCEL's straight | cannot express.")
