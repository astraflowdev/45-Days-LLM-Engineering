"""
Exercise 2 (solution): a supervisor that routes to the right specialist

    START -> [supervisor] --(conditional)--> [math | code | writing] -> END

The supervisor reads the request and picks ONE specialist. This is the routing core
of the supervisor pattern (Module 03), single-shot: decide, route, answer, done.

Run it (needs GROQ_API_KEY in a .env file in this folder):
    python route_to_specialist_solution.py
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
    system = (
        "You are a Supervisor. Route the request to ONE specialist: 'math' (calculations, "
        "numbers), 'code' (programming, debugging), or 'writing' (essays, emails, text). "
        "Reply with ONLY that one word."
    )
    choice = _ask(system, state["request"]).lower()
    choice = next((s for s in SPECIALISTS if s in choice), "writing")
    print(f"[supervisor] -> {choice}")
    return {"next": choice}


def _specialist(name: str, persona: str):
    def run(state: State) -> dict:
        return {"answer": _ask(persona, state["request"]), "handled_by": name}
    return run


math = _specialist("math", "You are a Math tutor. Solve it and show the key step. Be brief.")
code = _specialist("code", "You are a Coding assistant. Give a short, correct answer with a tiny snippet if useful.")
writing = _specialist("writing", "You are a Writing assistant. Help clearly and concisely.")


def route(state: State) -> str:
    return state["next"]


def build_desk():
    g = StateGraph(State)
    g.add_node("supervisor", supervisor)
    g.add_node("math", math)
    g.add_node("code", code)
    g.add_node("writing", writing)
    g.add_edge(START, "supervisor")
    g.add_conditional_edges("supervisor", route, SPECIALISTS)
    for s in SPECIALISTS:
        g.add_edge(s, END)   # single-shot: answer, then done
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
