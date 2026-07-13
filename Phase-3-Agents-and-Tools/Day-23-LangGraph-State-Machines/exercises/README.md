# Day 23 · Exercises

Build two small LangGraph programs yourself. Each has a stub with `# TODO`s and a worked
`_solution.py`. **Both run without a key** — the graph machinery (branching, loops, state) is pure
Python — so you can focus on the *shape*, not an API call.

## 1. Ticket Router (`ticket_router.py`)

Build a graph that reads a support message and **branches** to the right handler — the module-03
pattern, on your own.

- State: `message`, `priority` (`"high"` / `"low"`), `reply`.
- A `triage` node that sets `priority` (rule-based: words like *urgent*, *down*, *refund* → high).
- A **router** function returning `"high"` or `"low"`, wired with `add_conditional_edges`.
- Two handler nodes: `escalate` (high) and `auto_reply` (low), each writing `reply`.

> **Skills:** state & nodes (02), conditional edges / routing (03).

## 2. Retry Loop (`retry_loop.py`)

Build a graph that **keeps trying until it succeeds**, then stops — the module-04 cycle, on your own.

- State: `target` (a number to reach), `value`, `attempts`.
- A `step` node that moves `value` closer to `target` and bumps `attempts`.
- A **router** (`keep_going`) that returns `"loop"` until `value >= target` (or an attempt cap is
  hit), then `"done"`.
- Wire the `"loop"` branch **back to `step`** to form the cycle.

> **Skills:** reducers optional (05), cycles + a safe exit condition (04).

## Run

```bash
python ticket_router_solution.py
python retry_loop_solution.py
```
(Swap `_solution` for the stub name once you've filled in the TODOs.) No key needed for either.

## Stretch

- **Ticket Router:** add a third `priority` (`"medium"`) and a third handler; classify with a real
  Groq call instead of keyword rules (return the label from the model).
- **Retry Loop:** give the state an `Annotated[list, add]` `log` field (module 05) so every attempt is
  recorded, and print the full trail at the end.

➡ Back to the day: [README](../README.md)
