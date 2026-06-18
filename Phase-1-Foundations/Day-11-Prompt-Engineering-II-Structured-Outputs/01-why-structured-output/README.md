# 01 — Why Structured Output

Ask a model "extract the name and age" and you might get:

```text
Sure! The person's name is Aarav and they are 21 years old.
```

That's friendly — and useless to code. You can't reliably `data["age"]` your way out of a sentence.
What you want is:

```json
{"name": "Aarav", "age": 21}
```

Now your program can use it: save to a database, call another API, show it in a UI.

## Where structured output is essential
| Feature | Needs structured data |
|---------|-----------------------|
| Extract fields from a document | name, date, amount → DB row |
| Classify with metadata | `{label, confidence}` |
| Tool/function calling (Phase 3) | the model must output exact arguments |
| Anything machine-readable | JSON, every time |

## The two-part recipe
1. **Ask** for JSON and describe the exact shape (ideally with a schema).
2. **Validate** the response into a Pydantic model — so bad data fails loudly, not silently.

This module is concept-only; the script shows the "prose vs JSON" contrast with plain Python.

```bash
python prose_vs_json.py
```

➡ Next: [02-json-mode](../02-json-mode/)
