"""
Solution -- Exercise 2: fallback chain.

Uses fake providers so it runs with no keys. The logic is identical with real
ask_gemini/ask_groq/ask_ollama functions.

Run: python fallback_chain_solution.py
"""


def broken_provider(prompt: str) -> str:
    raise RuntimeError("simulated outage")


def working_provider(prompt: str) -> str:
    return f"[backup] {prompt}"


PROVIDERS = {"primary": broken_provider, "backup": working_provider}


def ask_with_fallback(prompt: str, order=("primary", "backup")) -> str:
    for name in order:
        try:
            return PROVIDERS[name](prompt)
        except Exception as err:
            print(f"  {name} failed ({err}); trying next...")
    raise RuntimeError("All providers failed.")


result = ask_with_fallback("Summarize Day 12 in one line.", order=("primary", "backup"))
print("Result:", result)
