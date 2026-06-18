# 04 — Models & Dimensions: Which One, and Why

You've now made embeddings two ways. They gave vectors of **different sizes** — 384 vs 768. This
module explains what that means and how to choose.

## Dimensions
The **dimension** is just how many numbers are in each vector. More dimensions can capture more
nuance, but cost more storage and compute. It is **not** "bigger = always better" — `all-MiniLM-L6-v2`
(384) is excellent for its size.

| Model | Dimensions | Runs where | Key? | Good for |
|-------|:----------:|------------|:----:|----------|
| `all-MiniLM-L6-v2` (sentence-transformers) | 384 | your CPU | no | offline, private, free, fast |
| Gemini `text-embedding-004` | 768 | Google's servers | yes | higher quality, scale, no local compute |

## The rule you must never break
> **You can only compare vectors from the *same* model.**

A MiniLM vector and a Gemini vector live in **different spaces** — comparing them is meaningless,
even if you padded them to the same length. Pick one model for a project and embed *everything*
(documents and queries) with that same model.

## Normalization
Most similarity math assumes vectors have **length 1** ("unit vectors"). Normalizing keeps a
vector's *direction* (its meaning) but scales its length to exactly `1.0`. With
`sentence-transformers` you get this for free:

```python
model.encode(text, normalize_embeddings=True)   # length becomes 1.0
```

The script shows a raw vector's length vs a normalized one.

```bash
python models_and_dimensions.py
```

## How to choose (rule of thumb)
- **Privacy / offline / no cost / small scale** → local `sentence-transformers`.
- **Best quality / big scale / no local compute** → a hosted API like Gemini.
- Either way: **be consistent** — same model for your docs and your questions.

➡ Next: practise in [../exercises/](../exercises/)
