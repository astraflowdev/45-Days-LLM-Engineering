# 04 — Cosine Similarity (The Closeness Formula, by Hand)

Module 03 let the library score similarity. Now you'll compute that score yourself — it's a short
formula — so that tomorrow, when we store and retrieve vectors with Chroma, there's no black box left.

## Why not just distance?
Module 01 used straight-line **distance**. For text embeddings we prefer **cosine similarity**, which
measures the **angle** between two vectors, ignoring their length. Two sentences about the same topic
point the **same direction** even if one is longer; cosine catches that, distance can get fooled by
length.

## The formula
For two vectors **a** and **b**:

```
cosine_similarity(a, b) = (a . b) / (||a|| * ||b||)
```

- `a . b` — the **dot product**: multiply matching elements, add them up (`a1*b1 + a2*b2 + ...`).
- `||a||` — the **norm** (length) of `a`: `sqrt(a1^2 + a2^2 + ...)`.

The result runs from **-1 to 1**:

| Score | Meaning |
|------:|---------|
| `+1.0` | same direction — as similar as it gets |
| `0.0`  | unrelated (perpendicular) |
| `-1.0` | opposite |

In practice, for this model you'll see roughly **0.3–0.9** for related text and near **0** for
unrelated text.

## In numpy it's three lines
```python
import numpy as np

def cosine(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
```

`np.dot` does the multiply-and-sum; `np.linalg.norm` does the `sqrt(sum of squares)`. `cosine.py`
defines this, runs it on real embeddings, and checks it **matches** the library's `util.cos_sim` —
so you can trust your own version.

## Shortcut for unit vectors
Module 02 noted this model returns **unit-length** vectors (`||a|| = 1`). When that's true the
denominator is `1 * 1 = 1`, so **cosine = just the dot product**. That's why fast vector databases
pre-normalize everything and then only need a dot product. We'll lean on this next week.

Run it:
```bash
python cosine.py
```

➡ Next: [05-gemini-embeddings](../05-gemini-embeddings/) — the same idea from a cloud API (optional).
