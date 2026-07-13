"""
SOLUTION - Retry Loop (cycles).

Run:
    python retry_loop_solution.py
"""

from typing import TypedDict
from langgraph.graph import StateGraph, START, END

MAX_ATTEMPTS = 20


class State(TypedDict):
    target: int
    value: int
    attempts: int


def step(state: State) -> dict:
    return {"value": state["value"] + 3, "attempts": state["attempts"] + 1}


def keep_going(state: State) -> str:
    if state["value"] >= state["target"]:
        return "done"
    if state["attempts"] >= MAX_ATTEMPTS:      # safety belt: never loop forever
        return "done"
    return "loop"


# --- Build the cycle ------------------------------------------------------
builder = StateGraph(State)
builder.add_node("step", step)
builder.add_edge(START, "step")
builder.add_conditional_edges(
    "step",
    keep_going,
    {"loop": "step", "done": END},     # "loop" -> "step" = the cycle
)

graph = builder.compile()


# --- Run it ---------------------------------------------------------------
if __name__ == "__main__":
    final = graph.invoke({"target": 20, "value": 0, "attempts": 0})
    print(f"Reached {final['value']} (target {final['target']}) "
          f"in {final['attempts']} steps.")
