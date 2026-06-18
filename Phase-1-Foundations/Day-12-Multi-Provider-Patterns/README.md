# Day 12 — Multi-Provider Patterns

Don't marry one LLM provider. Gemini might be down, rate-limited, or just not the best fit for a
task. Today you wrap **Gemini, Groq, and Ollama** behind **one interface** so swapping is a single
line — resilient and flexible.

## Learning objectives
By the end of today you can:
- Explain why you shouldn't hardcode one provider
- Call **Gemini**, **Groq**, and **Ollama** (local)
- Build **one function** that talks to any of them
- Add a **fallback** so one provider failing doesn't break your app

## Modules (work through them in order)

| # | Module | What it covers |
|--:|--------|----------------|
| 01 | [the-provider-problem](01-the-provider-problem/) | Why a single hardcoded provider hurts |
| 02 | [gemini-provider](02-gemini-provider/) | A clean Gemini wrapper function |
| 03 | [groq-provider](03-groq-provider/) | Groq — fast hosted open models |
| 04 | [ollama-local](04-ollama-local/) | Ollama — models on your own machine |
| 05 | [one-interface](05-one-interface/) | One `ask()` over all three + fallback |

Then practise in **[exercises/](exercises/)**.

## Setup
```bash
pip install -r requirements.txt        # google-generativeai, groq, ollama, python-dotenv
# .env: GEMINI_API_KEY=...  and  GROQ_API_KEY=...   (both free)
# Ollama: install from ollama.com, then `ollama pull llama3.2`
```

## How to run
```bash
python 05-one-interface/ask.py
```

## Today's exercise
Build a **provider-switching CLI** that picks the backend from an env var, with a fallback chain.
See [`exercises/`](exercises/).

➡ Next (Day 13): working with data — JSON, CSV, PDF, and light scraping.
