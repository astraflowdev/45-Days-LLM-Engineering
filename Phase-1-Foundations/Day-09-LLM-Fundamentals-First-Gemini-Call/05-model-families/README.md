# 05 — Model Families: Which One, and Where It Runs

"An LLM" isn't one thing. You'll choose between **sizes**, **providers**, and **hosted vs local**.
For this course, all picks are **free**.

## Size: speed vs smarts (within one provider)
| Tier | Example (Gemini) | Good for |
|------|------------------|----------|
| Flash / small | `gemini-2.0-flash` | most tasks: fast, cheap, free |
| Pro / large | `gemini-2.5-pro` | hard reasoning, long/complex work |

Start with **flash**. Reach for **pro** only when flash isn't good enough — it's slower and costlier.

## Providers we use (all free)
| Provider | What it is | Why use it |
|----------|------------|------------|
| **Gemini** | Google's hosted models | our default; generous free tier |
| **Groq** | super-fast hosted open models (Llama, etc.) | speed; a second opinion |
| **Ollama** | runs open models **on your laptop** | offline, private, no key, no limits |
| **Hugging Face** | hosted inference for open models | huge model zoo |

## Hosted vs local
- **Hosted (Gemini, Groq, HF):** strong quality, nothing to install, needs internet + a key,
  has rate limits.
- **Local (Ollama):** private and unlimited, but quality/speed depend on your hardware.

## The takeaway
> Default to **Gemini flash**. Switch providers/sizes for speed, privacy, or quality —
> and on **Day 12** you'll hide all of them behind **one interface** so swapping is trivial.

This module is concept-only — there's a tiny script that prints a decision cheat-sheet.

```bash
python model_cheatsheet.py
```

➡ Next: practise in [../exercises/](../exercises/)
