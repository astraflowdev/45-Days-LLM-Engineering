# 03 — Pydantic + LLM: Validated Objects

JSON mode gives you a valid JSON **string**. The last step is turning it into a **typed, validated
Python object** — so the rest of your app works with real data, not a loose dict.

Remember Pydantic from Day 8? This is where it shines.

## The pattern
```python
import json
from pydantic import BaseModel

class Person(BaseModel):
    name: str
    age: int
    city: str

data = json.loads(response.text)     # dict from JSON mode
person = Person(**data)              # validated object  (raises if a field is wrong)
print(person.age + 1)               # a real int -> safe maths
```

If the model returns `"age": "twenty-one"`, Pydantic raises a clear `ValidationError` instead of
letting bad data sneak downstream.

## Why this combo is the backbone of AI apps
| Stage | Tool |
|-------|------|
| Force JSON | JSON mode (`response_mime_type`) |
| Define the shape | a Pydantic model |
| Guarantee correctness | Pydantic validation |

You define the model **once** and reuse it as the schema *and* the validator.

## Bonus: model as schema
Many SDKs (including Gemini) let you pass the Pydantic model **as** `response_schema`, so the field
names and types are enforced on the way out — then you still validate on the way in. Belt and braces.

```bash
python extract_to_pydantic.py
```

➡ Next: [04-validation-and-retry](../04-validation-and-retry/)
