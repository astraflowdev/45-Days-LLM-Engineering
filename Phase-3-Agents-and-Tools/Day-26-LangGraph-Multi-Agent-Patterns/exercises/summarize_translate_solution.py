"""
Exercise 1 (solution): a sequential 2-agent line -- summarizer -> translator

    START -> [summarizer] -> [translator] -> END

The summarizer condenses a long text; the translator turns that summary into Hindi.
The summary flows from one agent to the next through the shared state.

Run it (needs GROQ_API_KEY in a .env file in this folder):
    python summarize_translate_solution.py
"""

from typing import TypedDict

from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, START, END

load_dotenv()
llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0)


class State(TypedDict):
    text: str          # the long input
    summary: str       # filled by the summarizer
    translation: str   # filled by the translator


def _ask(system: str, user: str) -> str:
    return llm.invoke([SystemMessage(content=system), HumanMessage(content=user)]).content.strip()


def summarizer(state: State) -> dict:
    system = "You are a Summarizer. Condense the text into ONE clear sentence."
    return {"summary": _ask(system, state["text"])}


def translator(state: State) -> dict:
    system = "You are a Translator. Translate the given sentence into Hindi. Return only the translation."
    return {"translation": _ask(system, state["summary"])}


def build_line():
    g = StateGraph(State)
    g.add_node("summarizer", summarizer)
    g.add_node("translator", translator)
    g.add_edge(START, "summarizer")
    g.add_edge("summarizer", "translator")   # summary flows to the translator
    g.add_edge("translator", END)
    return g.compile()


if __name__ == "__main__":
    text = (
        "LangGraph lets you build AI agents as graphs of nodes and edges. Each node "
        "does one job on a shared state. You can add branches, loops, and memory, "
        "which plain chains cannot do. It is the engine most agent frameworks run on."
    )
    result = build_line().invoke({"text": text, "summary": "", "translation": ""})
    print("SUMMARY:", result["summary"])
    print("HINDI:  ", result["translation"])
