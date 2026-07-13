# 05 · Reducers & Messages

Back in module 02 we said an update **replaces** a key's value. That's fine for a `str` or `int` —
but wrong when you're **building up a list** (a chat history, a step log). Replacing throws away
everything so far.

A **reducer** changes *how* an update merges into the state.

## The problem, seen

Two nodes that each append to `log`, with a plain `list` field:

```python
def step_a(state): return {"log": ["a ran"]}
def step_b(state): return {"log": ["b ran"]}
# final log == ["b ran"]   ← a's work was overwritten!
```

## The fix: annotate the field with a reducer

```python
from typing import Annotated
from operator import add

class State(TypedDict):
    log: Annotated[list, add]     # merge updates with `add` (list + list)
```

Same nodes, same wiring — now:

```python
# final log == ["a ran", "b ran"]   ← both kept
```

`Annotated[<type>, <reducer>]` says: *this field is a `list`, and when a node returns a new value,
combine it with the current one using this function.* `add` on two lists concatenates them.

| Field declaration | A node returns `{"x": [2]}` when `x == [1]` | Result |
|-------------------|---------------------------------------------|--------|
| `x: list` | replace | `[2]` |
| `x: Annotated[list, add]` | reduce (concatenate) | `[1, 2]` |

## `add_messages`: the reducer built for chat

For conversations, LangGraph ships a smarter reducer, `add_messages`, that does two extra things a
plain `add` doesn't:

```python
from langgraph.graph.message import add_messages

class ChatState(TypedDict):
    messages: Annotated[list, add_messages]
```

- **Appends** new messages to the history (like `add`), **and**
- **Upgrades** loose tuples like `("human", "hi")` into proper `HumanMessage` / `AIMessage` objects,
- **Updates by id** — a message with an existing id replaces that one instead of duplicating (matters
  once tools stream partial messages; Day 24–25).

## `MessagesState`: the same thing, prewritten

That exact `{messages: Annotated[list, add_messages]}` shape is so common LangGraph ships it as
**`MessagesState`**. Subclass it and you inherit the `messages` field *and* its reducer for free:

```python
from langgraph.graph import MessagesState

class AgentState(MessagesState):
    step_count: int        # your own fields alongside the built-in `messages`
```

We'll build **exactly this** in the next module: a chatbot whose `messages` list grows automatically
each turn, then persists across calls with a checkpointer.

## Why this is the bridge to memory

A reducer makes state **accumulate within one run**. A **checkpointer** (module 06) makes that
accumulated state **survive between runs**, keyed by a `thread_id`. Reducer = the list grows;
checkpointer = the list is remembered. Together they are conversation memory — the thing we hand-rolled
on Day 16, now automatic.

## Run it

```bash
python reducers_and_messages.py
```
Four parts, all offline: no reducer (overwrite) → `add` reducer (accumulate) → `add_messages` →
`MessagesState`.

➡ Next: [06 · Chatbot With Memory](../06-chatbot-with-memory/README.md) — put it together with real Groq.
