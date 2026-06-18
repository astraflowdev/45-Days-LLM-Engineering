# Day 08 — Python for AI: Requests, Async, Dotenv, Type Hints & Pydantic

The Python week (Days 1–7) gave you the language. Today you pick up the **five engineering habits**
every AI app in this course relies on — *before* we call our first LLM tomorrow (Day 9).

## Learning objectives
By the end of today you can:
- Call a web API with **`requests`** and read JSON responses
- Understand **async** (`async`/`await`) and run things concurrently
- Keep API keys safe with a **`.env`** file and **`python-dotenv`**
- Write **type hints** that make code (and tools) understand your data
- Model and **validate** data with **Pydantic** — the backbone of structured LLM output

## Modules (work through them in order)

| # | Module | What it covers |
|--:|--------|----------------|
| 01 | [http-requests](01-http-requests/) | `requests`: GET/POST, status codes, JSON, headers |
| 02 | [async-basics](02-async-basics/) | `async`/`await`, `asyncio`, running calls concurrently |
| 03 | [dotenv-and-secrets](03-dotenv-and-secrets/) | `.env` + `python-dotenv`; never hardcode a key |
| 04 | [type-hints](04-type-hints/) | Annotating variables and functions; why it matters |
| 05 | [pydantic](05-pydantic/) | `BaseModel`, validation, parsing JSON into objects |

Then practise in **[exercises/](exercises/)**.

## Setup
```bash
pip install -r requirements.txt   # adds requests, httpx, pydantic, python-dotenv
```
Module 01 needs internet (it calls a free public API). Modules 02 and 04 run offline.

## How to run
```bash
python 01-http-requests/http_requests.py
python 02-async-basics/async_basics.py
```

## Today's exercise
**Validate a user profile** with Pydantic, and **fetch + parse** live data from a public API.
See [`exercises/`](exercises/).

➡ Next (Day 9): your **first Gemini API call** — tokens, context windows, temperature.
