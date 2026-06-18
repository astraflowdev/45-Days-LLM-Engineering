# Day 09 — LLM Fundamentals & Your First Gemini Call

Yesterday you set up the engineering habits. Today you actually **call an LLM** — and learn the four
ideas you must understand to use one well: **tokens, context windows, sampling (temperature/top-p),
and model families**.

## Learning objectives
By the end of today you can:
- Make a real **Gemini API call** from Python (free tier)
- Explain what **tokens** are and count them
- Reason about **context windows** (how much text fits)
- Control creativity with **temperature** and **top-p**
- Pick the right **model** (flash vs pro; hosted vs local)

## Modules (work through them in order)

| # | Module | What it covers |
|--:|--------|----------------|
| 01 | [first-gemini-call](01-first-gemini-call/) | Your first real LLM call with `google-generativeai` |
| 02 | [tokens-and-tokenization](02-tokens-and-tokenization/) | What tokens are; counting them |
| 03 | [context-windows](03-context-windows/) | How much text fits; the prompt + answer budget |
| 04 | [temperature-and-sampling](04-temperature-and-sampling/) | Temperature & top-p: control randomness |
| 05 | [model-families](05-model-families/) | Flash vs Pro; Gemini / Groq / Ollama |

Then practise in **[exercises/](exercises/)**.

## Setup
```bash
pip install -r requirements.txt
```
Get a **free** key at [Google AI Studio](https://aistudio.google.com/apikey) and put it in a `.env`:
```bash
# .env  (never commit this)
GEMINI_API_KEY=your_key_here
```

## How to run
```bash
python 01-first-gemini-call/first_call.py
```

## Today's exercise
Build a **command-line chatbot** and a **temperature explorer**. See [`exercises/`](exercises/).

➡ Next (Day 10): Prompt engineering I — system prompts, zero-shot, few-shot, chain-of-thought.
