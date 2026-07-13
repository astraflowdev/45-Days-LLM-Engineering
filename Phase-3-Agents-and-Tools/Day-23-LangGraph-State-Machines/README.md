# Day 23 — LangGraph: State Machines for AI

**Phase 3 · Agents & Tools — Day 3.** Days 21–22 gave us LangChain and put it to work (LCEL, RAG, a
Streamlit chatbot). The heart of it was LCEL: `prompt | model | parser` — a
**straight line**, data flowing left → right, once. That's perfect until your app needs to **loop**
("try again if that failed"), **branch** ("route billing questions here, tech questions there"), or
**remember where it is**. A `|` chain can't do any of those. **LangGraph** can.

> **What you learn:** how to model an AI app as a **graph** — a set of **nodes** (steps) connected by
> **edges** (what runs next), sharing one **state** object. You'll build linear graphs, branching
> graphs, **looping** graphs, and finish with a **chatbot that remembers** across turns using a
> checkpointer — all on free **Groq**, **LangGraph 1.x**.

## Why a graph, when a chain worked fine?

A chain is a graph with no choices: A → B → C, always, once. Real agents need choices:

| You need to… | A `\|` chain | A LangGraph |
|--------------|-------------|-------------|
| Run steps in order | ✅ | ✅ |
| **Branch** on the data ("is this a refund or a complaint?") | ❌ | ✅ conditional edges |
| **Loop** ("retry until the JSON is valid") | ❌ | ✅ cycles |
| Keep **memory** of the conversation across calls | painful | ✅ checkpointer + `thread_id` |
| Let a model **decide** the next step (an agent!) | ❌ | ✅ (Day 25) |

LangGraph is the engine under real agents. Today we learn the engine; Day 24 adds **tools**, Day 25
wires it into a full **ReAct agent**.

## The mental model (learn these 3 words)
- **State** — one shared dictionary that every step can read and write. It flows through the graph.
- **Node** — a plain Python function: takes the state, returns the *bit of state it changed*.
- **Edge** — a wire saying "after this node, go to that one." Edges can be **fixed** or **conditional**.

That's the whole framework. Everything else is detail.

## Learning objectives
By the end of today you can:
- Explain why a straight LCEL chain can't loop or branch, and when to reach for a graph.
- Build a graph from `StateGraph(State)` + `add_node` + `add_edge` + `START` / `END`, then `.compile()`.
- Route between nodes at runtime with `add_conditional_edges` and a router function.
- Build a **cycle** (a node that can loop back to itself) with a clean exit condition.
- Use **reducers** (`Annotated[list, add]`, `add_messages`) so state **accumulates** instead of overwrites.
- Give a chatbot real memory with `MemorySaver` + a `thread_id`.

## What this reuses
| From    | Idea used here                                             |
|---------|------------------------------------------------------------|
| Day 21  | `ChatGroq`, message objects — now driven **by** the graph   |
| Day 16  | "Append every turn" memory — now automatic via a reducer    |
| Day 8   | Type hints / `TypedDict` — now to define the **State**      |
| Day 5   | Functions in, values out — a **node** is just a function    |

## Module index
| # | Folder | You learn |
|---|--------|-----------|
| 01 | [`01-why-langgraph/`](01-why-langgraph/README.md) | Chain vs graph; build & run the simplest possible one-node graph |
| 02 | [`02-state-and-nodes/`](02-state-and-nodes/README.md) | `TypedDict` state, nodes that return partial updates, linear edges |
| 03 | [`03-conditional-edges/`](03-conditional-edges/README.md) | Branching: `add_conditional_edges` + a router function |
| 04 | [`04-cycles-and-loops/`](04-cycles-and-loops/README.md) | The move a chain can't make — a node that loops until done |
| 05 | [`05-reducers-and-messages/`](05-reducers-and-messages/README.md) | Reducers (`Annotated[list, add]`, `add_messages`) — state that accumulates |
| 06 | [`06-chatbot-with-memory/`](06-chatbot-with-memory/README.md) | A real Groq chatbot that remembers: `MemorySaver` + `thread_id` |

### Exercises
| Folder | Practise |
|--------|----------|
| [`exercises/`](exercises/README.md) | Ticket Router (conditional edges) · Retry Loop (cycles) |

## How to run

**Setup (once).** Install with the real CPython (see repo `CLAUDE.md`):
```bash
pip install langgraph langchain-groq python-dotenv
```
Create a `.env` in the folder you run from with your free Groq key (only module 06 needs it):
```
GROQ_API_KEY=your_key_here
```
Get a free key at [console.groq.com/keys](https://console.groq.com/keys).

**Run the modules in order:**
```bash
python 01-why-langgraph/why_langgraph.py
python 02-state-and-nodes/state_and_nodes.py
python 03-conditional-edges/conditional_edges.py
python 04-cycles-and-loops/cycles_and_loops.py
python 05-reducers-and-messages/reducers_and_messages.py
python 06-chatbot-with-memory/chatbot_memory.py
```
Modules **01–05 need no key** — the graph machinery (state, branching, loops, reducers) is pure
Python and runs fully offline. Only **06** calls Groq, and it prints a clear skip message without a key.

## Today's exercise
Do both in [`exercises/`](exercises/README.md):
1. **Ticket Router** — a graph that classifies a support message and branches to the right handler.
2. **Retry Loop** — a graph that keeps attempting until it produces a valid result, then stops.

## Latest-syntax notes (LangGraph 1.x)
- Build with `StateGraph(State)`; connect with `add_edge` / `add_conditional_edges`; finish with `.compile()`.
- Import terminals from `langgraph.graph`: `from langgraph.graph import StateGraph, START, END`.
- A node returns **only the keys it changed** — LangGraph merges that into the state for you.
- For lists/messages, annotate the state field with a **reducer** so updates append, not replace:
  `Annotated[list, add_messages]`.
- Memory across calls = compile with a **checkpointer** (`MemorySaver`) and pass a `thread_id`.

## The big idea
> A chain answers **one** question. A graph runs a **process** — with branches, loops, and memory.
> Nodes are just functions, edges are just wires, and the state is just a dict. Once your app can
> *decide what to do next*, it stops being a Q&A bot and starts being an **agent**.

➡ Next: **Day 24 — Tool use / function calling** — give the model real tools (`@tool`, `bind_tools`)
so a graph node can *do* things, not just talk.
