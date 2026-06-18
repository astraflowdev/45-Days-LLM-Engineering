# 05 — Pydantic: Data That Validates Itself

LLMs return messy text. You want **clean, checked objects**. **Pydantic** reads your type hints and
*enforces* them — it's the tool you'll use all course to turn a model's JSON reply into trustworthy
Python data.

## Define a shape, get validation for free
```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    email: str

u = User(name="Aarav", age=21, email="aarav@example.com")
print(u.age)            # 21  (a real int)
```

If the data is wrong, Pydantic **raises a clear error** instead of letting bad data through:
```python
User(name="Aarav", age="not-a-number", email="x")   # ValidationError: age must be an int
```

## Why this is the backbone of LLM apps
| You do this | Pydantic gives you |
|-------------|--------------------|
| Define the output shape you want | a schema the model can follow |
| Feed in the model's JSON | a validated object, or a clear error to retry on |
| Read `obj.field` | typed, autocompleted, safe access |

## Handy features
```python
from pydantic import BaseModel, Field

class Product(BaseModel):
    name: str
    price: float = Field(gt=0)          # must be > 0
    tags: list[str] = []                # default value

# Parse straight from a dict (e.g. parsed JSON):
p = Product(**{"name": "Pen", "price": 10})
print(p.model_dump())                    # back to a dict
```

## Type coercion (nice, but know it)
Pydantic will gently convert when it safely can: `age="21"` (string) becomes `21` (int). It only
errors when conversion is impossible (`age="twenty"`).

Run the example:

```bash
python pydantic_models.py
```

➡ Next: practise in [../exercises/](../exercises/)
