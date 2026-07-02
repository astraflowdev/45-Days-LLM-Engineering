# 02 — Score the Whole Corpus Against a Query (at once)

You have the corpus matrix (`N x 384`). A user types a query. Now: **how similar is the query to each
document?** Yesterday you scored *two* vectors. Today you score the query against **all `N` rows in
one shot.**

## The slow way (a loop) — fine, but we can do better
You *could* loop:

```python
scores = []
for row in corpus_vectors:            # N times
    scores.append(cosine(query_vec, row))
```

That works, but it's a Python loop — slow once `N` is large. numpy can do the same thing in one
vectorized step.

## The fast way: one matrix-times-vector
Cosine similarity is `(a . b) / (||a|| * ||b||)`. The dot product of the query against **every** row
at once is just a **matrix-vector multiply**:

```python
import numpy as np

# normalize so every vector has length 1  ->  then cosine is just the dot product
corpus_unit = corpus_vectors / np.linalg.norm(corpus_vectors, axis=1, keepdims=True)
query_unit  = query_vec / np.linalg.norm(query_vec)

scores = corpus_unit @ query_unit      # shape (N,): one score per document
```

`@` is matrix multiplication. `(N, 384) @ (384,)` → `(N,)` — **one number per document**, all
computed together. No loop.

### Why divide by the norms first?
Cosine ignores length; it only cares about **direction**. Dividing each vector by its own length
(`np.linalg.norm`) makes every vector unit-length, and for unit vectors **cosine = dot product**
(the denominator becomes `1 * 1`). So normalize once, then a plain dot product gives cosine.

> This model already returns near-unit-length vectors (you saw `||a|| ~ 1.0` yesterday), so the
> normalize step barely changes the numbers — but doing it explicitly keeps the math correct for
> *any* embeddings, and it's exactly the trick real vector DBs use.

## `axis` and `keepdims`, briefly
- `axis=1` → "compute the norm of **each row**" (one length per document), giving shape `(N, 1)`.
- `keepdims=True` keeps that as a column so it **broadcasts** cleanly when we divide the `(N, 384)`
  matrix by it.

`score.py` embeds the corpus and a query, scores every document with that one-liner, and prints each
note with its score so you can see meaning win over keywords.

Run it:
```bash
python score.py
```

➡ Next: [03-top-k-results](../03-top-k-results/) — turn these scores into a ranked top-k answer.
