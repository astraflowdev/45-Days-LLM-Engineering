# 03 — Top-k: From Scores to a Ranked Answer

Module 02 gave you a score for every document. A search engine doesn't dump all scores at the user —
it returns **the best few, in order**. That's the **top-k**.

## Sorting the scores
You have `scores`, one number per document. You want the **indices** of the highest ones so you can
look the documents back up. numpy gives you two tools:

```python
order = np.argsort(scores)[::-1]    # indices, lowest->highest, then reversed = highest first
top_k = order[:k]                   # the k best indices
```

`argsort` returns **positions**, not values — exactly what you need to map a score back to its
document (`CORPUS[i]`). `[::-1]` reverses to best-first, then `[:k]` keeps the top `k`.

| Call | Returns | Use it for |
|------|---------|------------|
| `np.argsort(scores)` | indices that sort low→high | ranking; reverse for high→low |
| `np.argmax(scores)` | index of the single best | when `k == 1` |

## A faster cousin: `argpartition`
Sorting orders **all** `N` documents even though you only want the top `k`. For big corpora,
`np.argpartition` finds the top `k` without fully sorting the rest — cheaper when `N` is huge and `k`
is small:

```python
top_unsorted = np.argpartition(scores, -k)[-k:]      # the k best, in any order
top_k = top_unsorted[np.argsort(scores[top_unsorted])[::-1]]   # then sort just those k
```

For five notes it makes no difference; we mention it because it's the trick that keeps "top-k" fast,
and it's a stepping stone toward the **approximate nearest neighbor** indexes real vector DBs use.

## Returning results cleanly
`top_k.py` wraps this into a `search(query, k)` that returns a list of `(score, document)` pairs,
best first — the shape every search API gives you.

Run it:
```bash
python top_k.py
```

➡ Next: [04-mini-search-engine](../04-mini-search-engine/) — wrap all of this into a reusable class.
