"""
Exercise 2 (stub): a supervisor that routes to the right specialist

Build a single-shot supervisor:
    START -> [supervisor] --(conditional)--> [math | code | writing] -> END
The supervisor reads the request and picks ONE specialist to answer it.

Fill in the TODOs, then run:
    python route_to_specialist.py     # needs GROQ_API_KEY in a .env file here

PLAN FIRST (rule 1): what does the supervisor WRITE into state, and how does the
router turn that into the next node's name? Sketch it before coding.
"""

from typing import TypedDict

from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, START, END

load_dotenv()
llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0)

SPECIALISTS = ["math", "code", "writing"]


class State(TypedDict):
    request: str
    next: str
    answer: str
    handled_by: str


def _ask(system: str, user: str) -> str:
    return llm.invoke([SystemMessage(content=system), HumanMessage(content=user)]).content.strip()


def supervisor(state: State) -> dict:
    # TODO: prompt the model to reply with ONE word: math / code / writing.
    # Sanitize the reply to a valid specialist, then return {"next": choice}.
    ...


def _specialist(name: str, persona: str):
    def run(state: State) -> dict:
        return {"answer": _ask(persona, state["request"]), "handled_by": name}
    return run


math = _specialist("math", "You are a Math tutor. Solve it and show the key step. Be brief.")
code = _specialist("code", "You are a Coding assistant. Give a short, correct answer.")
writing = _specialist("writing", "You are a Writing assistant. Help clearly and concisely.")


def route(state: State) -> str:
    # TODO: return the chosen specialist's node name (hint: it's in state["next"]).
    ...


def build_desk():
    g = StateGraph(State)
    g.add_node("supervisor", supervisor)
    for name, fn in [("math", math), ("code", code), ("writing", writing)]:
        g.add_node(name, fn)
    # TODO: START -> supervisor; conditional edges from supervisor via `route`;
    #       each specialist -> END.
    ...
    return g.compile()


if __name__ == "__main__":
    desk = build_desk()
    for request in [
        "What is 17 percent of 2500?",
        "Why does my Python list keep the same value across function calls?",
    ]:
        print("\nREQUEST:", request)
        result = desk.invoke({"request": request, "next": "", "answer": "", "handled_by": ""})
        print(f"[{result['handled_by']}]:", result["answer"])
