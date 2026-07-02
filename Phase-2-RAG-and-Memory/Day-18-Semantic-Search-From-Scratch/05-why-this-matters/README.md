# 05 — Why This Matters (and Where It Breaks)

Step back. The little engine you built in module 04 is not a toy concept — it's the **retrieval**
step that powers RAG, document Q&A, and "chat with your PDF". Understanding what you built (and its
limits) tells you exactly why tomorrow looks the way it does.

## What you actually built: the "R" in RAG
**RAG = Retrieval-Augmented Generation.** When you ask an AI "what does my contract say about
notice period?", it can't have your contract memorized. So:

```
1. RETRIEVE   <- you built this today
   embed the question, find the most similar chunks of the document
2. AUGMENT
   paste those chunks into the prompt as context
3. GENERATE
   the LLM answers using that context, and can cite it
```

Your `SemanticSearch.search()` **is** step 1. Everything in this phase builds outward from it.

## Where the hand-rolled version breaks
It's perfect for learning and fine for a few hundred documents. Three things break as you grow:

| Problem | What happens | The fix (Day 19+) |
|---------|--------------|-------------------|
| **No persistence** | Every run re-embeds the whole corpus from scratch — slow, wasteful | A vector **DB** saves vectors to disk; embed once, ever |
| **Linear scan** | `scores = matrix @ query` checks *every* vector. Fine at 1k, painful at 10M | **ANN** indexes (HNSW) find nearest neighbors without checking them all |
| **No metadata / updates** | Just text + vectors; no "filter by source", no easy delete/update | DBs store metadata, support filters, add/update/delete |

> The math doesn't change — it's still embeddings + cosine. A vector database just makes it
> **persistent, fast, and manageable** at scale. That's the entire pitch for Chroma tomorrow.

## When to hand-roll vs. reach for a DB
- **A few hundred docs, one process, throwaway script?** numpy like today is genuinely fine — don't
  over-engineer.
- **Thousands+ of docs, needs to persist between runs, filters, production?** Use a vector DB.

Knowing *both* — and when each is right — is what separates someone who pastes framework code from
someone who understands it.

`recap.py` needs **no model and no internet** — it's a pure-Python summary that prints the RAG loop
and the scaling table so the idea sticks.

Run it:
```bash
python recap.py
```

➡ Next: practise in [../exercises/](../exercises/), then **Day 19 — Chroma**, your first vector DB.
