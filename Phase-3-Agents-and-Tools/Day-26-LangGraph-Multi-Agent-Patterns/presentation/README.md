# Day 26 deck — *LangGraph multi-agent patterns: one agent, then a team* (speaker notes)

Open [`index.html`](index.html) in any browser. `→` / `Space` to advance, `F` for fullscreen.
15 slides ≈ 30 min, leaving the rest of the 3-hour block for the modules + mini-project.

**The through-line:** Day 24 gave them the graph engine; Day 25 gave them one ReAct agent. Today the
whole point is one sentence — **"an agent is just a node; a team is just a graph."** Multi-agent needs
*no new engine*: it is Day 24's `StateGraph` with more nodes, wired in three shapes (Sequential,
Supervisor, Parallel). Keep saying **"same engine, more nodes"** so nobody thinks a new framework
appeared.

| # | Slide | Time | What to say / do |
|---|-------|------|------------------|
| 1 | Cover | 1′ | "Everything so far has been one agent. Real work needs a team — a researcher, a writer, an editor. Tonight you'll build teams, and you already have the engine to do it." |
| 2 | Recap: you own the engine | 2′ | Two cards: Day 24 = graph engine (nodes/edges/loops/reducers/memory), Day 25 = one agent in a line. Land: "today we just add more nodes." |
| 3 | The core idea | 3′ | The whole day in one line: **an agent is a node, a team is a graph.** Point at the code — three agent functions, one `StateGraph`. Repeat: "no new library today." This is the slide they must remember. |
| 4 | Three shapes | 3′ | The map of the day: Sequential (assembly line), Supervisor (boss routes), Parallel (fan-out/fan-in). Walk the three tiny SVG thumbnails. "The rest of the deck is one pair of slides per shape." |
| 5 | Sequential — the line | 3′ | researcher → writer → editor. Walk the left-to-right SVG. The code is just ordinary `add_edge` calls — a straight line, no conditions. When to use: a **fixed pipeline**, each step needs the last one's output. |
| 6 | Sequential — the hand-off | 3′ | Key point: **agents never talk directly — they hand off through the state.** Researcher writes `notes`, writer reads `notes` + writes `draft`, editor reads `draft`. Gotcha: a plain *list* key overwrites (last writer wins) — fine for single strings, but flag it now because Shape 3 fixes it with a reducer. |
| 7 | Supervisor — a boss routes | 4′ | Walk the SVG: supervisor on top, three workers below, **every worker edges BACK to the supervisor** — that back-edge is what makes it hierarchical (a loop). Mechanic = `add_conditional_edges` (Day 24). When to use: the worker/order **depends on the input** — routing, judgement. |
| 8 | Supervisor — the router | 3′ | Zoom on the router function: the supervisor writes a **decision word** into state; the router returns it; the dict maps word → next node (or `END`). Workers loop back so it can route again. `recursion_limit` = the safety belt against a mis-routing boss spinning forever. "This is Day 24's conditional-edge + loop, with agents as destinations." |
| 9 | Parallel — fan-out / fan-in | 3′ | Walk the SVG: one `dispatch` node fans out to three reviewers that **run concurrently**, then all merge into `combine` which **waits for all**. Fan-out = one → several; fan-in = several → one. When to use: **independent** opinions on the *same* input; also speed. |
| 10 | Parallel — the reducer | 4′ | The trap and the fix. Three reviewers write the same field at once → without help the last one wins and two notes vanish. The fix is the **reducer**: each returns a single-item list, `Annotated[list, operator.add]` concatenates them. Stress: **this is Day 24's reducer** — nothing new, just applied to a review panel. |
| 11 | Memory for a team | 3′ | Same two knobs as Day 24: `compile(checkpointer=MemorySaver())` + a `thread_id` per conversation. The checkpointer saves the **whole shared state** — notes, drafts, everything. Punchline: "there is nothing special about multi-agent memory; a team is one compiled graph." |
| 12 | Which shape when? | 2′ | The scoreboard table: Sequential = fixed order / pipeline; Supervisor = dynamic routing / judgement; Parallel = independent opinions / speed. Then the real-world note: production teams **combine** them (supervisor → parallel panel → sequential polish). |
| 13 | Mini-project | 3′ | Sell it: **SoftDesk Content Crew** — one example (topic → polished blurb) grown 6 times, each step adds exactly one shape onto the same code: single writer → sequential → +editor → supervisor → parallel panel → crew + memory + Streamlit. All offline-graceful. |
| 14 | Roadmap | 2′ | Motivation: 24 engine → 25 one agent → 26 multi-agent by hand → frameworks (CrewAI, AutoGen). "You just built the frameworks by hand; when you meet CrewAI you'll recognise sequential / supervisor / parallel under the hood." |
| 15 | Recap / close | 1′ | Read the three shapes back; class fills them in. Close on the mantra: **an agent is a node, a team is a graph.** Tee up CrewAI. |

## Q&A ammo
- **"Do I need a special multi-agent framework?"** No — that is the whole point of today. A team is a
  `StateGraph` with more nodes. Frameworks (CrewAI/AutoGen, next days) add roles and convenience on
  top of exactly these shapes; they don't add a new engine.
- **"Can agents talk to each other directly?"** They communicate **through the shared state**, not by
  calling each other. One node writes a key, the next reads it. That's the hand-off. It keeps the
  system inspectable — you can print the state between any two nodes.
- **"Sequential vs Supervisor — when does 'order depends on input' matter?"** If the pipeline is always
  the same (research → write → edit), use Sequential. If *which* worker runs, or how many times,
  depends on the request (a billing question vs a tech question), you need a Supervisor to decide at
  runtime.
- **"Why does Parallel need a reducer but Sequential doesn't?"** In Sequential only one node writes a
  given field at a time, so overwrite is fine. In Parallel several nodes write the **same** field
  concurrently — without a reducer LangGraph keeps only one. `Annotated[list, operator.add]` merges
  them. Same reducer idea as Day 24's `add_messages`.
- **"Is it really running the reviewers at the same time?"** LangGraph schedules fan-out branches
  together (a super-step). For LLM calls that means overlapped I/O — faster than calling them one after
  another — and the fan-in node waits until all branches finish before it runs.
- **"Does it work without an API key?"** The wiring does — the mini-project steps run with a scripted
  stand-in so students watch the shapes execute offline. Real writing/reviewing needs a Groq key (free
  tier).

## If you're short on time
Cut slide 8 (router detail) and slide 12 (scoreboard) — mention them verbally. Never cut 3 (the core
idea), 4 (three shapes), or 10 (the reducer): those carry the day's whole argument. Slides 5/7/9 (the
three shape diagrams) are the visual backbone — keep all three.
