# 05 — One Interface (with Fallback)

Now we tie the three provider functions together behind a single `ask()` — plus a **fallback chain**
so one provider failing doesn't break your app.

## The dispatcher
```python
PROVIDERS = {"gemini": ask_gemini, "groq": ask_groq, "ollama": ask_ollama}

def ask(prompt: str, provider: str = "gemini") -> str:
    return PROVIDERS[provider](prompt)
```

One line to switch provider — exactly what module 01 promised.

## Add a fallback chain
If the first provider errors (rate limit, network, bad key), try the next one:

```python
def ask_with_fallback(prompt: str, order=("gemini", "groq", "ollama")) -> str:
    for name in order:
        try:
            return PROVIDERS[name](prompt)
        except Exception as err:
            print(f"  {name} failed ({err}); trying next...")
    raise RuntimeError("All providers failed.")
```

| Pattern | Benefit |
|---------|---------|
| `ask(prompt, provider)` | swap with one argument |
| `ask_with_fallback(...)` | survive a provider outage |
| dict of functions | add a provider = add one entry |

## Why this is a big deal
Your whole app now depends on **`ask()`**, not on any vendor. Demos don't die on a rate limit;
you can A/B providers; on-prem deployments just reorder the chain to local-first.

```bash
python ask.py     # tries gemini -> groq -> ollama, prints whichever answers
```

➡ Next: practise in [../exercises/](../exercises/)
