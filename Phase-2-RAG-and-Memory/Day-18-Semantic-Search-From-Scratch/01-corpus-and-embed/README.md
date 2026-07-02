# 01 — The Corpus: Embed Everything Once

A **corpus** is just "all the documents you want to search" — your notes, an FAQ list, the pages of a
textbook. Step one of every search engine is to turn that whole corpus into vectors **one time** and
keep them.

## The key idea: embed once, reuse forever
Embedding costs time (the model has to run). You do **not** want to re-embed your 10,000 notes every
time someone types a query. So:

1. **Once**, up front: embed every document → store the vectors.
2. **Per query**, cheaply: embed *only* the query and compare it to the stored vectors.

Today everything lives in memory and we re-embed on each run (the corpus is tiny). Tomorrow's vector
database is exactly this idea made **permanent** — embed once, save to disk, never redo it.

## One call embeds the whole list
`model.encode` takes a **list** of strings and hands back a **matrix** — one row per document:

```python
docs = ["buy milk", "fix the bike", "submit assignment"]
vectors = model.encode(docs)      # shape (3, 384): 3 rows, 384 numbers each
```

| Thing | Shape | Meaning |
|-------|-------|---------|
| one document | `(384,)` | a single point in 384-D space |
| the whole corpus | `(N, 384)` | `N` points stacked into a matrix — **row `i` is `docs[i]`** |

That `(N, 384)` matrix **is** your searchable knowledge base. Hold onto it.

## Why a matrix (not a list of vectors)?
Because numpy can compare a query against **all `N` rows at once** with a single operation — no Python
`for` loop. We cash in on that in module 02. Keeping the embeddings as one array is what makes that
possible.

`embed_corpus.py` embeds a small corpus, prints the matrix shape, and confirms each row lines up with
its document.

Run it:
```bash
python embed_corpus.py
```

➡ Next: [02-query-and-score](../02-query-and-score/) — score the whole corpus against a query at once.
