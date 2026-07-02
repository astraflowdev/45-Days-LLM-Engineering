# 05 — Why This Matters

Today is the first day the RAG stack feels like a real application instead of a math demo.

## What changed
You already knew how to make vectors. The missing part was a place to store, organize, and retrieve
them cleanly. Chroma gives you that.

| Without a vector DB | With Chroma |
|---------------------|-------------|
| vectors disappear after the script ends | vectors persist on disk |
| you manage arrays and indexes manually | collections manage the stored records |
| retrieval code is custom every time | `collection.query(...)` is reusable |
| metadata is awkward | metadata lives beside each document |
| chat has no grounding | retrieval gives the model relevant context |

## This is already RAG
The loop you wrote today is the foundation of document Q&A:

```text
documents -> embeddings -> Chroma -> retrieve top chunks -> LLM answer
```

Later days will improve each box:

- better chunking
- filtering and metadata
- cloud vector storage
- re-ranking
- citations

But the shape stays the same.

`recap.py` prints a short offline recap of the pipeline and the practical reasons vector databases
exist.

Run it:
```bash
python recap.py
```

➡ Next: practise in [../exercises/](../exercises/), then move to Day 19 — pgvector via Supabase.
