# Day 18 — Semantic Search From Scratch (numpy + cosine, no framework)

Yesterday you turned text into vectors and measured how close two of them are. Today you turn that
into something useful: a **search engine that finds by meaning**. Type *"something to ride to
college"* and it surfaces the note about a **scooter** — even though that word never appears in your
query.

This is the single most important loop in this whole phase. It's the **"R" in RAG** (Retrieval):

```
embed the knowledge base ONCE  ->  embed the query  ->  score every doc  ->  return the best
```

We build it **by hand with numpy** — no Chroma, no LlamaIndex, no magic. Tomorrow (Day 19) a real
vector database does exactly this for you; the only way to trust the tool is to have built the thing
once yourself.

## Learning objectives
By the end of today you can:
- Embed a whole **corpus** (a list of documents) once into a single numpy **matrix**
- Score a query against **every** document with **one** vectorized numpy operation (no Python loop)
- Rank results and return the **top-k** best matches with their scores
- Wrap the whole thing in a reusable **`SemanticSearch`** class (`.add()` / `.search()`)
- Explain what this is (retrieval), where it breaks at scale, and **why a vector DB exists**

## Modules (work through them in order)

| # | Module | What it teaches | The "aha" |
|--:|--------|-----------------|-----------|
| 01 | [corpus-and-embed](01-corpus-and-embed/) | Embed many docs once into an `N x 384` matrix | Your knowledge base is **one matrix** |
| 02 | [query-and-score](02-query-and-score/) | Score the whole corpus against a query in one shot | One line of numpy beats every doc at once |
| 03 | [top-k-results](03-top-k-results/) | Sort the scores, return the best k | Scores -> a ranked answer |
| 04 | [mini-search-engine](04-mini-search-engine/) | Wrap it in a `SemanticSearch` class + live loop | You built **retrieval** |
| 05 | [why-this-matters](05-why-this-matters/) | This is RAG; where it breaks; why vector DBs | When to stop hand-rolling it |

Then practise in **[exercises/](exercises/)**.

## Provider: local `sentence-transformers` (free, no key)
Same as Day 17 — the **`all-MiniLM-L6-v2`** model: tiny (~90 MB), runs on your laptop, costs
nothing, no API key. We reuse the **cosine similarity** you wrote yesterday. Nothing new to install.

## Setup
```bash
pip install -r requirements.txt        # needs: numpy, sentence-transformers
```
> First run downloads the model once (~90 MB). After that it loads from disk instantly. Module 05
> needs **no model at all** — it's a pure-Python recap that runs offline.

## How to run
```bash
python 01-corpus-and-embed/embed_corpus.py
python 02-query-and-score/score.py
python 03-top-k-results/top_k.py
python 04-mini-search-engine/search_engine.py     # interactive: type queries, Ctrl+C to quit
python 05-why-this-matters/recap.py               # offline, no model
```

## Today's exercise
Build a **FAQ answer bot** (match a user's question to the closest stored FAQ) and a **search-your-
own-notes** tool. See [`exercises/`](exercises/).

> Today you built search by scanning **every** vector by hand. **Day 19** stores those vectors in
> **Chroma**, a real vector database that persists them to disk and finds the nearest ones *fast* —
> so you don't re-embed your whole corpus on every run.

➡ Next (Day 19): Chroma — your first vector database (persistence + collections).
