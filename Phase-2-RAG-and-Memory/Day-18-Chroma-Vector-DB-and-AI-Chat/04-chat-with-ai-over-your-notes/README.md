# 04 — Chat with AI Over Your Notes

This is the full beginner RAG loop.

## The pattern
For each user question:

1. embed the question
2. retrieve the top notes from Chroma
3. build a prompt that includes those notes
4. ask the chat model to answer using that context

```python
messages = [
    {"role": "system", "content": "...use only the retrieved notes..."},
    {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {question}"},
]
```

The model is still just a chatbot. What makes it grounded is the retrieved context you attach before
the call.

## Why this is better than plain chat
Without retrieval, the model answers from its own training data and guesses about your private notes.
With retrieval, it can answer from:

- your class notes
- your FAQ
- your policy docs
- your product catalog

`rag_chat.py` loads the saved Chroma collection, retrieves the nearest notes for each question, and
asks Groq to answer from those notes only.

Run it:
```bash
python rag_chat.py
```

Try asking:
- `How should I study recursion?`
- `What does binary search need before it works?`
- `How can I improve prompt quality?`

➡ Next: [05-why-this-matters](../05-why-this-matters/) — connect today's code to real RAG systems.
