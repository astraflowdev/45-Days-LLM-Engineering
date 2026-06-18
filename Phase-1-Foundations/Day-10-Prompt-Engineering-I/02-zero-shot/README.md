# 02 — Zero-Shot Prompting

**Zero-shot** = you just ask, giving **no examples**. The model relies entirely on what it learned in
training.

```python
model.generate_content("Classify this review as positive or negative: 'The food was cold.'")
```

It works surprisingly often for common tasks (summarize, translate, classify, explain).

## When zero-shot is enough
- Common, well-known tasks
- You don't need a strict output format
- The wording is clear and specific

## When it falls short
| Problem | Symptom |
|---------|---------|
| Ambiguous task | model guesses what you meant |
| Specific format needed | output style drifts each call |
| Niche/edge cases | inconsistent or wrong answers |

The fix for all three is usually **examples** — that's **few-shot** (next module).

## Make zero-shot better (without examples)
- **Be specific:** say the exact output you want ("Reply with one word: positive or negative").
- **Constrain length/format:** "in 3 bullet points", "as a JSON list".
- **Give context:** who's it for, what's the goal.

```bash
python zero_shot.py
```

➡ Next: [03-few-shot](../03-few-shot/)
