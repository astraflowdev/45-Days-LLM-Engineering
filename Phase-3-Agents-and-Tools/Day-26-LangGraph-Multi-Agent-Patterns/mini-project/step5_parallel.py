"""
SoftDesk Content Crew -- Step 5: a parallel review panel

Before the editor finalises, we send the draft to THREE reviewers at once -- a
fact-checker, an SEO expert, and a tone editor. They run in parallel and their notes
are merged with a reducer; the editor then polishes using all three. This is the
fan-out / fan-in pattern from Module 04, dropped into our line.

  research -> write --+--> [fact-checker] --+
                      +--> [seo-expert] ----+--> [editor uses all notes] -> END
                      +--> [tone-expert] ---+

Run it (needs GROQ_API_KEY in a .env file in this folder):
    python step5_parallel.py
"""

import operator
from typing import Annotated, TypedDict

from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, START, END

load_dotenv()
llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0)


class State(TypedDict):
    topic: str
    research: str
    draft: str
    reviews: Annotated[list, operator.add]  # reducer: keep ALL reviewers' notes
    blurb: str


def _ask(system: str, user: str) -> str:
    return llm.invoke([SystemMessage(content=system), HumanMessage(content=user)]).content.strip()


def researcher(state: State) -> dict:
    system = "You are a Researcher. List 3 short factual selling points for the topic. Bullets only."
    return {"research": _ask(system, state["topic"])}


def writer(state: State) -> dict:
    system = "You are a marketing Writer. Using ONLY these points, write a punchy 2-sentence blurb."
    return {"draft": _ask(system, f"Topic: {state['topic']}\nPoints:\n{state['research']}")}


def _reviewer(name: str, system: str):
    def run(state: State) -> dict:
        note = _ask(system, state["draft"])
        return {"reviews": [f"{name}: {note}"]}   # single-item list -> reducer appends
    return run


fact_checker = _reviewer("fact-checker", "You are a Fact-Checker. Flag any dubious claim in 1 sentence.")
seo_expert = _reviewer("seo-expert", "You are an SEO Expert. Suggest 1 keyword/headline tweak in 1 sentence.")
tone_expert = _reviewer("tone-expert", "You are a Tone Editor. Say in 1 sentence if the tone fits a general audience.")


def editor(state: State) -> dict:
    notes = "\n".join(state["reviews"])
    system = "You are an Editor. Apply the review notes, return ONLY the final 2-sentence blurb."
    return {"blurb": _ask(system, f"Draft:\n{state['draft']}\n\nReview notes:\n{notes}")}


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
    # fan-out: writer -> all three reviewers (run in parallel)
    g.add_edge("writer", "fact_checker")
    g.add_edge("writer", "seo_expert")
    g.add_edge("writer", "tone_expert")
    # fan-in: all three -> editor (waits for all)
    g.add_edge("fact_checker", "editor")
    g.add_edge("seo_expert", "editor")
    g.add_edge("tone_expert", "editor")
    g.add_edge("editor", END)
    return g.compile()


if __name__ == "__main__":
    crew = build_crew()
    result = crew.invoke(
        {"topic": "a free 45-day AI engineering bootcamp",
         "research": "", "draft": "", "reviews": [], "blurb": ""}
    )
    print("REVIEW NOTES:")
    for r in result["reviews"]:
        print("  - " + r)
    print("\nFINAL BLURB:\n" + result["blurb"])
    print("\n(Parallel review added. Next: package it + memory -> step6.)")
