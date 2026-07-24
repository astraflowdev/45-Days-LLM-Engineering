# Day 26 — LangGraph Multi-Agent Patterns

**Phase 3 · Agents & Tools — Day 6.** Day 24 gave you the **LangGraph engine**
(nodes, edges, branches, loops, memory). Day 25 put **one** ReAct agent on it in a
single line. **Today: when one agent isn't enough**, you wire *several* agents into a
team — and you build the three classic shapes **by hand**, so they're never magic.

> **What you learn:** the one idea that makes multi-agent easy (*an agent is a node,
> a team is a graph*), and the three team shapes — **sequential** (assembly line),
> **supervisor / hierarchical** (a boss routes work), and **parallel** (fan-out /
> fan-in) — plus how to give a team **memory**. All on free **Groq**, **LangGraph 1.x**.

## The big idea
> **An agent is just a node. A team of agents is just a graph.**

No new engine. A multi-agent system is the same `StateGraph` from Day 24 with more
workers wired in. That's why today is a *practice* day: you already know the parts.

## The three shapes
| Shape | Picture | Use it when | Module |
|-------|---------|-------------|--------|
| **Sequential** | `A → B → C` | the steps are fixed; each needs the previous one's output | [02](02-sequential-agents/README.md) |
| **Supervisor** | a boss over workers (with a loop-back) | the right worker/order **depends on the input** | [03](03-supervisor-hierarchical/README.md) |
| **Parallel** | fan-out → fan-in | several **independent** opinions on one input, fast | [04](04-parallel-agents/README.md) |

## Learning objectives
By the end of today you can:
- Explain why *"an agent is a node, a team is a graph"* and pick the right shape.
- Build a **sequential** crew where state carries the hand-off.
- Build a **supervisor** that routes with `add_conditional_edges` + a back-edge.
- Build **parallel** agents with fan-out/fan-in and merge results with a **reducer**.
- Give a team **memory** with `MemorySaver` + `thread_id`.

## What this reuses
| From | Idea used here |
|------|----------------|
| Day 24 | `StateGraph`, `add_conditional_edges`, reducers (`Annotated[list, add]`), `MemorySaver`, `MessagesState` |
| Day 25 | agents as graph nodes (an agent is a worker on the graph) |
| Day 21 | `ChatGroq`, message objects, system prompts as "roles" |
| Day 19 | Streamlit chat UI (`session_state`, `st.stop()` key guard) |

## Start here
1. **Slides:** open [`presentation/index.html`](presentation/index.html) — *One agent,
   then a team* (speaker notes in [`presentation/README.md`](presentation/README.md)).
2. **Concepts:** run the modules `01 → 05` below.
3. **Build:** the [`mini-project/`](mini-project/README.md) — **SoftDesk Content
   Crew**, one example scaled through all three shapes in 6 steps.

## Module index
| # | Folder | You learn |
|---|--------|-----------|
| 01 | [`01-why-multi-agent/`](01-why-multi-agent/README.md) | An agent is a node; a team is a graph; the 3 shapes (no LLM, no key) |
| 02 | [`02-sequential-agents/`](02-sequential-agents/README.md) | Assembly line: researcher → writer → editor; state carries the hand-off |
| 03 | [`03-supervisor-hierarchical/`](03-supervisor-hierarchical/README.md) | A supervisor routes to workers via conditional edges + a back-edge |
| 04 | [`04-parallel-agents/`](04-parallel-agents/README.md) | Fan-out / fan-in; merge concurrent results with a **reducer** |
| 05 | [`05-agents-with-memory/`](05-agents-with-memory/README.md) | Team memory: `MemorySaver` + `thread_id` |

### Mini-project (today's build)
| Folder | Build |
|--------|-------|
| [`mini-project/`](mini-project/README.md) | **SoftDesk Content Crew** — 6 steps: single writer → sequential → +editor → supervisor → parallel review → finished crew + memory + a Streamlit UI |

### Exercises
| Folder | Practise |
|--------|----------|
| [`exercises/`](exercises/README.md) | Summarize→Translate (sequential) · Route-to-specialist (supervisor) |

## How to run

**Setup (once).** Nothing new to install — today reuses Days 24–25:
```bash
pip install langgraph langchain langchain-groq streamlit python-dotenv
```
The LLM modules make **direct Groq calls**, so they need a free `GROQ_API_KEY` in a
`.env` file (in the folder you're running from):
```
GROQ_API_KEY=your_key_here
```
Get one at [console.groq.com/keys](https://console.groq.com/keys).

**Run the modules in order:**
```bash
python 01-why-multi-agent/why_multi_agent.py     # runs with NO key (pure Python)
python 02-sequential-agents/sequential_agents.py
python 03-supervisor-hierarchical/supervisor.py
python 04-parallel-agents/parallel_agents.py
python 05-agents-with-memory/agents_with_memory.py
```
> **Note:** Module 01 is pure Python (no key). Modules 02–05 and the mini-project
> call Groq directly and require a `GROQ_API_KEY`.

## Today's exercise
Do both in [`exercises/`](exercises/README.md):
1. **Summarize → Translate** — a sequential 2-agent line.
2. **Route to a specialist** — a supervisor that routes with conditional edges.

## The big idea (recap)
> One agent is one node. A **team** is a **graph** of agents in one of three shapes —
> a line, a boss, or a fan-out. You built each by hand on the Day 24 engine, so when
> a framework hands you a "crew," you'll know exactly what's inside it.

➡ Next: **Day 27 — CrewAI** — a framework that packages these role-based crews for
you; you'll recognise every pattern under the hood.
