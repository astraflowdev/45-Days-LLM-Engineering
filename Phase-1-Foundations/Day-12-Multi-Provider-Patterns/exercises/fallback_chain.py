"""
Exercise 2 -- fallback chain (survive a failing provider).

This version uses fake providers so it runs with no keys -- focus on the
fallback logic, then swap in the real ask_* functions.

Run: python fallback_chain.py
"""


def broken_provider(prompt: str) -> str:
    raise RuntimeError("simulated outage")


def working_provider(prompt: str) -> str:
    return f"[backup] {prompt}"


PROVIDERS = {"primary": broken_provider, "backup": working_provider}

# TODO 1: write ask_with_fallback(prompt, order) that tries each provider in `order`
#         and returns the first success
# TODO 2: on an exception, print a note (which provider failed) and try the next
# TODO 3: call it with order=("primary", "backup") and print the result
