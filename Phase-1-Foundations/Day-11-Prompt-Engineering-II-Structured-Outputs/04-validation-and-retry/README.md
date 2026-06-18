# 04 — Validation & Retry

Even with JSON mode, a model can occasionally return data that's valid JSON but **wrong** — a missing
field, a string where you need a number, an out-of-range value. Production code plans for that:
**validate, and if it fails, retry.**

## The loop
```text
1. Ask the model for JSON.
2. Try to validate it into your Pydantic model.
3. If it validates -> done.
4. If it raises -> send the error back and ask it to fix, up to N times.
5. Still failing after N tries -> raise / log, don't ship bad data.
```

```python
for attempt in range(3):
    resp = model.generate_content(prompt)
    try:
        return Product.model_validate_json(resp.text)   # parse + validate in one step
    except ValidationError as err:
        prompt = base_prompt + f"\nYour last answer was invalid: {err}. Return corrected JSON."
raise RuntimeError("Model failed to produce valid output after 3 tries.")
```

## Why this matters
| Without retry | With retry |
|---------------|------------|
| one bad reply crashes the feature | a transient slip self-corrects |
| bad data reaches your DB/UI | only validated data passes |

## Handy Pydantic helper
`Product.model_validate_json(text)` parses a JSON **string** and validates in one call — no separate
`json.loads`.

> Guarantee **valid JSON** with JSON mode; guarantee **correct data** with validation + retry.

```bash
python validate_and_retry.py
```

➡ Next: practise in [../exercises/](../exercises/)
