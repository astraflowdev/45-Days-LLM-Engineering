# 02 · State & Nodes

One idea, and it's the whole framework:

> A **node is a function**. It gets the whole **state** and returns **only the keys it changed**.
> LangGraph merges that partial update back into the state before the next node runs.

## State is a form passed desk to desk

Picture a paper form moving from desk to desk in an office. Each desk (node) fills in *its* boxes and
passes the same form on. By the end, the form holds everyone's work.

```python
class State(TypedDict):
    raw: str          # the input
    cleaned: str      # filled by clean()
    word_count: int   # filled by count_words()
    shape: str        # filled by summarize_shape()
```

List **every field any node reads or writes** — that's your state schema.

## A node returns only what it changed

```python
def count_words(state):
    n = len(state["cleaned"].split())
    return {"word_count": n}      # <- just this key, not the whole state
```

`count_words` reads `cleaned` — which the **previous** node wrote — and returns only `word_count`.
It does **not** copy `raw` or `cleaned` forward; LangGraph keeps them. This is why nodes stay small
and independent: each one minds its own key.

## Wiring a linear pipeline

```python
builder = StateGraph(State)
builder.add_node("clean", clean)
builder.add_node("count_words", count_words)
builder.add_node("summarize_shape", summarize_shape)

builder.add_edge(START, "clean")
builder.add_edge("clean", "count_words")
builder.add_edge("count_words", "summarize_shape")
builder.add_edge("summarize_shape", END)

graph = builder.compile()
graph.invoke({"raw": "  some   text  "})
```

The edges spell out the path: `START → clean → count_words → summarize_shape → END`. Each node runs
once, in that order, and the state grows as it goes.

## How state updates merge (important)

| Node returns | What happens to the state |
|--------------|---------------------------|
| `{"cleaned": "hi"}` | `state["cleaned"]` is **set/replaced** with `"hi"` |
| `{}` (empty dict) | nothing changes — a valid "I only read" node |
| a key not in the schema | error — keys must exist in the `TypedDict` |

By default an update **replaces** the old value of that key. That's fine for `str`/`int`. But what if
two nodes both want to *add to a list* (like a chat history)? Replacing would throw away the first
one's work. That's exactly what **reducers** fix — see module 05.

## Run it

```bash
python state_and_nodes.py
```
You'll see each node announce its work, then the final state with every key filled in. No key needed.

➡ Next: [03 · Conditional Edges](../03-conditional-edges/README.md) — let the graph *choose* the next node.
