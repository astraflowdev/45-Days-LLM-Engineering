"""
Async basics -- run slow tasks concurrently with asyncio.

We simulate slow "API calls" with asyncio.sleep so this runs with the standard
library alone (no network). The lesson: gather() overlaps the waiting.

Run:
    python async_basics.py
"""

import asyncio
import time


async def fake_api_call(name, seconds):
    """Pretend to call a slow LLM. await lets other work run while we wait."""
    print(f"  start  {name}")
    await asyncio.sleep(seconds)      # non-blocking wait (yields to the loop)
    print(f"  done   {name}")
    return f"{name} result"


async def main():
    # --- Concurrent: all three run together, total time ~= the SLOWEST one ---
    start = time.perf_counter()
    results = await asyncio.gather(
        fake_api_call("model-A", 1.0),
        fake_api_call("model-B", 1.0),
        fake_api_call("model-C", 1.0),
    )
    elapsed = time.perf_counter() - start

    print()
    print("Results:", results)
    print(f"Three 1-second calls took {elapsed:.2f}s (concurrent, not 3s).")


# asyncio.run() starts the event loop, runs main() to completion, then stops it.
asyncio.run(main())
