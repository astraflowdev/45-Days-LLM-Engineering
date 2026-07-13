# Day 22 · Exercises

Two console programs that drill the day's two pillars — **RAG** and a **memory chatbot** — with
LangChain. Each has a stub with `# TODO`s and a worked `_solution.py`. **Retrieval and memory run
without a key**; the final Groq answer step skips gracefully if no key is set.

## 1. RAG CLI (`rag_cli.py`)

Build a LangChain **RAG chain** over a small FAQ and answer questions from the terminal.

- Turn the given `FAQS` list into `Document`s (each with a `source` in metadata).
- Embed them with local `HuggingFaceEmbeddings` into a `Chroma` store; get a retriever (`k=2`).
- Compose the LCEL chain: `{"context": retriever | format_docs, "question": passthrough} | prompt | model | parser`.
- Loop over a few questions and print grounded answers (or the retrieved context, offline).

> **Skills:** splitters/Documents (01), vector store + retriever (02), the LCEL RAG chain (03).

## 2. Persona Chatbot (`persona_chatbot.py`)

A memory-carrying chatbot with a **swappable system persona**.

- Build a prompt: a `{persona}`-driven system line + `MessagesPlaceholder("history")` + `{input}`.
- Keep a `history` list; append both sides every turn (module 04).
- Run a scripted 3-turn chat where the bot must recall an earlier detail.
- Bonus: change the persona string (e.g. "reply like a pirate") and see the tone shift.

> **Skills:** prompt templates + `MessagesPlaceholder` (04), memory as a history list.

## Run

```bash
python rag_cli_solution.py
python persona_chatbot_solution.py
```
(Swap `_solution` for the stub name once you've filled in the TODOs.)

## Stretch

- **RAG CLI:** add a metadata `filter` to `search_kwargs` so a question only searches one topic; or
  raise `k` and watch the context grow.
- **Persona Chatbot:** wrap it in a real `while True: input(...)` REPL with a `/persona <text>` command
  to switch personas live, and a `/reset` to clear history.

➡ Back to the day: [README](../README.md)
