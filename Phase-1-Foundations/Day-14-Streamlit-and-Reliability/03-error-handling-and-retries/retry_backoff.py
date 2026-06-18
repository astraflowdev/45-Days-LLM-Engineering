"""
Retry with exponential backoff (standard library -- runs anywhere).

A fake function fails the first couple of times, then succeeds -- exactly like
a flaky API call. We retry with growing waits instead of crashing.

Run:
    python retry_backoff.py
"""

import time

# A fake flaky call: fails twice, then works. (Closure over a mutable counter.)
attempts = {"n": 0}


def flaky_call():
    attempts["n"] += 1
    if attempts["n"] < 3:
        raise ConnectionError("simulated 429 / network blip")
    return "success!"


def with_retry(call, max_tries=4, base_delay=0.2):
    for attempt in range(max_tries):
        try:
            return call()
        except Exception as err:
            if attempt == max_tries - 1:
                raise                                  # out of retries
            wait = base_delay * (2 ** attempt)         # 0.2, 0.4, 0.8 ...
            print(f"  attempt {attempt + 1} failed ({err}); retrying in {wait:.1f}s")
            time.sleep(wait)


result = with_retry(flaky_call)
print("Result:", result, f"(after {attempts['n']} attempts)")
