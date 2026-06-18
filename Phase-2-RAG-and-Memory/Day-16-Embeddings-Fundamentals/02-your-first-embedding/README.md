# 02 — Your First Real Embedding (Local & Free)

Time to make a *real* embedding. We'll use **`sentence-transformers`**, a free library that runs a
small model **on your own machine** — no API key, works offline after the first download.

The model: **`all-MiniLM-L6-v2`**. It's tiny, fast, and turns any text into a **384-number** vector.

| Property | Value |
|----------|-------|
| Library | `sentence-transformers` (free, open-source) |
| Model | `all-MiniLM-L6-v2` |
| Output size | **384** dimensions |
| Runs on | your CPU (no GPU needed) |
| API key | none |

## Install (one time)
```bash
pip install sentence-transformers
```

> ℹ️ The **first** time you run it, it downloads the model (~90 MB) and caches it. Every run after
> that is offline and fast.

## What the code does
1. Load the model once.
2. Call `model.encode([...])` on a list of sentences.
3. Get back a NumPy array of shape `(number_of_sentences, 384)` — one 384-number vector per sentence.

```bash
python first_embedding.py
```

You'll see the shape `(3, 384)` and the first few numbers of a vector. Those numbers aren't
meaningful to *read* — what matters is that similar sentences get similar vectors (you'll use that
in the exercise).

## Gotcha
`encode("one string")` returns a single 1-D vector; `encode(["a", "list"])` returns a 2-D array
(one row per item). Pass a **list** when you have multiple texts — it's faster and gives you `.shape`.

➡ Next: [03-gemini-embeddings](../03-gemini-embeddings/)
