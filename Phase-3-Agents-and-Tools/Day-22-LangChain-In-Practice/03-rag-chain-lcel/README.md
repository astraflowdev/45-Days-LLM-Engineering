# 03 · The RAG Chain (LCEL)

Here's the payoff. **RAG is not a new framework** — it's yesterday's `prompt | model | parser` chain
with a **retriever bolted on the front**:

```python
rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | model
    | StrOutputParser()
)
rag_chain.invoke("How long do refunds take?")
```

Every arrow is the same LCEL `|` from Day 21. We just added a **retrieve → format** step in front.

## The flow, step by step

```
question ─┬─▶ retriever ─▶ format_docs ─▶ {context}  ─┐
          └────────── passthrough ──────▶ {question} ─┴─▶ prompt ─▶ model ─▶ parser ─▶ answer
```

| Stage | Gets | Returns |
|-------|------|---------|
| `retriever` | the question | top-k `Document`s |
| `format_docs` | those Documents | one context **string** (with `[source]` tags) |
| `RunnablePassthrough()` | the question | the question, unchanged |
| `prompt` | `{context, question}` | filled messages |
| `model` → `parser` | messages → reply | a plain-text answer |

## The dict is a `RunnableParallel`

That opening `{...}` runs **both branches for the same input** and collects their outputs into a dict:

```python
{"context": retriever | format_docs,   # branch 1: fetch + stitch the chunks
 "question": RunnablePassthrough()}     # branch 2: pass the question straight through
```

The result — `{"context": "...", "question": "..."}` — is exactly the shape the prompt's `{context}`
and `{question}` variables need. (You saw `RunnableParallel` / `RunnablePassthrough` on Day 21,
module 05 — this is what they were *for*.)

## `format_docs`: the one bit of glue

The retriever returns `list[Document]`; the prompt wants a `str`. This tiny function bridges them —
and tagging each chunk with its source is what lets you **cite** later:

```python
def format_docs(retrieved):
    return "\n".join(f"[{d.metadata['source']}] {d.page_content}" for d in retrieved)
```

## What makes it RAG (not just a chatbot): grounding

The system prompt is doing real work:

> *"Answer using **ONLY** the context below. If the answer isn't in the context, say you don't have
> that information."*

That instruction is why the model **refuses to invent** a Mumbai store when the retrieved chunks don't
mention one. Grounding = the model sticks to retrieved facts instead of its own guesses. It's the whole
reason RAG reduces hallucination.

## Do this, not `RetrievalQA`

Older tutorials wire RAG with `RetrievalQA` or `ConversationalRetrievalChain`. Those are **deprecated**.
The composed LCEL chain above is the current way — and it's more transparent: you can see and tweak
every stage. If a blog uses `RetrievalQA(...)`, it predates LCEL RAG.

## Run it

```bash
python rag_chain.py
```
**Without** a key it prints the exact context the retriever feeds the prompt for each question (so you
see retrieval working offline). **With** `GROQ_API_KEY`, it returns grounded answers — including
correctly saying "I don't have that information" for the out-of-context question.

➡ Next: [04 · Chatbot With Memory](../04-chatbot-with-memory/README.md) — switch gears to a conversational LangChain chain.
