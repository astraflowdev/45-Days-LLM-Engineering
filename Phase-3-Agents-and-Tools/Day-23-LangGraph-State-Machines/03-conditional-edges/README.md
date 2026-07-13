# 03 · Conditional Edges (Branching)

A normal edge is **fixed**:

```python
add_edge("a", "b")      # always a → b
```

A **conditional edge** runs a little **router** function that looks at the state and **returns the
name of the next node**. This is the branching a `|` chain can never do.

```python
add_conditional_edges("classify", route, {"billing": "billing", "technical": "technical"})
#                      ^source      ^router  ^map: router's return value → node name
```

## The pattern: classify → route → handle

Three moving parts, and it's worth keeping them separate:

| Part | Job | Changes state? |
|------|-----|----------------|
| **node** (`classify`) | inspect the input, record a `category` | ✅ yes |
| **router** (`route`) | read state, **return a string** (a routing key) | ❌ no |
| **handler nodes** (`billing`…) | do the branch-specific work | ✅ yes |

The node decides *what* the data is; the router decides *where to go*. Splitting them keeps each
piece small and reusable.

```python
def route(state):
    return state["category"]        # "billing" | "technical" | "general"

builder.add_conditional_edges(
    "classify",
    route,
    {
        "billing":   "billing",     # route() returns "billing" → billing node
        "technical": "technical",
        "general":   "general",
    },
)
```

The dict maps **the router's return value → a node name**. Return `"billing"`, and LangGraph runs the
`billing` node next.

## One graph, many paths

```
                 ┌──▶ billing ──┐
START ▶ classify ─┼──▶ technical ┼──▶ END
                 └──▶ general ──┘
```

The **same compiled graph** takes a *refund* message down the billing path and a *crash* message
down the technical path — the route is chosen **at runtime from the data**.

## Gotchas
- The router **returns a routing key, not a node** by default — you map keys → nodes in the dict. (You
  *can* return a node name directly and skip the dict, but the explicit map reads better.)
- Every value the router can return **must be in the map**, or you'll hit a "no matching edge" error.
- Don't mutate state inside the router — do that in a node. Routers only *decide*.
- A router can also return the special `END` to stop — handy for "if done, exit" branches (module 04).

## Why this matters

Branching is the first thing that turns a pipeline into something *smart*: the app now responds
differently to different inputs. Add the ability to **loop back** (next module) and you have the two
control-flow moves every agent is built from.

## Run it

```bash
python conditional_edges.py
```
Rule-based classification, so it runs with no key — the lesson is the graph shape. A real app would
swap `classify` for a Groq call.

➡ Next: [04 · Cycles & Loops](../04-cycles-and-loops/README.md) — a node that runs again and again until done.
