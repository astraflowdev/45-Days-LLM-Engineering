# 03 · Supervisor / hierarchical agents (the boss)

A sequential line is **fixed**: research, then write, then edit — always. But real
work needs judgement: *"Is this a billing question or a tech question? Who should
handle it?"* That decision is the **supervisor** pattern.

```
             +-------------+
    +------> | supervisor  | <------+     the supervisor READS the state and
    |        +------+------+        |     DECIDES which worker goes next; the
    v               |              v      worker does its bit and reports back;
 [billing]       [tech]       [general]   the supervisor decides again... FINISH.
```

## The mechanic (all from Day 24)
Two pieces you already know:

1. **`add_conditional_edges`** — from the supervisor, branch to different nodes
   based on a **router function**.
2. **A back-edge** — after *every* worker, edge **back to the supervisor**. That
   loop is what makes it a *hierarchy* (a boss in charge) instead of a straight line.

```python
g.add_edge(START, "supervisor")
g.add_conditional_edges("supervisor", route, ["billing", "tech", "general", END])
for w in WORKERS:
    g.add_edge(w, "supervisor")     # every worker reports back to the boss
```

The supervisor writes its decision into state; the router turns that into the next
node's name:

```python
def route(state):
    return END if state["next"] == "FINISH" else state["next"]
```

## The supervisor doesn't answer — it decides
That's the key mental shift. The supervisor node's job is **routing**, not doing the
work. Its system prompt says *"reply with ONLY one word: billing, tech, or general."*
We then **sanitize** that word (defend against the model adding extra text) before
routing.

| Node | Job |
|------|-----|
| `supervisor` | Pick the worker (or FINISH). Produces a decision, not an answer. |
| `billing` / `tech` / `general` | The specialists — each a role + a system prompt. |

## Why this beats a fixed line
The **order isn't hard-coded**. A refund question goes to billing; a crash goes to
tech — the *same graph* handles both. Add a new worker + one line in the supervisor's
prompt and the boss can route to it. No rewiring of the flow.

## Run it
```bash
python supervisor.py     # needs GROQ_API_KEY in a .env file here
```
It sends two very different requests through the same desk and shows each getting
routed to a different specialist.

## Gotcha — runaway loops
A supervisor + back-edges is a **loop**. If the supervisor never says FINISH, it
runs forever. Two guards: a clear "when is it done?" rule (here: once a worker has
answered), and LangGraph's `recursion_limit` (Day 24's safety belt) on `.invoke()`.

➡ Next: [04 · Parallel agents](../04-parallel-agents/README.md)
