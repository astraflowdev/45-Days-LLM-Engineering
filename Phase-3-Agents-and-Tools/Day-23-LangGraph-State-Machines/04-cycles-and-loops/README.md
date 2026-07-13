# 04 · Cycles & Loops

This is the module that justifies the whole framework. A `|` chain goes **forward only**. A graph
edge can point **backward** — a node can lead to itself — so the graph **loops until a condition says
stop**.

> generate → check → *(not good enough? go back)* → generate → check → … → done

That loop is the skeleton of **every agent**: try something, look at the result, decide whether to try
again.

## A loop is just a conditional edge that points back

You already have the tool — it's the conditional edge from module 03. The trick is that one of its
targets is **the node itself**:

```python
builder.add_conditional_edges(
    "draft",
    keep_going,
    {
        "loop": "draft",   # ← back to the same node = a cycle
        "done": END,
    },
)
```

The router decides each time around:

```python
def keep_going(state):
    if state["ok"]:
        return "done"                     # rules passed → exit
    if state["attempts"] >= MAX_ATTEMPTS:
        return "done"                     # safety cap → exit
    return "loop"                         # otherwise → run draft() again
```

## The shape

```
START ▶ draft ──(keep_going?)──▶ END
          ▲                │
          └──── "loop" ────┘
```

Each pass, `draft` writes a new `candidate` and whether it's `ok`; `keep_going` reads that and either
sends us around again or out to `END`.

## Always give a loop a way out

An infinite loop is a real risk here. Two seatbelts, use **both**:

| Guard | What it does |
|-------|--------------|
| **Your own counter** (`attempts >= MAX_ATTEMPTS`) | the *intended* exit — you control the cap and can log it |
| **`recursion_limit`** (LangGraph built-in) | a backstop — the graph raises `GraphRecursionError` after N steps (default 25) so a bug can't hang forever |

You can raise the built-in limit when a loop legitimately needs more steps:
```python
graph.invoke(state, {"recursion_limit": 50})
```
But prefer a real exit condition in your router — the recursion limit is a crash guard, not a plan.

## Why a chain can't do this

`prompt | model | parser` has no way to say "run `model` again." Its structure is a straight pipe.
The moment your app needs *retry*, *refine*, or *"keep calling tools until you have the answer"*, you
need a graph. That last one **is** an agent — and it's exactly Day 25.

## Run it

```bash
python cycles_and_loops.py
```
It drafts passwords, strengthening the attempt each pass, and stops the moment one passes all three
rules. No key needed — the loop *mechanics* are the lesson.

➡ Next: [05 · Reducers & Messages](../05-reducers-and-messages/README.md) — make state **accumulate**
so a loop (or a chat) can build up history instead of overwriting it.
