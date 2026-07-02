# 02 — Persist and Reload

Storing vectors only matters if they are still there in the next script.

## Fresh client, same collection
Chroma persistence is simple:

```python
client = chromadb.PersistentClient(path="...")
collection = client.get_collection("student_notes")
```

If the path points at the same database folder, Chroma reloads the collection from disk. No new
embeddings are needed.

## What this module proves
`reload_collection.py`:

- opens a brand-new Chroma client
- reconnects to the `student_notes` collection
- prints the stored count
- shows the saved IDs and metadata

That is the big shift from yesterday's scripts. The knowledge base no longer lives only inside one
Python process.

Run it:
```bash
python reload_collection.py
```

➡ Next: [03-retrieve-best-matches](../03-retrieve-best-matches/) — ask the database for the nearest
notes.
