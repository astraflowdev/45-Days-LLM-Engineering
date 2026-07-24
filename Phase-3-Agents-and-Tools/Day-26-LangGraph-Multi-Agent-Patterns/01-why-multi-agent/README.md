# 01 · Why multi-agent? (and the three shapes)

You've spent two days on **one** agent: Day 24 gave you the LangGraph engine
(nodes, edges, loops, memory), Day 25 put a whole ReAct agent on it in one line.
Today's question: **what if one agent isn't enough?**

## The one idea that makes today easy
> **An agent is just a node. A team of agents is just a graph.**

That's it. You already know the engine. A "multi-agent system" is a `StateGraph`
(Day 24) with **more than one worker** wired in. Each agent is a node that reads the
shared **state**, does its one job, and returns only the keys it changed — exactly
like every node you've written.

`why_multi_agent.py` proves it with **no LLM and no key**: two plain-Python
"agents" (a `writer` and an `editor`) wired in a line.

```python
g = StateGraph(State)
g.add_node("writer", writer)   # agent 1 = a node
g.add_node("editor", editor)   # agent 2 = a node
g.add_edge(START, "writer")
g.add_edge("writer", "editor") # the hand-off
g.add_edge("editor", END)
```

## The three shapes of a team
Everything you build today is one of these (all just graphs):

| Shape | Picture | Idea | Module |
|-------|---------|------|--------|
| **Sequential** | `A → B → C` | An assembly line; each agent adds one piece, state carries the hand-off | [02](../02-sequential-agents/README.md) |
| **Supervisor** | a boss over workers | A supervisor **routes** each task to the right worker, who reports back | [03](../03-supervisor-hierarchical/README.md) |
| **Parallel** | fan-out / fan-in | Several agents work on the **same** input at once; a reducer merges results | [04](../04-parallel-agents/README.md) |

And [05](../05-agents-with-memory/README.md) gives any of them **memory** across turns.

## When to reach for which
- **Sequential** — the steps are known and fixed (research, then write, then edit).
- **Supervisor** — the right worker/order **depends on the input** (routing, judgement).
- **Parallel** — several **independent** opinions on one thing, and you want them fast.

Real systems **combine** them — you'll do exactly that in today's mini-project.

## Run it
```bash
python why_multi_agent.py
```
No key needed — it's pure Python, on purpose, so the *shape* is unmistakable.

## Gotcha (previewed here, fixed in 04)
The demo carries its `log` list forward **by hand** (`state["log"] + [...]`). A plain
list key in state **overwrites** — the last node wins. The proper fix for
accumulating lists is a **reducer**, which you'll meet in Module 04.

➡ Next: [02 · Sequential agents](../02-sequential-agents/README.md)
