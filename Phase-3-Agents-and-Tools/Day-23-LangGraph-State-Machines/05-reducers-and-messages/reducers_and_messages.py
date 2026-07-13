"""
05 - Reducers: make state ADD UP instead of overwrite.

By default, when a node returns {"key": value}, that value REPLACES the old
one. Fine for a str or int. But for a LIST you're building up (a chat history,
a log of steps), replacing throws away everything so far.

A REDUCER changes how updates merge. You attach it to a field with Annotated:

    from operator import add
    log: Annotated[list, add]          # updates get concatenated, not replaced

For chat messages, LangGraph ships a smarter reducer, add_messages, that also
turns ("human", "hi") tuples into proper Message objects and handles updates by
id. State whose messages field uses it is so common there's a prebuilt
MessagesState you can subclass.

This whole file is offline -- it's about how state merges, no model call.

Setup:
    pip install langgraph langchain-core
Run:
    python reducers_and_messages.py
"""

from typing import TypedDict, Annotated
from operator import add
from langgraph.graph import StateGraph, START, END, MessagesState
from langgraph.graph.message import add_messages


# =========================================================================
# PART A - Without a reducer: updates OVERWRITE (usually not what you want)
# =========================================================================
class NoReducer(TypedDict):
    log: list

def step_a(state): return {"log": ["a ran"]}
def step_b(state): return {"log": ["b ran"]}   # replaces a's list entirely!

b1 = StateGraph(NoReducer)
b1.add_node("step_a", step_a); b1.add_node("step_b", step_b)
b1.add_edge(START, "step_a"); b1.add_edge("step_a", "step_b"); b1.add_edge("step_b", END)
print("PART A (no reducer): log =", b1.compile().invoke({"log": []})["log"])
print("  -> b's update REPLACED a's. History lost.\n")


# =========================================================================
# PART B - With a reducer: updates ACCUMULATE
# =========================================================================
class WithReducer(TypedDict):
    # Annotated[<type>, <reducer>]: the reducer decides how a new update
    # combines with the current value. `add` on two lists = concatenation.
    log: Annotated[list, add]

# same nodes, same wiring -- only the state annotation changed
b2 = StateGraph(WithReducer)
b2.add_node("step_a", step_a); b2.add_node("step_b", step_b)
b2.add_edge(START, "step_a"); b2.add_edge("step_a", "step_b"); b2.add_edge("step_b", END)
print("PART B (Annotated[list, add]): log =", b2.compile().invoke({"log": []})["log"])
print("  -> both kept. The reducer appended instead of replacing.\n")


# =========================================================================
# PART C - add_messages: the reducer built for chat history
# =========================================================================
class ChatState(TypedDict):
    messages: Annotated[list, add_messages]

def user_turn(state): return {"messages": [("human", "What's the capital of France?")]}
def bot_turn(state):  return {"messages": [("ai", "Paris.")]}

b3 = StateGraph(ChatState)
b3.add_node("user_turn", user_turn); b3.add_node("bot_turn", bot_turn)
b3.add_edge(START, "user_turn"); b3.add_edge("user_turn", "bot_turn"); b3.add_edge("bot_turn", END)
msgs = b3.compile().invoke({"messages": []})["messages"]
print("PART C (add_messages): history grew to", len(msgs), "messages")
for m in msgs:
    # add_messages upgraded our ("human", "...") tuples into Message objects
    print(f"  {type(m).__name__:10} {m.content}")
print()


# =========================================================================
# PART D - MessagesState: the same thing, prewritten for you
# =========================================================================
# This tiny class...
#     class ChatState(TypedDict):
#         messages: Annotated[list, add_messages]
# ...is needed so often that LangGraph ships it as MessagesState. Subclass it
# to add your own fields; you inherit the messages field + its reducer.
class AgentState(MessagesState):
    step_count: int          # your extra field alongside the built-in messages

print("PART D: MessagesState already has:", list(MessagesState.__annotations__))
print("  Subclass it (as AgentState) to get add_messages for free -- we'll use")
print("  exactly this in module 06 to build a chatbot that remembers.")
