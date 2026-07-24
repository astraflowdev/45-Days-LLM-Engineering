"""
Day 26 - Module 05: Giving the team memory

A crew that forgets everything between turns isn't much of a team. The fix is the
SAME one you learned on Day 24 for a single graph:

    compile(checkpointer=MemorySaver())   +   a thread_id per conversation

Nothing about "it's a multi-agent graph" changes this. The checkpointer saves the
whole state (here: the running message history) after every turn, keyed by
thread_id. Send only the NEW message; the team still "remembers" the earlier ones.

We reuse the supervisor shape from Module 03 -- a boss routes each turn to a
specialist -- and make the whole conversation persistent.

Run it (needs a free GROQ_API_KEY in a .env file next to this script):
    python agents_with_memory.py
"""

from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, START, END
from langgraph.graph import MessagesState          # state with a `messages` list + add_messages
from langgraph.checkpoint.memory import MemorySaver

load_dotenv()
llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0)

WORKERS = ["billing", "tech", "general"]
PERSONAS = {
    "billing": "You are a Billing specialist. Use the conversation so far. Answer in 1-2 sentences.",
    "tech": "You are a Technical Support specialist. Use the conversation so far. Answer in 1-2 sentences.",
    "general": "You are a friendly general support agent. Use the conversation so far. Answer in 1-2 sentences.",
}


# MessagesState already gives us `messages: Annotated[list, add_messages]`.
# We add `next` so the supervisor can record its routing choice.
class State(MessagesState):
    next: str


def supervisor(state: State) -> dict:
    """Route the LATEST human turn to a specialist."""
    last = state["messages"][-1].content
    system = (
        "You are a support Supervisor. Route this message to one team: 'billing', "
        "'tech', or 'general'. Reply with ONLY that one word."
    )
    choice = llm.invoke([SystemMessage(content=system), HumanMessage(content=last)]).content.lower()
    choice = next((w for w in WORKERS if w in choice), "general")
    print(f"   [supervisor -> {choice}]")
    return {"next": choice}


def _worker(name: str):
    def run(state: State) -> dict:
        # The worker sees the FULL history (all prior turns) -> that's the memory.
        messages = [SystemMessage(content=PERSONAS[name])] + state["messages"]
        reply = llm.invoke(messages)
        return {"messages": [reply]}   # add_messages appends this to the running history
    return run


def route(state: State) -> str:
    return state["next"]


def build_team():
    g = StateGraph(State)
    g.add_node("supervisor", supervisor)
    for w in WORKERS:
        g.add_node(w, _worker(w))
    g.add_edge(START, "supervisor")
    g.add_conditional_edges("supervisor", route, WORKERS)
    for w in WORKERS:
        g.add_edge(w, END)
    # THE MEMORY: a checkpointer saves state per thread_id after every invoke.
    return g.compile(checkpointer=MemorySaver())


def say(team, thread_id: str, text: str) -> None:
    print(f"\nYOU ({thread_id}): {text}")
    config = {"configurable": {"thread_id": thread_id}}
    result = team.invoke({"messages": [HumanMessage(content=text)]}, config)
    print("TEAM:", result["messages"][-1].content.strip())


def main() -> None:
    print("=" * 66)
    print("A support team that remembers -- MemorySaver + thread_id")
    print("=" * 66)

    team = build_team()

    # Conversation A: two turns on the SAME thread -> the team remembers turn 1.
    say(team, "customer-A", "I was double-charged on order 5567, I want a refund.")
    say(team, "customer-A", "By the way, what was the order number I just mentioned?")

    # Conversation B: a DIFFERENT thread -> it knows nothing about order 5567.
    say(team, "customer-B", "What was the order number I mentioned?")

    print(
        "\nNotice: on thread 'customer-A' the team recalled order 5567 from the\n"
        "earlier turn. On 'customer-B' -- a separate thread_id -- it had no idea.\n"
        "Same memory mechanic as Day 24, now wrapping a whole agent team."
    )


if __name__ == "__main__":
    main()
