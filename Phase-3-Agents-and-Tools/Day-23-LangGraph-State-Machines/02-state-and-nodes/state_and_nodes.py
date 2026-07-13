"""
02 - State & Nodes: how data flows through a multi-step graph.

The one idea to take from this file:
    A NODE IS A FUNCTION. It receives the whole state and returns ONLY the
    keys it changed. LangGraph merges that partial update back into the state
    before the next node runs.

We build a 3-node text pipeline that shares one state:
    clean  ->  count_words  ->  summarize_shape
Each node adds/updates a different key. By the end, the state holds the work
of all three. No API key needed -- this is all plain Python inside the graph.

Setup:
    pip install langgraph
Run:
    python state_and_nodes.py
"""

from typing import TypedDict
from langgraph.graph import StateGraph, START, END


# --- 1. The shared State --------------------------------------------------
# Think of State as a form that gets passed desk to desk; each node fills in
# its own boxes. List every field any node reads or writes.
class State(TypedDict):
    raw: str          # the original input
    cleaned: str      # filled by clean()
    word_count: int   # filled by count_words()
    shape: str        # filled by summarize_shape()


# --- 2. Three nodes, one job each -----------------------------------------
# Each returns a dict with ONLY the key(s) it changed. It does not need to
# copy the other keys forward -- LangGraph keeps them.

def clean(state: State) -> dict:
    text = state["raw"].strip().replace("  ", " ")
    print(f"[clean]  '{state['raw']}' -> '{text}'")
    return {"cleaned": text}

def count_words(state: State) -> dict:
    # Note: this reads 'cleaned', which the PREVIOUS node wrote. State carries
    # each node's work forward automatically.
    n = len(state["cleaned"].split())
    print(f"[count]  {n} words")
    return {"word_count": n}

def summarize_shape(state: State) -> dict:
    n = state["word_count"]
    shape = "short" if n < 5 else "medium" if n < 12 else "long"
    print(f"[shape]  {n} words -> '{shape}'")
    return {"shape": shape}


# --- 3. Wire them in a line -----------------------------------------------
builder = StateGraph(State)
builder.add_node("clean", clean)
builder.add_node("count_words", count_words)
builder.add_node("summarize_shape", summarize_shape)

builder.add_edge(START, "clean")
builder.add_edge("clean", "count_words")        # clean -> count -> shape
builder.add_edge("count_words", "summarize_shape")
builder.add_edge("summarize_shape", END)

graph = builder.compile()


# --- 4. Run it ------------------------------------------------------------
# We only supply the fields we have to start with. The other keys get filled
# in as the state flows through the nodes.
start = {"raw": "  LangGraph  passes state  from node  to node  "}
final = graph.invoke(start)

print()
print("Final state (every node's work is here):")
for key, value in final.items():
    print(f"  {key:12} = {value!r}")

print()
print("Takeaway: nodes are functions; each returns just what it changed; the")
print("shared state carries every node's result forward. That's the whole model.")
