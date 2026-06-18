# Day 16 — Embeddings Fundamentals

Welcome to **Phase 2 — RAG & Memory**. Phase 1 got an LLM to *generate* text. Phase 2 is about
giving it *knowledge*: your notes, PDFs, a company's docs. The first building block — and the one
everything in RAG sits on — is the **embedding**: turning text into a list of numbers that
captures its meaning.

## Learning objectives
By the end of today you can:
- Explain what an embedding is and why "similar meaning → nearby vectors" powers search & RAG
- Generate embeddings **locally and free** with `sentence-transformers` (no API key)
- Generate embeddings with the **Gemini embeddings API** (free tier)
- Compare models by **dimensions**, understand **normalization**, and pick the right one

## Modules (work through them in order)

| # | Module | What it covers |
|--:|--------|----------------|
| 01 | [what-are-embeddings](01-what-are-embeddings/) | The core idea, with a tiny hand-made demo (no installs) |
| 02 | [your-first-embedding](02-your-first-embedding/) | Local, free embeddings with `sentence-transformers` (384-dim) |
| 03 | [gemini-embeddings](03-gemini-embeddings/) | Gemini embeddings API, free tier (768-dim) |
| 04 | [models-and-dimensions](04-models-and-dimensions/) | Dimensions, normalization, which model to use |

Then apply it in **[exercises/](exercises/)**.

## Setup
Module 01 runs on the **standard library** — nothing to install. Modules 02–04 and the exercises
need a couple of free packages (already in the repo's `requirements.txt`):

```bash
pip install -r requirements.txt
```

For module 03 you also need a **free** Gemini API key from
[Google AI Studio](https://aistudio.google.com/apikey). Put it in a `.env` file:

```bash
# .env  (never commit this file)
GEMINI_API_KEY=your_key_here
```

## How to run
From this folder, run any module's script directly:

```bash
python 01-what-are-embeddings/what_are_embeddings.py
python 02-your-first-embedding/first_embedding.py
```

> ℹ️ The first run of a `sentence-transformers` script downloads a small model (~90 MB) once,
> then works offline. It runs fine on a normal CPU laptop.

## Today's exercise
**Find the closest sentence** — use embeddings to match a question to the most relevant sentence
*by meaning, not keywords*. See [`exercises/`](exercises/).

➡ Next day (Day 17): semantic search **from scratch** — cosine similarity with NumPy, no library helper.
