# 01 — The Provider Problem

It's tempting to scatter `genai.GenerativeModel(...)` calls all over your app. Then one day:

- Gemini hits a **rate limit** during your demo, or
- you want to try **Groq** because it's faster, or
- a client needs everything **on-premise** (Ollama), or
- Gemini changes a model name and **20 files** break.

If the provider is hardcoded everywhere, every one of these is a painful rewrite.

## The fix: one seam
Put **all** provider code behind a single function:

```python
answer = ask("Summarize this.", provider="gemini")
```

Your whole app calls `ask(...)`. Switching providers, adding a fallback, or upgrading a model name
happens in **one place**.

| Hardcoded everywhere | Behind one `ask()` |
|----------------------|--------------------|
| swap = edit many files | swap = change one default |
| no fallback | easy to add a fallback chain |
| testing is hard | mock one function |

This is just good software design — the same reason you write functions at all. The script shows the
"scattered vs centralized" idea in pseudo-form (no API needed).

```bash
python provider_problem.py
```

➡ Next: [02-gemini-provider](../02-gemini-provider/)
