# 01 — Your First Gemini Call

Time to talk to a real LLM. We'll use Google's **Gemini** — it has a generous **free tier**, so it's
perfect for learning.

## Three steps
1. **Configure** the SDK with your key (from `.env`, never hardcoded).
2. **Pick a model** — `gemini-2.0-flash` is fast and free.
3. **Generate** — send a prompt, read `response.text`.

```python
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-2.0-flash")
response = model.generate_content("Explain what an API is in one sentence.")
print(response.text)
```

## What you get back
`response.text` is the model's answer as a string. The full `response` also carries metadata —
token counts, safety info, and the finish reason — which you'll use later.

| You send | You get |
|----------|---------|
| a prompt (string) | `response.text` (the answer) |
| | `response.usage_metadata` (token counts) |

## Gotchas
- Model names change over time. If `gemini-2.0-flash` isn't available, check
  [ai.google.dev/models](https://ai.google.dev/gemini-api/docs/models) for the current free model.
- Free tiers have **rate limits** (requests per minute). You'll handle those on Day 14.

Run it (needs `GEMINI_API_KEY` in `.env`):

```bash
python first_call.py
```

➡ Next: [02-tokens-and-tokenization](../02-tokens-and-tokenization/)
