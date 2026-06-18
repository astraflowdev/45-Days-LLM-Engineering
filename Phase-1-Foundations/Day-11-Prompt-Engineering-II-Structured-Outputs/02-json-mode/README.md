# 02 — JSON Mode

Asking nicely for JSON works *most* of the time — but the model might wrap it in ```` ```json ````
fences or add a "Here you go:" line, which breaks `json.loads`. **JSON mode** forces a clean,
parseable JSON response.

## Turn it on in Gemini
Set `response_mime_type` to `application/json` in the generation config:

```python
model = genai.GenerativeModel(
    "gemini-2.0-flash",
    generation_config={"response_mime_type": "application/json"},
)
resp = model.generate_content("Extract name and age from: Aarav is 21.")
import json
data = json.loads(resp.text)        # clean JSON -> no fences, no preamble
```

## Even better: give it a schema
You can also pass a **`response_schema`** so the model matches an exact shape (field names + types):

```python
generation_config={
    "response_mime_type": "application/json",
    "response_schema": Person,        # a Pydantic model or typed schema
}
```

| Approach | Reliability |
|----------|-------------|
| "Please return JSON" | okay — may add fences/preamble |
| `response_mime_type=application/json` | clean JSON string |
| + `response_schema` | clean JSON **in your exact shape** |

> JSON mode guarantees **valid JSON**, not **correct values** — you still validate (next module).

```bash
python json_mode.py
```

➡ Next: [03-pydantic-with-llm](../03-pydantic-with-llm/)
