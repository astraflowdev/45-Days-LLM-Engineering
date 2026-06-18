# Day 10 — Prompt Engineering I

The model is fixed; your **prompt** is the steering wheel. Today is the highest-leverage skill in the
whole course: writing prompts that get reliable results — **system prompts, zero-shot, few-shot, and
chain-of-thought**.

## Learning objectives
By the end of today you can:
- Set behaviour with a **system prompt** vs the **user prompt**
- Use **zero-shot** prompts and know their limits
- Steer format and style with **few-shot** examples
- Improve reasoning with **chain-of-thought**
- Structure prompts clearly (roles, delimiters, specificity)

## Modules (work through them in order)

| # | Module | What it covers |
|--:|--------|----------------|
| 01 | [system-vs-user-prompts](01-system-vs-user-prompts/) | Set the model's role/rules vs the task |
| 02 | [zero-shot](02-zero-shot/) | Just ask — no examples |
| 03 | [few-shot](03-few-shot/) | Show 2–5 examples to lock format/style |
| 04 | [chain-of-thought](04-chain-of-thought/) | "Think step by step" for harder problems |
| 05 | [prompt-structure](05-prompt-structure/) | Delimiters, specificity, the anatomy of a good prompt |

Then practise in **[exercises/](exercises/)**.

## Setup
```bash
pip install -r requirements.txt        # google-generativeai, python-dotenv
# GEMINI_API_KEY=... in a .env file
```

## How to run
```bash
python 03-few-shot/few_shot.py
```

## Today's exercise
Write a **review-sentiment classifier** with few-shot, and a **word-problem solver** with
chain-of-thought. See [`exercises/`](exercises/).

➡ Next (Day 11): Prompt engineering II — structured outputs with Pydantic and JSON mode.
