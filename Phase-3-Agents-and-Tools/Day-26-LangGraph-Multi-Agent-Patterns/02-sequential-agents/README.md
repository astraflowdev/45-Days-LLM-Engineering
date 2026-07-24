# 02 · Sequential agents (the assembly line)

The simplest team shape: agents in a **straight line**, each doing one job and
handing its work to the next through the shared state.

```
START → [researcher] → [writer] → [editor] → END
```

## What makes each node an "agent"
One model, three roles. The role comes from the **system prompt**, not a different
model:

| Node | System prompt says | Reads | Writes |
|------|--------------------|-------|--------|
| `researcher` | "list 3 factual points" | `topic` | `research` |
| `writer` | "use ONLY these points, write a paragraph" | `research` | `draft` |
| `editor` | "polish this draft" | `draft` | `final` |

The **state** is the conveyor belt. The writer never sees the raw topic — it sees
the researcher's notes. Each agent trusts the previous one's output.

## The wiring is just a chain of edges
```python
g.add_edge(START, "researcher")
g.add_edge("researcher", "writer")   # research → writer
g.add_edge("writer", "editor")       # draft → editor
g.add_edge("editor", END)
```

## Sequential vs. one big prompt
Why not ask one model to "research, write, and edit" in a single call? Because
splitting the job:
- lets each step have a **focused** prompt (better output),
- makes each step **inspectable** (you can print the research, the draft, the final),
- lets you **swap or reorder** steps without touching the others.

That's the whole pitch for multi-agent: **specialists beat a generalist** on
complex work.

## Run it
```bash
python sequential_agents.py     # needs GROQ_API_KEY in a .env file here
```
It prints each agent's output so you can watch the hand-off, then the final blurb.

## Gotcha
A sequential line has a **fixed order**. If some requests need a different path
(skip research, or route to a different specialist), a line can't decide that — you
need a **supervisor**. That's next.

➡ Next: [03 · Supervisor / hierarchical agents](../03-supervisor-hierarchical/README.md)
