# 01 — Save Vectors to Chroma

This is the first time your embeddings become a database, not just a variable in RAM.

## The key move
You still create embeddings with the same local model from Day 17. The difference is what happens
next:

1. Embed the notes
2. Give Chroma the `ids`, `documents`, `metadatas`, and `embeddings`
3. Let Chroma persist them on disk

```python
collection.upsert(
    ids=["note-1", "note-2"],
    documents=["Use a queue for BFS", "Binary search needs sorted data"],
    embeddings=[[...], [...]],
)
```

## Why this matters
Without a vector DB, your notes disappear every time the script exits. With Chroma:

- the collection survives between runs
- you can keep adding documents later
- retrieval becomes a clean database query instead of hand-rolled array code

`store_vectors.py` creates a persistent database folder, embeds a few notes, and upserts them into a
collection named `student_notes`.

Run it:
```bash
python store_vectors.py
```

➡ Next: [02-persist-and-reload](../02-persist-and-reload/) — close the script, re-open the DB, and
prove the vectors are still there.
