# 04 · Parallel agents (fan-out / fan-in)

Sometimes several agents should look at the **same** input **independently** and at
the same time — like sending a draft to three reviewers at once.

```
              +--> [fact-checker] --+
 [dispatch] --+--> [seo-expert] ----+--> [aggregate] --> END
              +--> [tone-expert] ---+
```

## Two mechanics
| Mechanic | How | Effect |
|----------|-----|--------|
| **Fan-out** | one node → **several** nodes (`START` → all three reviewers) | they run **concurrently** |
| **Fan-in** | several nodes → **one** node (all three → `aggregate`) | LangGraph **waits for all** before running it |

```python
# fan-out
g.add_edge(START, "fact_checker")
g.add_edge(START, "seo_expert")
g.add_edge(START, "tone_expert")
# fan-in (aggregate has 3 incoming edges -> it waits for all 3)
g.add_edge("fact_checker", "aggregate")
g.add_edge("seo_expert", "aggregate")
g.add_edge("tone_expert", "aggregate")
```

## The reducer is the whole trick
Three nodes all write to the **same** state key, `reviews`. With a plain key, the
**last writer wins** — two reviews vanish. A **reducer** tells LangGraph how to
*combine* concurrent writes instead of overwriting:

```python
import operator
from typing import Annotated

class State(TypedDict):
    reviews: Annotated[list, operator.add]   # <- accumulate, don't overwrite
```

Each specialist returns a **single-item list**; `operator.add` concatenates them, so
all three notes survive:

```python
return {"reviews": [f"{name}: {note}"]}   # the list matters
```

You met reducers on Day 24 (`Annotated[list, add]`, `add_messages`). This is the
same idea, now doing real work.

| Without reducer | With `Annotated[list, add]` |
|-----------------|------------------------------|
| last review overwrites the rest | all reviews kept |
| `reviews` = 1 item | `reviews` = 3 items |

## When to use parallel
- The agents are **independent** — none needs another's output.
- You want **speed** (three calls at once, not one after another).
- You'll **merge** their outputs afterward (the fan-in / aggregate node).

If one agent needs the previous one's result, that's **sequential**, not parallel.

## Run it
```bash
python parallel_agents.py     # needs GROQ_API_KEY in a .env file here
```
Three reviewers critique one (deliberately over-hyped) draft; the aggregate node
prints all three merged notes.

➡ Next: [05 · Agents with memory](../05-agents-with-memory/README.md)
