"""
THE PROBLEM async solves -- slow tasks done one-at-a-time.

Before we learn async, feel the pain it removes. Here we make three "API calls"
the NORMAL (synchronous) way. Each one blocks: Python sits and waits for it to
finish before even starting the next. So the total time is the SUM of all three.

Nothing async here yet -- this is plain Python, on purpose.

Run:
    python 01_blocking_problem.py
"""

import time


def fake_api_call(name, seconds):
    """Pretend to call a slow server. time.sleep BLOCKS -- nothing else can run."""
    print(f"  start  {name}")
    time.sleep(seconds)               # the whole program freezes here
    print(f"  done   {name}")
    return f"{name} result"


start = time.perf_counter()

# Three calls, one after another. Call B cannot begin until A is fully done.
r1 = fake_api_call("model-A", 1.0)
r2 = fake_api_call("model-B", 1.0)
r3 = fake_api_call("model-C", 1.0)

elapsed = time.perf_counter() - start

print()
print("Results:", [r1, r2, r3])
print(f"Three 1-second calls took {elapsed:.2f}s -- about 3s (1 + 1 + 1).")
print("We waited 3 seconds, but the computer was idle the whole time!")
print("Each call was just WAITING for a reply -- it could have waited together.")
