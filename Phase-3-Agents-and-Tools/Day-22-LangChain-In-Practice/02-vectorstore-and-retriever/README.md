# 02 · Vector Store & Retriever

Day 18 made chunks searchable **by hand**: embed each one, store the vectors, cosine-compare a query.
LangChain folds all of that into a **vector store** — and then hands you a **retriever**, the piece
that makes RAG just another `|` chain.

## The pipeline in three objects

```
Documents ──▶ embeddings model ──▶ Chroma vector store ──▶ retriever
 (mod 01)      (local, no key)       (embed + index)       (.as_retriever())
```

| Object | Role |
|--------|------|
| `HuggingFaceEmbeddings` | turns text → a 384-dim vector (local `all-MiniLM-L6-v2`, from Day 17) |
| `Chroma` | stores the vectors and searches them by similarity |
| **retriever** | the store wrapped as a **Runnable**: `query → list[Document]` |

## Embed + index in one line

```python
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")   # local, no key
store = Chroma.from_documents(docs, embedding=embeddings)           # embeds every chunk
```

`from_documents` embeds each `Document` and indexes it. No `persist_directory` → the store lives **in
memory** (perfect for a demo or a per-session app). Add `persist_directory="db"` and it saves to disk
so it survives restarts.

## Searching by meaning

```python
store.similarity_search("how do I get my money back?", k=2)
# → the "refunds" doc — even with zero shared words
```

That's the whole point of embeddings: *"money back"* matches *"Refunds are processed…"* by **meaning**,
not keywords. Want the distances too? `similarity_search_with_score` returns `(Document, score)` —
**lower distance = closer**.

## The retriever: why RAG becomes a chain

```python
retriever = store.as_retriever(search_kwargs={"k": 2})
retriever.invoke("when will my order arrive?")     # → list[Document]
```

`.as_retriever()` wraps the store as a **Runnable** — the same interface as a prompt, a model, a
parser. That's the unlock: because a retriever has `.invoke()`, it drops **straight into a `|` chain**.
RAG = a retriever piped in front of yesterday's `prompt | model | parser`. (That's module 03.)

## Common `search_kwargs`

| Setting | Effect |
|---------|--------|
| `{"k": 4}` | return the top 4 chunks (more context, longer prompt) |
| `{"k": 4, "filter": {"source": "refunds"}}` | only search chunks whose metadata matches |
| `search_type="mmr"` | "maximal marginal relevance" — diversify results, less redundancy |

`k` is the dial you tune most: too low misses context, too high floods the prompt with noise.

## Store vs retriever — which do I use?

- Use the **store** directly (`similarity_search`) when you just want to *see* matches / scores.
- Use the **retriever** (`.as_retriever()`) when you're **building a chain** — it's the composable
  Runnable form. RAG always uses the retriever.

## Run it

```bash
python vectorstore.py
```
No key needed — embeddings and search are fully local. (First run downloads the ~90 MB model once.)

➡ Next: [03 · RAG Chain (LCEL)](../03-rag-chain-lcel/README.md) — pipe the retriever into a chain for grounded answers.
