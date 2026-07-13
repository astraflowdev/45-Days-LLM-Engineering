"""
04 - Cycles & loops: the move a straight | chain can NEVER make.

A chain goes forward only. A graph edge can point BACKWARD -- a node can lead
to itself -- so the graph LOOPS until a condition says "stop". This is how an
agent "keeps trying": generate -> check -> (not good enough? -> generate again).

The loop is built with a conditional edge (module 03) whose router returns
either the node's own name ("go around again") or END ("we're done").

    add_conditional_edges("work", keep_going, {"loop": "work", "done": END})

Example: keep drafting a password until it passes 3 rules -- no key needed.
Because loops can run forever, LangGraph enforces a recursion_limit; we also
carry our own attempt counter as a safety belt (good habit for real agents).

Setup:
    pip install langgraph
Run:
    python cycles_and_loops.py
"""

from typing import TypedDict
from langgraph.graph import StateGraph, START, END


class State(TypedDict):
    candidate: str    # the latest attempt
    attempts: int     # how many tries so far (our own safety counter)
    ok: bool          # did the last candidate pass the rules?


# A deterministic stand-in for "the model tries something new each time".
# (In a real agent this node would call Groq; here we grow the string so the
# loop visibly makes progress and eventually passes.)
def make_candidate(attempts: int) -> str:
    base = "pass"
    extras = ["1", "!", "Word", "9"][:attempts]   # add one piece per attempt
    return base + "".join(extras)


def is_strong(pw: str) -> bool:
    has_digit = any(c.isdigit() for c in pw)
    has_symbol = any(c in "!@#$%" for c in pw)
    long_enough = len(pw) >= 8
    return has_digit and has_symbol and long_enough


# --- 1. The work node -----------------------------------------------------
def draft(state: State) -> dict:
    n = state["attempts"] + 1
    pw = make_candidate(n)
    ok = is_strong(pw)
    print(f"[draft] attempt {n}: '{pw}'  strong={ok}")
    return {"candidate": pw, "attempts": n, "ok": ok}


# --- 2. The loop decision -------------------------------------------------
# Return "done" when the rules pass OR we've tried too many times; otherwise
# "loop" to run draft() again. ALWAYS give a loop a way out.
MAX_ATTEMPTS = 6

def keep_going(state: State) -> str:
    if state["ok"]:
        return "done"
    if state["attempts"] >= MAX_ATTEMPTS:
        print("[guard] hit attempt cap -- stopping to avoid an infinite loop")
        return "done"
    return "loop"


# --- 3. Wire the cycle ----------------------------------------------------
builder = StateGraph(State)
builder.add_node("draft", draft)
builder.add_edge(START, "draft")

# The edge that makes it a LOOP: "loop" points back to draft itself.
builder.add_conditional_edges(
    "draft",
    keep_going,
    {
        "loop": "draft",   # <-- back to the same node = a cycle
        "done": END,
    },
)

graph = builder.compile()


# --- 4. Run it ------------------------------------------------------------
final = graph.invoke({"candidate": "", "attempts": 0, "ok": False})

print()
print(f"Finished after {final['attempts']} attempts.")
print(f"Final password: {final['candidate']}  (strong={final['ok']})")
print()
print("A backward edge turned a one-shot step into 'keep trying until good'.")
print("generate -> check -> loop-or-stop is the skeleton of every agent (Day 25).")
