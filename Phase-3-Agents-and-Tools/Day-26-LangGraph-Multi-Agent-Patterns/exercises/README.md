# Exercises · Day 26

Two exercises, one per core pattern. Each has a stub (with `# TODO`s) and a worked
`_solution.py`. Both need a free **`GROQ_API_KEY`** in a `.env` file in this folder.

> **Work the [Problem-Solving Bootcamp](../../../Problem-Solving-Bootcamp/) rules:**
> plan before you code · struggle ~20 min before peeking · climb hints one rung at a
> time · after solving, cover it and rewrite from scratch.

## 1. Summarize → Translate (sequential)
**File:** `summarize_translate.py` → solution: `summarize_translate_solution.py`

Build a **two-agent assembly line**: a summarizer condenses a long text to one
sentence, then a translator turns that sentence into Hindi.

- **Practises:** the sequential pattern (Module 02) — state carries the hand-off.
- **Done when:** running it prints a one-sentence summary and its Hindi translation.
- **Stretch:** add a third agent that back-translates the Hindi to English so you can
  sanity-check the translation.

## 2. Route to a specialist (supervisor)
**File:** `route_to_specialist.py` → solution: `route_to_specialist_solution.py`

Build a **supervisor** that reads a request and routes it to one of three
specialists — `math`, `code`, or `writing` — using conditional edges.

- **Practises:** the supervisor pattern (Module 03) — a router turns a decision into
  the next node.
- **Done when:** a maths question goes to `math` and a code question goes to `code`,
  through the same graph.
- **Stretch:** add a back-edge from each specialist to the supervisor and let the
  supervisor say `FINISH` — turning the single-shot router into a loop (like the
  mini-project's step 4).

## Hints
- A node returns **only the keys it changed** — a dict like `{"summary": ...}`.
- The **router function** for `add_conditional_edges` returns a **node name string**
  (or `END`). Its return values must be in the list you pass as the third argument.
- Always **sanitize** the supervisor's word before routing (models add stray text):
  `next((s for s in SPECIALISTS if s in choice), "writing")`.

➡ Back to the [day README](../README.md).
