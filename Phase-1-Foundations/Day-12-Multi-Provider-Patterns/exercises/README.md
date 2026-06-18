# Day 12 — Exercises

```bash
pip install google-generativeai groq python-dotenv   # + GEMINI_API_KEY, GROQ_API_KEY in .env
```

---

## Exercise 1 — Provider-switching CLI 🔀
Pick the LLM backend from an environment variable at runtime.

**Your task:** in `provider_cli.py`, read `LLM_PROVIDER` from the environment (default `"gemini"`),
look up the matching `ask_*` function in a dict, send a prompt, and print the answer. Switching
provider should be just `LLM_PROVIDER=groq python provider_cli.py`.

➡ Solution: [`provider_cli_solution.py`](provider_cli_solution.py)

---

## Exercise 2 — Fallback chain 🛟
Make it survive a failing provider.

**Your task:** in `fallback_chain.py`, write `ask_with_fallback(prompt, order)` that tries each
provider in order and returns the first success; if one raises, print a note and try the next. Test
it with a deliberately broken provider first in the order.

*Hint:* wrap each call in `try/except Exception`.

➡ Solution: [`fallback_chain_solution.py`](fallback_chain_solution.py)
