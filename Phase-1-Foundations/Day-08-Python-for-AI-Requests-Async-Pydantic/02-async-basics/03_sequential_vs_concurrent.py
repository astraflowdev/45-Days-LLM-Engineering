"""
WHY async is worth it -- and the #1 beginner mistake.

Same three slow calls as 01_blocking_problem.py, but now they are coroutines.
We run them TWO ways and time both:

  1) Sequentially: `await` each one, then the next  -> still ~3s (the trap!)
  2) Concurrently: hand them all to asyncio.gather   -> ~1s (the payoff!)

The lesson: `async def` alone does NOT make things fast. `await call_a()` then
`await call_b()` still waits one-at-a-time. The speed comes from STARTING them
together (gather) so their waiting overlaps.

Run:
    python 03_sequential_vs_concurrent.py
"""

import asyncio
import time


async def fake_api_call(name, seconds):
    """Each call mostly just WAITS -- perfect candidate to overlap."""
    print(f"  start  {name}")
    await asyncio.sleep(seconds)      # non-blocking: the loop can run others now
    print(f"  done   {name}")
    return f"{name} result"


async def run_sequentially():
    """The trap: await one, THEN the next. No overlap -> times add up."""
    print("Sequential (await one at a time):")
    start = time.perf_counter()
    r1 = await fake_api_call("model-A", 1.0)
    r2 = await fake_api_call("model-B", 1.0)
    r3 = await fake_api_call("model-C", 1.0)
    elapsed = time.perf_counter() - start
    print(f"  -> took {elapsed:.2f}s   (~3s, no faster than normal code)\n")
    return [r1, r2, r3]


async def run_concurrently():
    """The win: gather STARTS all three, then waits once. Waiting overlaps."""
    print("Concurrent (asyncio.gather):")
    start = time.perf_counter()
    results = await asyncio.gather(
        fake_api_call("model-A", 1.0),
        fake_api_call("model-B", 1.0),
        fake_api_call("model-C", 1.0),
    )
    elapsed = time.perf_counter() - start
    print(f"  -> took {elapsed:.2f}s   (~1s, the slowest single call)\n")
    return results


async def main():
    await run_sequentially()
    await run_concurrently()
    print("Same work, same coroutines -- gather just let the waiting overlap.")


asyncio.run(main())
