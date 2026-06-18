# 04 — Ollama: Models on Your Own Machine

**Ollama** runs open models **locally** — no API key, no rate limits, fully private, works offline.
The trade-off is quality/speed depends on your laptop, but for many tasks a small local model is
plenty (and free forever).

## Setup
1. Install Ollama from [ollama.com](https://ollama.com).
2. Pull a small model: `ollama pull llama3.2`
3. Ollama runs a local server in the background (at `http://localhost:11434`).

## Same shape again
```python
import ollama

def ask_ollama(prompt: str) -> str:
    response = ollama.chat(
        model="llama3.2",
        messages=[{"role": "user", "content": prompt}],
    )
    return response["message"]["content"]
```

Notice it uses the **same `messages` format** as Groq — and our wrapper gives it the **same
signature** as the others.

## When to reach for local
| Use Ollama when… | Prefer hosted (Gemini/Groq) when… |
|------------------|-----------------------------------|
| privacy / offline matters | you want top quality |
| you're hammering it (no limits) | your laptop is weak |
| zero cost is a hard requirement | you need big context windows |

> Three providers, three SDKs, **one signature**: `ask_x(prompt) -> str`. Module 05 unifies them.

```bash
python ollama_local.py     # needs Ollama running + a pulled model
```

➡ Next: [05-one-interface](../05-one-interface/)
