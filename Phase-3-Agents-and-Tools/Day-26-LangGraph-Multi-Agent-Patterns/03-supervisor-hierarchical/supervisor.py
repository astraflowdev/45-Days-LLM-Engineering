"""
Day 26 - Module 03: Supervisor / hierarchical agents (the boss)

A sequential line is fixed: research, then write, then edit -- always in that order.
But what if the work needs judgement? "Is this a billing question or a tech
question? Who should handle it?" That's the SUPERVISOR pattern:

                 +-------------+
        +------> | supervisor  | <------+     the supervisor READS the state and
        |        +------+------+        |     DECIDES which worker goes next; the
        v               |              v      worker does its bit and reports back;
    [billing]        [tech]        [general]  the supervisor decides again... until
                                              it says FINISH.

The mechanic is Day 24's `add_conditional_edges`: the supervisor node writes a
"next" decision into state, and a router function sends the graph to that worker.
After every worker we route BACK to the supervisor -- that back-edge is what makes
it a hierarchy (a boss in the loop) instead of a straight line.

Run it (needs a free GROQ_API_KEY in a .env file next to this script):
    python supervisor.py
"""

from typing import TypedDict

from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, START, END

load_dotenv()
llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0)

WORKERS = ["billing", "tech", "general"]


# --- Shared state ------------------------------------------------------------
class State(TypedDict):
    request: str      # the customer's message (input)
    next: str         # the supervisor's routing decision
    answer: str       # the worker's reply
    handled_by: str   # which worker took it (for the trail)


def _ask(system: str, user: str) -> str:
    return llm.invoke([SystemMessage(content=system), HumanMessage(content=user)]).content.strip()


# --- The supervisor: it doesn't answer, it DECIDES ---------------------------
def supervisor(state: State) -> dict:
    """Look at the request and pick a worker (or FINISH if already answered)."""
    if state.get("answer"):
        # A worker has already replied -> the job is done.
        print("[supervisor] a worker has answered -> FINISH")
        return {"next": "FINISH"}

    system = (
        "You are a support Supervisor. Route the customer's request to exactly one "
        "team: 'billing' (payments, refunds, invoices), 'tech' (errors, bugs, login "
        "problems), or 'general' (anything else). Reply with ONLY that one word."
    )
    choice = _ask(system, state["request"]).lower()
    # Be defensive: keep only a valid worker name.
    choice = next((w for w in WORKERS if w in choice), "general")
    print(f"[supervisor] routing to -> {choice}")
    return {"next": choice}


# --- The workers: each is a specialist with its own system prompt ------------
def _worker(name: str, persona: str):
    def run(state: State) -> dict:
        answer = _ask(persona, state["request"])
        print(f"\n[{name}] answered:\n{answer}")
        return {"answer": answer, "handled_by": name}
    return run


billing = _worker("billing", "You are a Billing specialist. Answer payment/refund questions in 2-3 sentences.")
tech = _worker("tech", "You are a Technical Support specialist. Give a 2-3 sentence troubleshooting answer.")
general = _worker("general", "You are a friendly general support agent. Answer helpfully in 2-3 sentences.")


# --- The router: reads the supervisor's decision, moves the graph ------------
def route(state: State) -> str:
    """A conditional edge: turn the 'next' decision into the next node's name."""
    return END if state["next"] == "FINISH" else state["next"]


def build_desk():
    g = StateGraph(State)
    g.add_node("supervisor", supervisor)
    g.add_node("billing", billing)
    g.add_node("tech", tech)
    g.add_node("general", general)

    g.add_edge(START, "supervisor")
    # From the supervisor, branch to a worker OR to END, based on `route`.
    g.add_conditional_edges("supervisor", route, ["billing", "tech", "general", END])
    # After ANY worker, go BACK to the supervisor -- the boss is in the loop.
    for w in WORKERS:
        g.add_edge(w, "supervisor")
    return g.compile()


def main() -> None:
    print("=" * 66)
    print("Supervisor pattern: a boss routes each request to a specialist")
    print("=" * 66)

    desk = build_desk()
    for request in [
        "I was charged twice for my order, can I get a refund?",
        "The app crashes every time I try to log in.",
    ]:
        print("\n" + "-" * 66)
        print("CUSTOMER:", request)
        print("-" * 66)
        result = desk.invoke(
            {"request": request, "next": "", "answer": "", "handled_by": ""}
        )
        print(f"\n=> handled by the '{result['handled_by']}' team.")

    print(
        "\nWhy this beats a fixed line: the ORDER isn't hard-coded. The supervisor\n"
        "chose a different worker for each request. Add a new worker + one line in\n"
        "the prompt and the boss can route to it -- no rewiring of the whole flow."
    )


if __name__ == "__main__":
    main()
