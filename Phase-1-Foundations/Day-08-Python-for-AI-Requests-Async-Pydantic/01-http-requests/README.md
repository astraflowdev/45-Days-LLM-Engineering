# 01 — Talking to APIs with `requests`

Every LLM you'll use — Gemini, Groq, an Ollama server — is a **web server**. Your code sends it an
**HTTP request** and reads back a **response**. The `requests` library is the friendly standard way
to do that in Python.

## The two verbs you'll use most
| Method | Meaning | Typical use |
|--------|---------|-------------|
| `GET` | "give me data" | fetch a page, read a record |
| `POST` | "here's data, do something" | **send a prompt to an LLM** |

## The response object
A response has three parts you care about:
- **`.status_code`** — `200` OK, `401` bad key, `429` rate-limited, `500` server error
- **`.json()`** — parses a JSON body into a Python `dict`
- **`.text`** — the raw body as a string

```python
import requests

r = requests.get("https://api.github.com")
print(r.status_code)        # 200
data = r.json()             # dict
print(data["current_user_url"])
```

## The mistake to avoid
`requests` does **not** raise an error for a `401`/`429`/`500` — your code sails on and crashes
later trying to read an error body. Always check:

```python
r.raise_for_status()   # turns 4xx/5xx into a clear exception
```

Run the example:

```bash
python http_requests.py
```

➡ Next: [02-async-basics](../02-async-basics/)
