# 06 · A Chatbot That Remembers

Everything from today lands here. On **Day 16** we kept conversation memory *by hand* — append each
turn to a `messages` list, pass the whole list back every time. LangGraph does that bookkeeping for
you with two ingredients:

| Ingredient | From | Job |
|-----------|------|-----|
| `MessagesState` + `add_messages` | module 05 | the `messages` list **grows** each turn |
| a **checkpointer** (`MemorySaver`) + `thread_id` | here | that list **survives between calls** |

Reducer = the list grows *within* a run. Checkpointer = the list is *remembered across* runs. Put
together, that's memory — automatic.

## The whole app

```python
from langgraph.graph import StateGraph, START, END, MessagesState
from langgraph.checkpoint.memory import MemorySaver
from langchain_groq import ChatGroq

model = ChatGroq(model="llama-3.1-8b-instant", temperature=0)

def chat(state):                       # state["messages"] = the full history
    return {"messages": [model.invoke(state["messages"])]}

builder = StateGraph(MessagesState)
builder.add_node("chat", chat)
builder.add_edge(START, "chat")
builder.add_edge("chat", END)

graph = builder.compile(checkpointer=MemorySaver())   # ← memory turned on
```

The node calls the model on the **whole** `messages` history and returns the reply. `add_messages`
appends both your message and the reply for you.

## Talking across turns

The `thread_id` names the conversation. Reuse it → history remembered. Change it → fresh start.

```python
config = {"configurable": {"thread_id": "student-1"}}

graph.invoke({"messages": [("human", "My name is Aditi.")]}, config)
graph.invoke({"messages": [("human", "What is my name?")]}, config)   # → "Aditi"
```

**Notice:** each turn you pass **only the new message**, not the whole history. The checkpointer
reloads the rest from `thread_id`. That's the payoff versus the Day-16 hand-rolled version, where you
had to carry the list yourself.

## Threads are separate memories

```python
graph.get_state(config).values["messages"]     # → the full saved thread
```

```
thread "student-1":  [Hi, I'm Aditi] [Hi Aditi!] [What's my name?] [Aditi]   ← remembers
thread "student-2":  [What's my name?] [I don't know your name]              ← clean slate
```

One compiled graph serves many users — each `thread_id` is an isolated conversation. That's how a real
chat app keeps a thousand users' histories apart.

## `MemorySaver` and beyond

| Checkpointer | Stores in | Use for |
|--------------|-----------|---------|
| `MemorySaver` | RAM (this process) | learning, tests, short-lived apps |
| `SqliteSaver` | a `.db` file | a local app that should survive restarts |
| `PostgresSaver` | Postgres | production, many users |

They're drop-in swaps — same `compile(checkpointer=...)` line. Start with `MemorySaver`.

## Run it

```bash
python chatbot_memory.py
```
**With** a `GROQ_API_KEY` in `.env`, it truly remembers your name and sport across turns. **Without**
a key, it uses an offline stand-in so you can still watch the thread grow and see two `thread_id`s stay
separate — the memory mechanics don't need a model.

## Where this goes next

A chatbot loops *you → model → you*. An **agent** loops *model → tool → model* until the model has the
answer — same graph machinery, but the model also gets **tools** it can call. That's the next two days:

➡ Next: **Day 24 — Tool use / function calling** (`@tool`, `bind_tools`), then **Day 25** wires tools
into a full ReAct agent graph.
