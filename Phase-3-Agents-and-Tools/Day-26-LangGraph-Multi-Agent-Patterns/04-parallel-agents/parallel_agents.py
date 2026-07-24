"""
Day 26 - Module 04: Parallel agents (fan-out / fan-in)

Sometimes several agents should look at the SAME input independently and at the
same time -- like sending a draft to three reviewers at once:

                  +--> [fact-checker] --+
   [dispatch] ----+--> [seo-expert] ----+---> [aggregate] --> END
                  +--> [tone-expert] ---+

Two LangGraph mechanics make this work:
  1. FAN-OUT: add an edge from one node to SEVERAL nodes -> they run in parallel.
  2. FAN-IN with a REDUCER: each specialist appends to a shared list. A plain state
     key would OVERWRITE (last writer wins); `Annotated[list, add]` ACCUMULATES, so
     all three notes survive. (You met reducers on Day 24.)

The `aggregate` node has three incoming edges, so LangGraph waits for ALL three
specialists to finish before running it -- that's the "fan-in".

Run it (needs a free GROQ_API_KEY in a .env file next to this script):
    python parallel_agents.py
"""

import operator
from typing import Annotated, TypedDict

from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, START, END

load_dotenv()
llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0)


# --- Shared state ------------------------------------------------------------
class State(TypedDict):
    draft: str
    # The reducer: every specialist RETURNS a one-item list; `operator.add`
    # concatenates them so all three reviews are kept, not overwritten.
    reviews: Annotated[list, operator.add]
    summary: str


def _review(name: str, system: str):
    """Build one specialist node. Each returns a SINGLE-item list -> the reducer joins them."""
    def run(state: State) -> dict:
        note = llm.invoke(
            [SystemMessage(content=system), HumanMessage(content=state["draft"])]
        ).content.strip()
        print(f"[{name}] reviewed the draft.")
        return {"reviews": [f"{name}: {note}"]}  # note the LIST -> reducer appends it
    return run


fact_checker = _review(
    "fact-checker",
    "You are a Fact-Checker. Point out any claim in the text that needs verifying. Be brief (1-2 sentences).",
)
seo_expert = _review(
    "seo-expert",
    "You are an SEO Expert. Suggest one keyword or headline tweak to improve reach. Be brief (1-2 sentences).",
)
tone_expert = _review(
    "tone-expert",
    "You are a Tone Editor. Comment on whether the tone fits a general audience. Be brief (1-2 sentences).",
)


def aggregate(state: State) -> dict:
    """Fan-in: runs only after ALL specialists finish. Collate their notes."""
    summary = "\n".join(f"  - {r}" for r in state["reviews"])
    print("\n[aggregate] collected all reviews.")
    return {"summary": summary}


def build_panel():
    g = StateGraph(State)
    g.add_node("fact_checker", fact_checker)
    g.add_node("seo_expert", seo_expert)
    g.add_node("tone_expert", tone_expert)
    g.add_node("aggregate", aggregate)

    # FAN-OUT: START points at all three -> they run concurrently.
    g.add_edge(START, "fact_checker")
    g.add_edge(START, "seo_expert")
    g.add_edge(START, "tone_expert")
    # FAN-IN: all three point at aggregate -> it waits for all of them.
    g.add_edge("fact_checker", "aggregate")
    g.add_edge("seo_expert", "aggregate")
    g.add_edge("tone_expert", "aggregate")
    g.add_edge("aggregate", END)
    return g.compile()


def main() -> None:
    print("=" * 66)
    print("Parallel agents: three reviewers look at one draft at once")
    print("=" * 66)

    draft = (
        "Python is the most popular language in the world and every AI company uses "
        "it. Learn Python today and you will get a job instantly."
    )
    print("\nDRAFT UNDER REVIEW:\n" + draft + "\n")

    panel = build_panel()
    result = panel.invoke({"draft": draft, "reviews": [], "summary": ""})

    print("\n" + "=" * 66)
    print("PANEL FEEDBACK (all three, merged by the reducer)")
    print("=" * 66)
    print(result["summary"])

    print(
        "\nWhy parallel: the three reviewers don't depend on each other, so running\n"
        "them in sequence would just waste time. The reducer (`Annotated[list, add]`)\n"
        "is the key -- without it the last specialist would overwrite the other two."
    )


if __name__ == "__main__":
    main()
