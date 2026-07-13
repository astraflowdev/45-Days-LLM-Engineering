# 01 · Documents & Splitters

RAG always starts the same way: **break big text into small, searchable chunks.** On Day 20 you wrote
a word-counter chunker by hand. LangChain hands you a smarter one — and a standard way to carry each
chunk's *source*.

## Two objects to meet

| Object | What it is |
|--------|-----------|
| `Document` | LangChain's text wrapper: `.page_content` (the text) + `.metadata` (a dict) |
| `RecursiveCharacterTextSplitter` | splits text/Documents into overlapping chunks, respecting structure |

`Document` is how *everything* flows through a LangChain RAG pipeline — the splitter emits them, the
vector store stores them, the retriever returns them. Content + metadata, always together.

## Why "recursive"?

A naive splitter cuts every N characters — often mid-word or mid-sentence. `RecursiveCharacterTextSplitter`
tries a **list of separators in order**, biggest first:

```python
separators=["\n\n", "\n", ". ", " ", ""]
#            paragraph  line  sentence  word  (last resort: mid-word)
```

It splits on paragraphs where it can, drops to sentences when a paragraph is too big, and only ever
cuts a word as a last resort. Chunks come out clean.

```python
splitter = RecursiveCharacterTextSplitter(
    chunk_size=160,      # target max characters per chunk
    chunk_overlap=30,    # characters shared between neighbours
)
chunks = splitter.split_text(long_text)      # -> list[str]
```

## Why overlap?

A fact can land exactly on a chunk boundary and get cut in half — so neither chunk holds it whole.
**Overlap** repeats the last few characters of one chunk at the start of the next, so a boundary-straddling
sentence survives intact in at least one chunk. A little overlap (10–20% of `chunk_size`) is standard.

## Chunks vs Documents

| Method | Returns | Use when |
|--------|---------|----------|
| `splitter.split_text(text)` | `list[str]` | you just need the strings |
| `splitter.create_documents([text], metadatas=[{...}])` | `list[Document]` | you want to keep **source metadata** (for citations) |
| `Document(page_content=..., metadata=...)` | one `Document` | building a chunk by hand |

In real RAG you almost always want **Documents** — the metadata (`{"source": "policy.txt"}`) is what
lets you later say *"answer came from policy.txt."*

## Picking `chunk_size`

| Too small | Too big |
|-----------|---------|
| a fact gets split across chunks; retrieval misses half of it | chunk holds several topics; retrieval pulls in irrelevant text, wasting the prompt |

Start around **500–1000 characters** for prose; we use a tiny `160` here just so the split is easy to
*see* on screen.

## Run it

```bash
python splitters.py
```
No key needed — splitting is pure text work. You'll see the policy text split into clean, overlapping
chunks, then the same as `Document`s with metadata.

➡ Next: [02 · Vector Store & Retriever](../02-vectorstore-and-retriever/README.md) — embed these chunks and make them searchable.
