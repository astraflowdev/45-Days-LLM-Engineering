# 04 — Rate Limits & Cost Awareness

Free tiers are generous but **not infinite**. Two limits matter:

- **Rate limits** — requests per minute (RPM) / tokens per minute (TPM). Exceed them → `429`.
- **Cost** — paid tiers bill **per token** (input + output). Even on free tiers, tokens = your budget.

## Staying under rate limits
| Technique | What it does |
|-----------|--------------|
| Retry with backoff (module 03) | survive an occasional `429` |
| Small delay between calls | avoid bursts in a loop |
| Batch where possible | fewer, bigger calls |
| Cache repeated prompts | don't pay twice for the same answer |

## Estimating cost
Cost ≈ `(input_tokens × input_price) + (output_tokens × output_price)`. You already know how to count
tokens (Day 9), so you can estimate **before** sending and log **after**.

```python
def estimate_cost(in_tokens, out_tokens, in_price_per_1k, out_price_per_1k):
    return (in_tokens / 1000) * in_price_per_1k + (out_tokens / 1000) * out_price_per_1k
```

## Habits that save money (and limits)
- Keep prompts **tight** — every word is tokens.
- Use **flash/small** models for routine work (Day 9).
- Don't resend giant context every turn — that's what **RAG** (Phase 2) fixes.
- **Log token usage** (`response.usage_metadata`) so surprises show up early.

The script estimates cost for a sample call (standard library).

```bash
python cost_estimate.py
```

➡ Next: [05-streaming-responses](../05-streaming-responses/)
