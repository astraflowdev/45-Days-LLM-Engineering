# 05 · Giving the team memory

A crew that forgets everything between turns isn't much of a team. The fix is the
**same one from Day 24** — nothing about "multi-agent" changes it:

```python
team = g.compile(checkpointer=MemorySaver())     # save state after every turn
config = {"configurable": {"thread_id": "customer-A"}}
team.invoke({"messages": [HumanMessage(content="...")]}, config)
```

## How it works
- The **checkpointer** saves the whole graph state after each `.invoke()`, keyed by
  **`thread_id`**.
- Next turn, you send **only the new message**; LangGraph reloads the saved state, so
  the team still "remembers" the earlier turns.
- Different `thread_id` = a **separate, isolated** conversation.

We reuse Module 03's **supervisor** shape (a boss routes each turn to a specialist)
and make the whole conversation persistent using `MessagesState`.

## `MessagesState` does the accumulation for you
```python
from langgraph.graph import MessagesState

class State(MessagesState):   # gives you messages: Annotated[list, add_messages]
    next: str                 # + our supervisor's routing decision
```
`MessagesState` already carries a `messages` list with the `add_messages` reducer
(Day 24), so each worker's reply is **appended** to the running history, not
overwritten. Every worker sees the **full history**:

```python
def worker(state):
    messages = [SystemMessage(content=persona)] + state["messages"]  # <- full history
    return {"messages": [llm.invoke(messages)]}
```

## What the demo shows
| Turn | Thread | Message | Result |
|------|--------|---------|--------|
| 1 | `customer-A` | "double-charged on order **5567**, refund?" | routed to billing |
| 2 | `customer-A` | "what was the order number I just mentioned?" | **recalls 5567** |
| 3 | `customer-B` | "what order number I mentioned?" | **no idea** (isolated thread) |

Same memory mechanic as Day 24 — now wrapping a whole agent **team**.

## Run it
```bash
python agents_with_memory.py     # needs GROQ_API_KEY in a .env file here
```

## Gotcha
Memory lives **per `thread_id`**, in RAM (`MemorySaver`). Restart the program and
it's gone. For a real app you'd use a persistent checkpointer (e.g. SQLite/Postgres),
but the API is identical — swap the checkpointer, keep everything else.

➡ Next: build it all — the [mini-project](../mini-project/README.md) (SoftDesk Content Crew).
