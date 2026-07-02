# Day 18 — Chroma Vector DB and AI Chat

Yesterday you learned that text can become vectors. Today you stop keeping those vectors in Python
lists and put them into a real vector database: **Chroma**.

That changes two things immediately:

1. You can **save** embeddings to disk and load them again tomorrow.
2. You can **retrieve** the nearest notes and pass them into an LLM so it answers from your data.

This is the practical RAG loop:

```text
embed notes -> store vectors in Chroma -> retrieve top matches -> give them to the AI -> answer
```

## Learning objectives
By the end of today you can:
- Create a persistent Chroma collection on disk
- Convert notes into embeddings and upsert them into the collection
- Re-open the database later and prove the vectors are still there
- Retrieve the top-k nearest notes for a new query
- Build a tiny AI chat with retrieval using Groq + Chroma
- Explain why vector databases matter: persistence, filtering, collections, and clean retrieval APIs

## Modules (work through them in order)

| # | Module | What it teaches | The "aha" |
|--:|--------|-----------------|-----------|
| 01 | [save-vectors-to-chroma](01-save-vectors-to-chroma/) | Create a collection and store embedded notes | Your vectors can live on disk |
| 02 | [persist-and-reload](02-persist-and-reload/) | Re-open the same collection in a fresh script | You do not re-embed every run |
| 03 | [retrieve-best-matches](03-retrieve-best-matches/) | Query Chroma for the nearest notes | Retrieval is now one database call |
| 04 | [chat-with-ai-over-your-notes](04-chat-with-ai-over-your-notes/) | Send retrieved notes into a chat model | This is the core RAG pattern |
| 05 | [why-this-matters](05-why-this-matters/) | Where Chroma fits in the bigger stack | Retrieval needs storage, not just math |

Then practise in **[exercises/](exercises/)**.

## Stack for today
- Embeddings: local `sentence-transformers` (`all-MiniLM-L6-v2`)
- Vector DB: `chromadb`
- Chat model: `groq`

## Setup
```bash
pip install -r requirements.txt
```

Create a `.env` for the chat module:

```bash
GROQ_API_KEY=your_key_here
```

> The first embedding run downloads the local model once (~90 MB). Chroma stores its files inside
> this day folder, so you can inspect and delete the local database easily.

## How to run
```bash
python 01-save-vectors-to-chroma/store_vectors.py
python 02-persist-and-reload/reload_collection.py
python 03-retrieve-best-matches/retrieve.py
python 04-chat-with-ai-over-your-notes/rag_chat.py
python 05-why-this-matters/recap.py
```

## Today's exercise
Build:
- a FAQ retrieval bot backed by Chroma
- a notes chat assistant that retrieves relevant notes before asking Groq to answer

See [`exercises/`](exercises/).

> Day 17 taught you what embeddings are. Day 18 turns them into a persistent retrieval system. Day
> 19 moves the same idea from local Chroma to cloud Postgres with `pgvector`.

➡ Next (Day 19): pgvector via Supabase — move local retrieval into cloud Postgres.
