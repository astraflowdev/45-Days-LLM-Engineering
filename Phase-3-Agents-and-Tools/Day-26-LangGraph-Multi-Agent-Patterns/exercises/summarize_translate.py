"""
Exercise 1 (stub): a sequential 2-agent line -- summarizer -> translator

Build a two-agent assembly line:
    START -> [summarizer] -> [translator] -> END
The summarizer condenses a long text to one sentence; the translator turns that
sentence into Hindi. Fill in the TODOs, then run:

    python summarize_translate.py     # needs GROQ_API_KEY in a .env file here

PLAN FIRST (rule 1): before you write code, sketch the state keys and which agent
reads/writes each. Only then start typing.
"""

from typing import TypedDict

from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, START, END

load_dotenv()
llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0)


class State(TypedDict):
    text: str
    summary: str
    translation: str


def _ask(system: str, user: str) -> str:
    return llm.invoke([SystemMessage(content=system), HumanMessage(content=user)]).content.strip()


def summarizer(state: State) -> dict:
    # TODO: give the model a "Summarizer" system prompt; summarize state["text"]
    # into one sentence. Return {"summary": ...}.
    ...


def translator(state: State) -> dict:
    # TODO: give the model a "Translator" system prompt; translate state["summary"]
    # into Hindi. Return {"translation": ...}.
    ...


def build_line():
    g = StateGraph(State)
    # TODO: add both nodes and wire START -> summarizer -> translator -> END
    ...
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
