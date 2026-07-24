"""
Day 26 - Module 01: Why multi-agent? (and the three shapes)

The big idea: an "agent" is just a NODE in a LangGraph graph. Once you see that,
building a *team* of agents is nothing new -- it's the same StateGraph you learned
on Day 24, with more than one worker wired in.

This script needs NO API key and NO LLM. It builds a tiny two-"agent" graph out of
plain Python functions so you can see the shape, then prints the three team shapes
you'll build across today's modules.

Run it:
    python why_multi_agent.py
"""

from typing import TypedDict
from langgraph.graph import StateGraph, START, END


# --- The shared "desk" every agent writes on ---------------------------------
# On Day 24 you learned: the STATE is the shared memory that flows through the
# graph. Every agent (node) reads what it needs and returns only the keys it
# changed. Nothing else changes here for multi-agent -- there are just more nodes.
class State(TypedDict):
    topic: str
    draft: str
    log: list  # a running trail so we can SEE who did what


# --- Two "agents" -- each is just a function -------------------------------
# No LLM yet. The point is structural: agent == node == "a worker that transforms
# the shared state." Tomorrow's modules swap these bodies for real Groq calls.
def writer(state: State) -> dict:
    """Agent #1: turns a topic into a rough one-liner."""
    draft = f"{state['topic']} is useful because it saves people time."
    return {"draft": draft, "log": ["writer wrote a rough draft"]}


def editor(state: State) -> dict:
    """Agent #2: polishes whatever the writer handed over via the state."""
    polished = state["draft"].replace("useful", "genuinely useful").rstrip(".") + "!"
    # Carry the log forward by hand (a plain list key OVERWRITES otherwise -- you'll
    # meet `reducers`, the proper fix for accumulating lists, in Module 04).
    return {"draft": polished, "log": state["log"] + ["editor polished the draft"]}


def build_team():
    """Wire the two agents into a straight line: writer -> editor."""
    g = StateGraph(State)
    g.add_node("writer", writer)
    g.add_node("editor", editor)
    g.add_edge(START, "writer")   # start hands the topic to the writer
    g.add_edge("writer", "editor")  # writer hands the draft to the editor
    g.add_edge("editor", END)
    return g.compile()


THREE_SHAPES = r"""
The three shapes of an agent team (all just graphs):

1) SEQUENTIAL  (an assembly line)         -> Module 02
   START -> [research] -> [write] -> [edit] -> END
   Each agent adds one piece; state carries the hand-off forward.

2) SUPERVISOR / HIERARCHICAL (a boss)      -> Module 03
                 +-------------+
        +------> | supervisor  | <------+       the boss ROUTES work to a
        |        +------+------+        |       worker, the worker reports
        v               |              v        back, the boss decides who is
   [researcher]     [writer]       [editor]     next -- or that it's done.

3) PARALLEL  (fan-out / fan-in)            -> Module 04
                  +--> [fact-checker] --+
   [dispatch] ----+--> [seo-expert] ----+---> [merge]
                  +--> [tone-expert] ---+
   All specialists run at once; a reducer collects their notes.
"""


def main() -> None:
    print("=" * 66)
    print("Why multi-agent? Because one agent is just ONE node.")
    print("=" * 66)

    team = build_team()
    result = team.invoke({"topic": "LangGraph", "draft": "", "log": []})

    print("\nA 2-agent team ran (writer -> editor), no LLM, no key:\n")
    for line in result["log"]:
        print("  -", line)
    print("\nFinal draft:", result["draft"])

    print(THREE_SHAPES)

    print("Take-away:")
    print("  * An agent = a node. A team = a graph of nodes.")
    print("  * You ALREADY know the engine (Day 24). Today = wiring patterns.")
    print("  * When one agent isn't enough, reach for one of the 3 shapes above.")


if __name__ == "__main__":
    main()
