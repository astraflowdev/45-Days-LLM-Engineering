# 04 — Type Hints: Telling Python What You Mean

Python doesn't *force* you to declare types, but **type hints** let you write them down anyway:

```python
name: str = "Aarav"
age: int = 21

def greet(name: str, times: int) -> str:
    return f"Hi {name}! " * times
```

They don't change how the code runs — Python ignores them at runtime — but they pay off big:

| Benefit | Why it helps |
|---------|--------------|
| Readability | `def embed(text: str) -> list[float]` tells you everything at a glance |
| Editor help | autocomplete + red squiggles when you pass the wrong type |
| **Pydantic** | the next module *uses* type hints to validate data automatically |

## The common ones
```python
x: int
name: str
price: float
ok: bool
tags: list[str]            # a list of strings
scores: dict[str, int]     # keys are str, values are int
from typing import Optional
nickname: Optional[str]    # a str OR None
```

## Gotcha
Hints are **not enforced** at runtime — `age: int = "twenty"` won't raise on its own. That's exactly
why **Pydantic** (next) exists: it reads your hints and *actually checks* the data.

Run the example:

```bash
python type_hints.py
```

➡ Next: [05-pydantic](../05-pydantic/)
