# 03 — Retrieve the Best Matches

Now the database does the search for you.

## The query shape
You embed the user's question once, then ask Chroma for the nearest rows:

```python
result = collection.query(
    query_embeddings=[query_vector],
    n_results=3,
)
```

Chroma returns parallel lists:

- `documents`
- `metadatas`
- `ids`
- `distances`

## Distance vs similarity
This lesson creates the collection with cosine distance. That means:

- smaller distance = closer match
- `similarity ~= 1 - distance`

You mostly care about the ranking, but showing both helps students see what the DB is returning.

`retrieve.py` embeds a few natural-language queries and prints the nearest notes from the saved
collection.

Run it:
```bash
python retrieve.py
```

➡ Next: [04-chat-with-ai-over-your-notes](../04-chat-with-ai-over-your-notes/) — take the retrieved
notes and give them to the model as context.
