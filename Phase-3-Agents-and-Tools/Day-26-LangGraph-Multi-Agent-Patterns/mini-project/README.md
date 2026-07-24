# Mini-project · SoftDesk Content Crew

**One example, grown six times.** We build a small "content crew" that turns a
**topic** into a polished marketing **blurb** — adding exactly one of today's
patterns at each step. Every `stepN_*.py` runs on its own; each is a visible diff
over the one before.

> All steps need a free **`GROQ_API_KEY`** in a `.env` file **in this folder**:
> ```
> GROQ_API_KEY=your_key_here
> ```
> Get one at [console.groq.com/keys](https://console.groq.com/keys).

## The build, step by step
| Step | File | Adds | Pattern (module) |
|------|------|------|------------------|
| 1 | `step1_single_writer.py` | one writer agent (one node) | — |
| 2 | `step2_sequential.py` | a researcher **before** the writer | Sequential (02) |
| 3 | `step3_add_editor.py` | an editor **after** the writer (3-stage line) | Sequential (02) |
| 4 | `step4_supervisor.py` | a **supervisor** that decides the next step | Supervisor (03) |
| 5 | `step5_parallel.py` | a **parallel review panel** (fact / seo / tone) | Parallel (04) |
| 6 | `step6_content_crew.py` | the finished, reusable crew **+ memory** | Memory (05) |
| — | `app.py` | a thin Streamlit UI over step 6 | — |

## Run them in order
```bash
python step1_single_writer.py
python step2_sequential.py
python step3_add_editor.py
python step4_supervisor.py
python step5_parallel.py
python step6_content_crew.py
streamlit run app.py
```

## How the final crew fits together (step 6)
```
START → researcher → writer ─┬─→ fact-checker ─┐
                             ├─→ seo-expert ────┤→ editor → END
                             └─→ tone-expert ───┘
        (compiled with MemorySaver → a thread_id remembers the campaign)
```
It combines the patterns: a **sequential** spine, a **parallel** review panel, and
**memory**. `step6` exposes ONE function — `run(topic, thread_id)` → the blurb, the
review notes, and a build **trail** — with **no Streamlit**, so it stays importable
and testable. `app.py` is only the web layer on top.

## Design choices (worth teaching)
- **`step6` has no Streamlit.** Keeping the crew in a plain module means you can
  `import` and test it; the UI is a thin wrapper. (Same split as Day 20 / Day 23.)
- **The crew is built once** at import (`CREW = build_crew()`), then reused — you
  don't rebuild the graph on every request.
- **Each browser session gets its own `thread_id`**, so one user's "blurbs produced
  this session" memory doesn't leak into another's.

## Checkpoint questions
1. In step 4, why does every worker edge **back** to the supervisor? (What would
   break if `editor` went straight to `END`?)
2. In step 5, what happens to the review notes if you drop the
   `Annotated[list, operator.add]` reducer on `reviews`?
3. In step 6, why is `run()` in a plain module instead of inside `app.py`?

## Stretch goals
- Add a **`translator`** agent after the editor (sequential) to produce a Hindi blurb.
- Give the **supervisor from step 4** the power to send a weak draft back to the
  writer for one rewrite (a quality loop, like Day 24's review→improve cycle).
- Show the **build trail** live in Streamlit with `st.status(...)` as each agent runs.

➡ Back to the [day README](../README.md) · or the [exercises](../exercises/README.md).
