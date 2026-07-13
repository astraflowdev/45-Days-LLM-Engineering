# 01 · Why LangGraph?

Yesterday's chain was a **straight line**:

```python
chain = prompt | model | parser      # data flows left → right, once
```

That's perfect for *one question → one answer*. But it can never:
- **loop** — "if the model's JSON is broken, try again";
- **branch** — "send refund questions to one step, complaints to another";
- **remember** where it is across calls.

The `|` operator just doesn't have a way to say "go back" or "choose". **LangGraph** does, because
you describe your app as a **graph**, not a line.

## The four pieces (you'll use these all day)

| Piece | What it is | In code |
|-------|-----------|---------|
| **State** | one shared dict that flows through the graph | a `TypedDict` |
| **Node** | a step — *just a function* `state → {changes}` | `def shout(state): ...` |
| **Edge** | a wire: "after this node, run that one" | `add_edge(a, b)` |
| **START / END** | the graph's entry and exit points | `from langgraph.graph import START, END` |

## The smallest possible graph

```python
from typing import TypedDict
from langgraph.graph import StateGraph, START, END

class State(TypedDict):
    text: str

def shout(state):
    return {"text": state["text"].upper() + "!"}

builder = StateGraph(State)
builder.add_node("shout", shout)
builder.add_edge(START, "shout")
builder.add_edge("shout", END)

graph = builder.compile()
graph.invoke({"text": "hello"})     # -> {'text': 'HELLO!'}
```

Read it top to bottom:
1. **Describe the state** (`text`).
2. **Write a node** — a function that returns the keys it changed.
3. **Wire edges**: `START → shout → END`.
4. **`.compile()`** into a runnable, then **`.invoke()`** with the starting state.

Notice the node returns `{"text": ...}` — *only the key it touched*, not the whole state. LangGraph
merges that back in for you. (Module 02 leans on this; module 05 shows how to make it *append*.)

## Chain vs graph, at a glance

| | LCEL chain | LangGraph |
|---|-----------|-----------|
| Shape | a line: A → B → C | a graph: nodes + edges |
| Runs each step… | once, in order | as many times as the edges say |
| Can branch? | ❌ | ✅ (module 03) |
| Can loop? | ❌ | ✅ (module 04) |
| Runnable with `.invoke()`? | ✅ | ✅ |

A chain is really just a graph with no choices. Today we add the choices.

## Run it

```bash
python why_langgraph.py
```
No API key needed — the graph engine is pure Python. (Only module 06 calls a model.)

➡ Next: [02 · State & Nodes](../02-state-and-nodes/README.md) — how state flows through several nodes.
