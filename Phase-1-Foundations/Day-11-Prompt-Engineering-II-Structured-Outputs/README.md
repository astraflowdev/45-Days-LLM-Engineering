# Day 11 — Prompt Engineering II: Structured Outputs

Free-text answers are great for humans, terrible for **code**. Today you make the model return
**clean JSON** that you validate into **Pydantic** objects — the bridge from "chatbot" to "software".

## Learning objectives
By the end of today you can:
- Explain why **structured output** matters for real apps
- Force **JSON** with Gemini's JSON mode + a schema
- Parse model JSON into **Pydantic** objects
- **Validate and retry** when the model returns something wrong

## Modules (work through them in order)

| # | Module | What it covers |
|--:|--------|----------------|
| 01 | [why-structured-output](01-why-structured-output/) | Why apps need JSON, not prose |
| 02 | [json-mode](02-json-mode/) | Gemini `response_mime_type` + `response_schema` |
| 03 | [pydantic-with-llm](03-pydantic-with-llm/) | Validate model JSON into typed objects |
| 04 | [validation-and-retry](04-validation-and-retry/) | Catch bad output and retry cleanly |

Then practise in **[exercises/](exercises/)**.

## Setup
```bash
pip install -r requirements.txt        # google-generativeai, pydantic, python-dotenv
# GEMINI_API_KEY=... in a .env file
```

## How to run
```bash
python 03-pydantic-with-llm/extract_to_pydantic.py
```

## Today's exercise
Build a **resume parser** that extracts a structured profile, and a **product extractor** that
validates and retries. See [`exercises/`](exercises/).

➡ Next (Day 12): multi-provider patterns — one interface over Gemini, Groq, and Ollama.
