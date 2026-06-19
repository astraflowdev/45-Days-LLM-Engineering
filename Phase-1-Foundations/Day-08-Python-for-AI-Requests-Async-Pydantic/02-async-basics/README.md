# 02 — Async Basics: Doing Many Things at Once

LLM calls are **slow** — each one waits seconds for a server to reply. If you make 10 calls one
after another, you wait for all 10 in a row. With **async**, you fire them off together and wait
once. This is the single biggest speed win in AI apps.

We'll build the idea up in **four tiny scripts** — feel the problem first, then learn the cure.

| Run in order | Shows |
|--------------|-------|
| `python 01_blocking_problem.py` | **The problem** — 3 slow calls done normally = 3s of idle waiting |
| `python 02_first_coroutine.py` | **What async is** — `async def`, `await`, `asyncio.run` (no speed-up yet) |
| `python 03_sequential_vs_concurrent.py` | **Why it's worth it** — sequential (~3s, the trap) vs `gather` (~1s) side by side |
| `python async_basics.py` | **The clean recap** — the `gather` pattern on its own |
| `python 04_real_http_async.py` | **For real** — same trick over the network with `httpx.AsyncClient` *(needs internet)* |

Scripts 01–03 and `async_basics.py` run **offline**. Script 04 makes real web requests, so it
needs internet (and `pip install httpx`).

## The idea
- A normal (`def`) function runs top to bottom, **blocking** until each line finishes. While it
  waits for a slow server, the whole program just sits there (see `01_blocking_problem.py`).
- An `async def` function (a *coroutine*) can **pause** at an `await` and let other work run while
  it waits — then resume. That's what lets the waiting **overlap**.

```python
import asyncio

async def greet(name):
    await asyncio.sleep(1)      # pretend this is a slow API call (a pause point)
    return f"Hello, {name}"

async def main():
    # gather STARTS all three, then waits once -> ~1 second total, not 3
    results = await asyncio.gather(greet("Aarav"), greet("Priya"), greet("Sam"))
    print(results)

asyncio.run(main())             # asyncio.run starts the event loop
```

## The three new words
| Word | What it does | Gotcha |
|------|--------------|--------|
| `async def` | Defines a *coroutine* (a pausable function) | **Calling it doesn't run it** — you get a coroutine object back |
| `await` | "Pause here until this is ready, let others run meanwhile" | Only allowed **inside** an `async def` |
| `asyncio.run(main())` | Starts the event loop and runs a coroutine to the end | This is your **one** entry point — don't nest it |

## The mistake everyone makes first
`async def` alone is **not** faster. Awaiting one call, *then* the next, still waits one-at-a-time:

```python
r1 = await call_a()   # waits 1s...
r2 = await call_b()   # ...THEN waits another 1s  -> 2s total, no win
```

The speed comes from **starting them together** so the waiting overlaps:

```python
r1, r2 = await asyncio.gather(call_a(), call_b())   # ~1s total
```

`03_sequential_vs_concurrent.py` runs both and times them so you can see the difference.

## For real HTTP
`requests` is **synchronous** (it blocks). The async equivalent is **`httpx.AsyncClient`** (or
`aiohttp`): `await client.get(url)`. Same idea, real network calls. **`04_real_http_async.py`** does
exactly this — sequential vs concurrent against a live API. You'll use this pattern to hit several
models at once.

➡ Next: [03-dotenv-and-secrets](../03-dotenv-and-secrets/)
