# 04 — The Mini Search Engine (a reusable class)

You now have all the pieces: embed a corpus, score a query, take the top-k. This module **packages**
them into one tidy object you can reuse anywhere — a real (tiny) search engine.

## Why a class?
Because a search engine has **state** (the documents + their embeddings) and **behaviour** (add docs,
search them). That's exactly what a class is for. Two methods are all we need:

| Method | Does |
|--------|------|
| `.add(documents)` | embed new documents and remember them (build the index) |
| `.search(query, k)` | embed the query, score everything, return the top-k |

```python
engine = SemanticSearch()
engine.add(["buy milk", "fix the bike", "submit the assignment"])
engine.search("repair my cycle", k=2)     # -> [(0.41, "fix the bike"), ...]
```

That `add` / `search` shape is the **same interface** Chroma gives you tomorrow (`collection.add` /
`collection.query`). You're learning the real API by building a baby version of it.

## What's happening inside
- `add` calls `model.encode(documents)`, normalizes the rows, and **stacks** them onto whatever it
  already stored (`np.vstack`) — so you can add docs in batches.
- `search` reuses the stored matrix: it only has to embed the **one** query, then it's a single
  matrix-vector multiply + a top-k. The expensive embedding of the corpus already happened in `add`.

That split — **pay once in `add`, stay cheap in `search`** — is the whole point of building an index.

## Try it live
`search_engine.py` loads a slightly bigger corpus, then drops you into a prompt where you type
queries and watch the ranked results. Try things the corpus never says word-for-word:

- `how do I get to campus cheaply?`
- `I'm hungry, what can I make?`
- `when is my homework due?`

Run it:
```bash
python search_engine.py        # type a query, press Enter; Ctrl+C (or 'quit') to exit
```

➡ Next: [05-why-this-matters](../05-why-this-matters/) — this is RAG retrieval; where it breaks, and
why tomorrow we switch to a vector database.
