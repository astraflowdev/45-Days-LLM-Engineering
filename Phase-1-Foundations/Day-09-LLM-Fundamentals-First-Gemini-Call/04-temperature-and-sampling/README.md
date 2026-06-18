# 04 — Temperature & Sampling

When a model writes the next token, it doesn't pick one fixed answer — it picks from a **probability
distribution**. **Sampling settings** control how adventurous that pick is.

## Temperature
The big dial. Roughly **0.0 = focused/deterministic**, **1.0+ = creative/random**.

| Temperature | Behaviour | Use it for |
|:-----------:|-----------|------------|
| `0.0`–`0.3` | consistent, predictable | extraction, code, facts, JSON |
| `0.4`–`0.7` | balanced | general chat, summaries |
| `0.8`–`1.5` | varied, surprising | brainstorming, creative writing |

## Top-p (nucleus sampling)
Instead of considering all possible next tokens, **top-p** keeps only the most likely ones that add
up to probability `p` (e.g. `0.95`), then samples from those. Lower `top_p` = safer, more focused.

You usually tune **temperature first**; leave `top_p` near its default unless you need finer control.

## How to set them
```python
from google.generativeai.types import GenerationConfig

model.generate_content(
    "Give me a startup name for an AI tutoring app.",
    generation_config=GenerationConfig(temperature=0.9, top_p=0.95),
)
```

## The rule to remember
> **Need the same answer every time? Use a low temperature.** Need variety? Turn it up.

Run it to see the same prompt at low vs high temperature (needs `GEMINI_API_KEY`):

```bash
python temperature_demo.py
```

➡ Next: [05-model-families](../05-model-families/)
