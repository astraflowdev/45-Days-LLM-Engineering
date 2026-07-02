# Day 17 — Embeddings Fundamentals (Text → Vectors)

Yesterday your chatbot remembered a conversation. But how would it find *the right note* out of
10,000 notes when none of them share the exact words you typed? Keyword search can't — it only
matches letters. **Embeddings** let a computer match **meaning**.

An **embedding** turns a piece of text into a list of numbers (a **vector**) so that texts with
similar meaning land **close together** in space. That single idea is the engine of this entire
phase: search, RAG, document Q&A — all of it is "embed everything, then find the nearest vectors."

We build the intuition in **5 steps**, starting with no libraries at all, then using a real, free,
**local** embedding model.

## Learning objectives
By the end of today you can:
- Explain what an embedding **is** and why "similar meaning ⇒ nearby vector" matters
- Generate real embeddings locally with **`sentence-transformers`** (free, no API key)
- Read an embedding's **shape** (e.g. 384 numbers) and understand what it represents
- Measure how close two vectors are with **cosine similarity**
- Rank texts by meaning — keyword overlap *not* required
- (Optional) Get embeddings from the **Gemini** cloud API

## Modules (work through them in order)

| # | Module | What it teaches | The "aha" |
|--:|--------|-----------------|-----------|
| 01 | [what-is-an-embedding](01-what-is-an-embedding/) | Meaning as coordinates (tiny 2-D vectors, no libraries) | A vector is just a *point* |
| 02 | [first-embedding](02-first-embedding/) | Real model: text → 384 numbers | Meaning fits in a list of floats |
| 03 | [similar-vs-different](03-similar-vs-different/) | Rank sentences by meaning | "car" ≈ "automobile" with **zero** shared letters |
| 04 | [cosine-similarity](04-cosine-similarity/) | The closeness formula, by hand with numpy | One number = how alike two texts are |
| 05 | [gemini-embeddings](05-gemini-embeddings/) | Optional cloud embeddings | Same idea, different provider |

Then practise in **[exercises/](exercises/)**.

> 🖥️ **Visual walkthrough:** open **[`presentation/index.html`](presentation/)** — a beginner-friendly
> slide deck (with diagrams) that explains every concept on this page. Great for the live session.

## Provider: local `sentence-transformers` (free, no key)
Our default is the **`all-MiniLM-L6-v2`** model: tiny (~90 MB), fast, runs **on your laptop**, and
costs nothing. No API key. The **first run downloads the model** (one-time), then it's offline.
Module 05 shows the optional **Gemini** cloud alternative.

## Setup
```bash
pip install -r requirements.txt        # needs: numpy, sentence-transformers
```
> First run of a `sentence-transformers` script downloads the model once (~90 MB) — give it a
> minute. After that it loads from disk instantly.

> **Windows: `import torch` fails with `WinError 1114` / `c10.dll`?**
> PyTorch needs the **Microsoft Visual C++ 2015–2022 x64 Redistributable** (it provides
> `vcruntime140_1.dll`). Install it once from <https://aka.ms/vs/17/release/vc_redist.x64.exe>,
> then re-run. This is the most common first-time error on a fresh Windows Python.

## How to run
```bash
python 01-what-is-an-embedding/coordinates.py    # no install needed for module 01
python 02-first-embedding/first_embedding.py     # downloads the model on first run
```

## Today's exercise
Build a tiny **semantic search** ("find the most similar note") and an **odd-one-out** finder using
the embeddings + cosine similarity you learned today. See [`exercises/`](exercises/).

> Today you embed text and measure closeness by hand. **Day 18** stores those vectors in a real
> database (**Chroma**), retrieves the nearest notes, and feeds the results into an AI chat loop.

➡ Next (Day 18): Chroma vector DB — save vectors, retrieve them, and chat with AI.
