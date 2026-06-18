# 02 — Async Basics: Doing Many Things at Once

LLM calls are **slow** — each one waits seconds for a server to reply. If you make 10 calls one
after another, you wait for all 10 in a row. With **async**, you fire them off together and wait
once. This is the single biggest speed win in AI apps.

## The idea
- A normal (`def`) function runs top to bottom, **blocking** until each line finishes.
- An `async def` function (a *coroutine*) can **pause** at an `await` and let other work run while
  it waits — then resume.

```python
import asyncio

async def greet(name):
    await asyncio.sleep(1)      # pretend this is a slow API call
    return f"Hello, {name}"

async def main():
    # gather runs all three CONCURRENTLY -> ~1 second total, not 3
    results = await asyncio.gather(greet("Aarav"), greet("Priya"), greet("Sam"))
    print(results)

asyncio.run(main())             # asyncio.run starts the event loop
```

## Key rules
| Rule | Why |
|------|-----|
| `await` only inside an `async def` | `await` needs a coroutine to pause |
| `asyncio.run(main())` is the entry point | it starts/stops the event loop |
| `asyncio.gather(...)` runs awaitables **concurrently** | the whole point — overlap the waiting |

## For real HTTP
`requests` is **synchronous**. The async equivalent is **`httpx.AsyncClient`** (or `aiohttp`):
`await client.get(url)`. Same idea, real network calls. You'll use this to hit several models at once.

Run the demo (standard library only):

```bash
python async_basics.py
```

➡ Next: [03-dotenv-and-secrets](../03-dotenv-and-secrets/)
