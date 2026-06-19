"""
WHAT async is -- your first coroutine.

An `async def` function is special: calling it does NOT run it. It hands you a
"coroutine" object -- a recipe that hasn't been cooked yet. You need an event
loop (started by asyncio.run) to actually run it. Inside, `await` is where the
function is allowed to PAUSE and let the loop do other things.

This script has no speed-up yet -- it just shows the three new words:
    async def   ->  defines a coroutine
    await       ->  pause here until the awaited thing is ready
    asyncio.run ->  start the loop and run a coroutine to completion

Run:
    python 02_first_coroutine.py
"""

import asyncio


async def greet(name):
    """A coroutine. The `await` is a pause point, not a normal function call."""
    print(f"  ...waiting to greet {name}")
    await asyncio.sleep(1)            # non-blocking pause (vs time.sleep, which blocks)
    return f"Hello, {name}"


# Calling an async function does NOT run it -- watch:
maybe = greet("Aarav")
print("greet('Aarav') gave us:", maybe)        # a coroutine object, not "Hello"!
print("Type:", type(maybe).__name__)
maybe.close()                                   # tidy up the unused coroutine

print()
print("To actually RUN it, we need asyncio.run:")

# asyncio.run starts the event loop, runs the coroutine, returns its result.
result = asyncio.run(greet("Priya"))
print("Result:", result)

print()
print("Takeaway: async def = a recipe. asyncio.run = the oven that cooks it.")
