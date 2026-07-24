"""
SoftDesk Content Crew -- Step 6: the finished, reusable crew (+ memory)

This is the "brain" other code will import. It combines the patterns:
  * sequential   : researcher -> writer -> ... -> editor
  * parallel     : a fan-out review panel (fact / seo / tone) before the editor
  * memory       : compiled with a checkpointer, so a `thread_id` remembers the
                   blurbs produced earlier in the same campaign

It exposes ONE function -- `run(topic, thread_id)` -> a dict with the final blurb,
the review notes, and a step-by-step trail (for a "How the crew built this" view).
There is NO Streamlit here on purpose, so the crew stays importable and testable;
`app.py` puts a thin UI on top of this.

Run the built-in demo (needs GROQ_API_KEY in a .env file in this folder):
    python step6_content_crew.py
"""

import operator
from typing import Annotated, TypedDict

from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver

load_dotenv()
llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0)


class State(TypedDict):
    topic: str
    research: str
    draft: str
    reviews: Annotated[list, operator.add]    # parallel reviewers accumulate here
    blurb: str
    log: Annotated[list, operator.add]        # the build trail (all nodes append)
    produced: Annotated[list, operator.add]   # MEMORY: every finished blurb on this thread


def _ask(system: str, user: str) -> str:
    return llm.invoke([SystemMessage(content=system), HumanMessage(content=user)]).content.strip()


def researcher(state: State) -> dict:
    system = "You are a Researcher. List 3 short factual selling points for the topic. Bullets only."
    return {"research": _ask(system, state["topic"]), "log": ["researcher gathered 3 points"]}


def writer(state: State) -> dict:
    system = "You are a marketing Writer. Using ONLY these points, write a punchy 2-sentence blurb."
    draft = _ask(system, f"Topic: {state['topic']}\nPoints:\n{state['research']}")
    return {"draft": draft, "log": ["writer produced a draft"]}


def _reviewer(name: str, system: str):
    def run_node(state: State) -> dict:
        note = _ask(system, state["draft"])
        return {"reviews": [f"{name}: {note}"], "log": [f"{name} reviewed the draft"]}
    return run_node


fact_checker = _reviewer("fact-checker", "You are a Fact-Checker. Flag any dubious claim in 1 sentence.")
seo_expert = _reviewer("seo-expert", "You are an SEO Expert. Suggest 1 keyword/headline tweak in 1 sentence.")
tone_expert = _reviewer("tone-expert", "You are a Tone Editor. Say in 1 sentence if the tone fits a general audience.")


def editor(state: State) -> dict:
    notes = "\n".join(state["reviews"])
    system = "You are an Editor. Apply the review notes, return ONLY the final 2-sentence blurb."
    blurb = _ask(system, f"Draft:\n{state['draft']}\n\nReview notes:\n{notes}")
    return {"blurb": blurb, "log": ["editor finalised the blurb"], "produced": [blurb]}


def build_crew():
    g = StateGraph(State)
    for name, fn in [
        ("researcher", researcher), ("writer", writer),
        ("fact_checker", fact_checker), ("seo_expert", seo_expert),
        ("tone_expert", tone_expert), ("editor", editor),
    ]:
        g.add_node(name, fn)
    g.add_edge(START, "researcher")
    g.add_edge("researcher", "writer")
    for r in ("fact_checker", "seo_expert", "tone_expert"):
        g.add_edge("writer", r)   # fan-out
        g.add_edge(r, "editor")   # fan-in
    g.add_edge("editor", END)
    return g.compile(checkpointer=MemorySaver())   # <- memory


# Build once at import time so callers (like app.py) reuse the same crew.
CREW = build_crew()


def run(topic: str, thread_id: str = "default") -> dict:
    """Produce a blurb for `topic`. Same thread_id remembers earlier blurbs."""
    config = {"configurable": {"thread_id": thread_id}}
    state = CREW.invoke(
        {"topic": topic, "research": "", "draft": "", "reviews": [],
         "blurb": "", "log": [], "produced": []},
        config,
    )
    return {
        "blurb": state["blurb"],
        "reviews": state["reviews"],
        "trail": state["log"],
        "produced_so_far": len(state["produced"]),  # grows across turns on a thread
    }


def _demo() -> None:
    print("=" * 66)
    print("SoftDesk Content Crew -- finished")
    print("=" * 66)

    for topic in ["a free 45-day AI engineering bootcamp", "our new resume-review service"]:
        out = run(topic, thread_id="summer-campaign")   # same thread == same campaign
        print(f"\nTOPIC: {topic}")
        print("TRAIL:", " -> ".join(out["trail"]))
        print("BLURB:", out["blurb"])
        print(f"(blurbs produced on this campaign so far: {out['produced_so_far']})")


if __name__ == "__main__":
    _demo()
