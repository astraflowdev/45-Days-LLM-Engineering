# 03 — A Groq Provider Function

**Groq** runs open models (Llama and friends) on special hardware that's **very fast** — great when
latency matters or you want a second opinion. It has a **free tier**, and its API looks like the
OpenAI chat format.

## Get a free key
[console.groq.com/keys](https://console.groq.com/keys) → add `GROQ_API_KEY` to your `.env`.

## Same shape, different SDK
```python
from groq import Groq

def ask_groq(prompt: str) -> str:
    client = Groq(api_key=os.environ["GROQ_API_KEY"])
    chat = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
    )
    return chat.choices[0].message.content
```

Note the **messages** format — a list of `{role, content}` dicts. This "chat completions" shape is an
industry standard you'll see across many providers.

| | Gemini | Groq |
|--|--------|------|
| Input | a prompt string | a `messages` list |
| Output | `response.text` | `choices[0].message.content` |
| Our wrapper hides this | `ask_gemini` | `ask_groq` |

> Model names change — if `llama-3.3-70b-versatile` is gone, check the Groq docs for the current one.

```bash
python groq_provider.py
```

➡ Next: [04-ollama-local](../04-ollama-local/)
