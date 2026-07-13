"""
06 - A chatbot that REMEMBERS: MessagesState + a checkpointer + thread_id.

Everything comes together here:
    - MessagesState (module 05) so the `messages` list grows automatically.
    - A checkpointer (MemorySaver) so that list SURVIVES between .invoke() calls.
    - A thread_id so each conversation has its own saved history.

On Day 16 we kept memory by hand (append to a list, pass it back every turn).
LangGraph does that for us: compile with a checkpointer, pass a thread_id, and
each turn you send ONLY the new message -- the graph reloads the rest.

This is the one module that calls Groq. Without a key it prints a clear skip
message and still shows the memory mechanics with a fake model, so you can see
the thread grow either way.

Setup:
    pip install langgraph langchain-groq python-dotenv
    echo GROQ_API_KEY=your_key > .env
Run:
    python chatbot_memory.py
"""

import os
from dotenv import load_dotenv

from langgraph.graph import StateGraph, START, END, MessagesState
from langgraph.checkpoint.memory import MemorySaver

load_dotenv()
MODEL = "llama-3.1-8b-instant"


# --- 1. Get a "model": real Groq if we have a key, else a tiny stand-in ---
# The stand-in lets the memory mechanics run offline. Both expose .invoke(messages).
if os.getenv("GROQ_API_KEY"):
    from langchain_groq import ChatGroq
    model = ChatGroq(model=MODEL, temperature=0)
    print(f"Using real Groq model: {MODEL}\n")
else:
    from langchain_core.messages import AIMessage
    class FakeModel:
        """Echoes how many messages it has seen -- proof the history is growing."""
        def invoke(self, messages):
            human = [m for m in messages if m.type == "human"]
            return AIMessage(content=f"(offline) I now see {len(human)} of your messages. "
                                     f"Latest: {human[-1].content!r}")
    model = FakeModel()
    print("No GROQ_API_KEY -- using an offline stand-in so you can still see memory work.\n")


# --- 2. The one node: call the model on the WHOLE history -----------------
# state["messages"] already holds the full conversation (the checkpointer
# reloaded it). We return the reply; add_messages appends it for us.
def chat(state: MessagesState) -> dict:
    reply = model.invoke(state["messages"])
    return {"messages": [reply]}


# --- 3. Build the graph and compile WITH a checkpointer -------------------
builder = StateGraph(MessagesState)
builder.add_node("chat", chat)
builder.add_edge(START, "chat")
builder.add_edge("chat", END)

# The checkpointer is what makes memory persist between .invoke() calls.
# MemorySaver keeps it in RAM; swap for a SQLite/Postgres saver in production.
memory = MemorySaver()
graph = builder.compile(checkpointer=memory)


# --- 4. Talk to it across turns, all on ONE thread_id ---------------------
# The thread_id names this conversation. Reuse it and history is remembered;
# change it and you start a fresh, separate conversation.
config = {"configurable": {"thread_id": "student-1"}}

def say(text: str) -> None:
    # Send ONLY the new message. The graph reloads the rest from the checkpoint.
    result = graph.invoke({"messages": [("human", text)]}, config)
    print(f"You : {text}")
    print(f"Bot : {result['messages'][-1].content}\n")

say("Hi! My name is Aditi and I love cricket.")
say("What is my name?")               # remembers -> "Aditi" (with a real key)
say("Name one sport I like.")         # remembers -> "cricket"

# Peek at what's stored: the full thread, reloaded from the checkpointer.
saved = graph.get_state(config).values["messages"]
print(f"Stored on thread 'student-1': {len(saved)} messages (all turns, both sides).")

# --- 5. A different thread_id = a clean slate -----------------------------
other = {"configurable": {"thread_id": "student-2"}}
fresh = graph.invoke({"messages": [("human", "What is my name?")]}, other)
print("\nNew thread 'student-2' asks the same question with no history:")
print("Bot :", fresh["messages"][-1].content)
print("\nSame graph, two threads, two separate memories -- keyed by thread_id.")
