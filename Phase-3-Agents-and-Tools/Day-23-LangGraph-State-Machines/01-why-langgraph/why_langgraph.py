"""
01 - Why LangGraph? A chain is a straight line; a graph can branch and loop.

Yesterday's LCEL chain was:  prompt | model | parser  -- data flows left to
right, once, no matter what. That's great for "one question -> one answer".

But real apps need to make CHOICES:
    - "if the answer is invalid, try again"      (a LOOP)
    - "route billing questions to a different step than tech questions"  (a BRANCH)
LCEL's | can't do either. LangGraph can, because you describe your app as a
GRAPH of steps (nodes) wired together by edges, all sharing one state dict.

This file builds the SMALLEST possible graph -- one node -- just to meet the
four pieces you'll use all day: State, node, edges (START/END), compile+invoke.
No API key needed: the whole graph engine is plain Python.

Setup:
    pip install langgraph
Run:
    python why_langgraph.py
"""

from typing import TypedDict
from langgraph.graph import StateGraph, START, END

# --- 1. The State ---------------------------------------------------------
# State is ONE dictionary that flows through the graph. Every node reads it
# and returns the parts it changed. We describe its shape with a TypedDict
# (from Day 8) so the keys and types are clear.
class State(TypedDict):
    text: str


# --- 2. A node ------------------------------------------------------------
# A node is JUST A FUNCTION: it takes the current state and returns a dict of
# the keys it wants to update. Here we shout the text.
def shout(state: State) -> dict:
    return {"text": state["text"].upper() + "!"}


# --- 3. Wire the graph ----------------------------------------------------
builder = StateGraph(State)      # a graph whose shared state has this shape
builder.add_node("shout", shout) # register the node under a name

# Edges say "what runs next". START is the entry point, END is the exit.
builder.add_edge(START, "shout") # begin -> shout
builder.add_edge("shout", END)   # shout -> done

# --- 4. Compile, then run -------------------------------------------------
# .compile() turns the blueprint into a runnable app. Like a chain, it has
# .invoke() -- give it the starting state, get the final state back.
graph = builder.compile()

result = graph.invoke({"text": "hello langgraph"})
print("input : hello langgraph")
print("output:", result)                 # {'text': 'HELLO LANGGRAPH!'}
print("just the text:", result["text"])
print()

# --- 5. The point ---------------------------------------------------------
print("This one-node graph does no more than a tiny chain would. The power")
print("comes NEXT: because runs are wired with edges, we can add branches")
print("(module 03) and loops (module 04) -- things a straight | chain cannot do.")
