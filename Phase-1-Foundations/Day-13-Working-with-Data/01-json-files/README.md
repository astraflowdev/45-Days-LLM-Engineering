# 01 — JSON Files

JSON is the lingua franca of APIs and LLM output. Python's built-in **`json`** module converts
between JSON text and Python objects — no install needed.

| Function | Direction | Use |
|----------|-----------|-----|
| `json.loads(s)` | string → object | parse an API/LLM reply |
| `json.dumps(obj)` | object → string | build a request body, log data |
| `json.load(f)` | file → object | read a `.json` file |
| `json.dump(obj, f)` | object → file | save data to a `.json` file |

```python
import json

data = {"name": "Aarav", "skills": ["python", "ai"]}
json.dump(data, open("profile.json", "w"), indent=2)   # save
loaded = json.load(open("profile.json"))               # read back
```

## Handy options
- `indent=2` → pretty, human-readable output.
- `ensure_ascii=False` → keep non-ASCII characters as-is (e.g. Hindi) instead of `\uXXXX`.

## Gotcha
JSON keys are always **strings**, and JSON has no tuples or `datetime` — only objects, arrays,
strings, numbers, booleans, and null. Convert dates to strings before dumping.

```bash
python json_basics.py
```

➡ Next: [02-csv-files](../02-csv-files/)
