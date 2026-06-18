# 01 — Architecture

A small app, but a real one. Keep it in **three layers** so it stays clean and testable.

## Data flow
```
            ┌─────────────┐
  PDF  ───▶ │             │
  URL  ───▶ │  loaders.py │ ──▶ clean text ──▶ ┌───────────────┐ ──▶ Summary ──▶ ┌────────┐
  Text ───▶ │             │                    │ summarizer.py │   (Pydantic)    │ app.py │ ──▶ UI
            └─────────────┘                    │  Gemini+JSON  │                 └────────┘
                                               └───────────────┘
```

## The three layers
| File | Responsibility | Knows about |
|------|----------------|-------------|
| `loaders.py` | turn any input into clean text | PDFs, HTTP, cleaning |
| `summarizer.py` | text → validated `Summary` | Gemini, JSON mode, Pydantic, retries |
| `app.py` | UI: collect input, show output | Streamlit only |

Each layer has **one job** and doesn't reach into the others' details. `app.py` never calls Gemini
directly — it calls `summarize(text)`. That separation is exactly the multi-provider lesson (Day 12):
the UI doesn't care *how* the summary is made.

## The output shape
```python
class Summary(BaseModel):
    tldr: str
    key_points: list[str]
    action_items: list[str]
```
Structured output (Day 11) means the UI can render each part cleanly instead of parsing prose.

## Why this scales into Phase 2
Swap `loaders.py` for a **retriever** and `summarizer.py` for a **RAG chain**, and the same `app.py`
becomes a Document Q&A app — which is literally Project 2. Good layering pays off.

➡ Back to the [project README](../) · then build the [`app/`](../app/).
