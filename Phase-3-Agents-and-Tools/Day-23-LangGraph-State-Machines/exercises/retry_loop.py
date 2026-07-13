"""
EXERCISE 2 - Retry Loop (cycles).

Build a graph that keeps stepping toward a target, LOOPING until it arrives,
then stops. This is the module-04 cycle on your own.

Fill in every TODO, then run:
    python retry_loop.py
Compare with retry_loop_solution.py. No API key needed.
"""

from typing import TypedDict
from langgraph.graph import StateGraph, START, END

MAX_ATTEMPTS = 20


class State(TypedDict):
    target: int       # the number we want value to reach
    value: int        # our current progress
    attempts: int     # safety counter


def step(state: State) -> dict:
    # TODO: move value closer to target (e.g. +3 each step) and add 1 to attempts.
    #       Return the two changed keys.
    ...


def keep_going(state: State) -> str:
    # TODO: return "done" if value >= target OR attempts >= MAX_ATTEMPTS,
    #       otherwise return "loop".
    ...


# --- Build the cycle ------------------------------------------------------
builder = StateGraph(State)
# TODO: add the "step" node.
# TODO: add_edge(START, "step")
# TODO: add_conditional_edges("step", keep_going, {"loop": "step", "done": END})
#       (the "loop" -> "step" edge is what makes it a cycle)

graph = builder.compile()


# --- Run it ---------------------------------------------------------------
if __name__ == "__main__":
    final = graph.invoke({"target": 20, "value": 0, "attempts": 0})
    print(f"Reached {final['value']} (target {final['target']}) "
          f"in {final['attempts']} steps.")
