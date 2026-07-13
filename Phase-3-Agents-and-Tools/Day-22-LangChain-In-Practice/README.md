# Day 22 — LangChain in Practice: RAG & a Streamlit Chatbot

**Phase 3 · Agents & Tools — Day 2.** Day 21 taught the LangChain *pieces* — models, prompts, LCEL,
parsers, memory. Today we stop learning pieces and **build two real things** with them:

1. **RAG, the LangChain way** — the gap we've been circling. Day 18 built semantic search by hand and
   Day 20 wired raw Chroma into an app. Today we rebuild retrieval with LangChain's own components
   (splitters, a vector store, a **retriever**) and answer questions with an **LCEL RAG chain**.
2. **A Streamlit × LangChain chatbot** — a streaming web chat whose brain is a LangChain chain, with
   conversation memory in `session_state`. Then we fuse the two into a **"Chat with your docs"** app,
   rebuilt on LangChain end to end.

> **What you learn:** how the Day-21 `|` chain grows into a **RAG pipeline** and a **deployable web
> app** — all on free **Groq** + **local embeddings** (no paid keys), LangChain 1.x.

## Why this day exists

You *can* do RAG by hand (we did — Day 18/20). LangChain earns its keep by making every step a
swappable, composable piece:

| Hand-rolled (Day 18/20) | LangChain (today) | Win |
|-------------------------|-------------------|-----|
| your own word-chunker | `RecursiveCharacterTextSplitter` | smarter splits, one line |
| numpy cosine + a dict | `Chroma` vector store | persistence, metadata, filters |
| a `search()` function | `vectorstore.as_retriever()` | a standard `Runnable` you can `|` into a chain |
| manual prompt stuffing | an **LCEL RAG chain** | retrieve → format → prompt → model → parse, composed |

The retriever is the key idea: it's **just another Runnable**, so RAG becomes one more `|` chain —
exactly like Day 21, now with a retrieval step in front.

## Learning objectives
By the end of today you can:
- Turn raw text into LangChain `Document`s and split them with `RecursiveCharacterTextSplitter`.
- Embed and store chunks in a **`Chroma`** vector store using **local** `HuggingFaceEmbeddings`.
- Get a **retriever** with `.as_retriever(search_kwargs={"k": ...})` and pipe it into a chain.
- Build a full **LCEL RAG chain**: `{context: retriever, question} | prompt | model | parser`.
- Build a **Streamlit chatbot** powered by a LangChain chain, streaming with `st.write_stream`.
- Combine both into a **document-Q&A web app** — upload files, ask grounded questions.

## What this reuses
| From    | Idea used here                                                    |
|---------|-------------------------------------------------------------------|
| Day 21  | LCEL `\|`, prompts, `StrOutputParser`, memory — now inside RAG/apps |
| Day 20  | "Chat with your documents" — now rebuilt with LangChain retrievers |
| Day 18  | Cosine semantic search — now a `Chroma` retriever                  |
| Day 19  | Streamlit `session_state`, `st.chat_input`, `st.write_stream`      |

## Module index
| # | Folder | You learn |
|---|--------|-----------|
| 01 | [`01-documents-and-splitters/`](01-documents-and-splitters/README.md) | `Document`, `RecursiveCharacterTextSplitter` — the LangChain way to chunk |
| 02 | [`02-vectorstore-and-retriever/`](02-vectorstore-and-retriever/README.md) | Local `HuggingFaceEmbeddings` + `Chroma` + `.as_retriever()` |
| 03 | [`03-rag-chain-lcel/`](03-rag-chain-lcel/README.md) | The payoff: a full **LCEL RAG chain** (retrieve → prompt → answer) |
| 04 | [`04-chatbot-with-memory/`](04-chatbot-with-memory/README.md) | A LangChain conversational chain with memory — a console REPL |
| 05 | [`05-streamlit-langchain-chatbot/`](05-streamlit-langchain-chatbot/README.md) | That chatbot as a **Streamlit web app** (streaming + history) |
| 06 | [`06-streamlit-rag-app/`](06-streamlit-rag-app/README.md) | **Chat with your docs**, rebuilt on LangChain end to end |

### Exercises
| Folder | Practise |
|--------|----------|
| [`exercises/`](exercises/README.md) | RAG CLI (build a RAG chain over an FAQ) · Persona Chatbot (memory + system prompt) |

## How to run

**Setup (once).** Install with the real CPython (see repo `CLAUDE.md`):
```bash
pip install langchain langchain-groq langchain-chroma langchain-huggingface \
            langchain-text-splitters sentence-transformers streamlit python-dotenv
```
Create a `.env` in the folder you run from with your free Groq key:
```
GROQ_API_KEY=your_key_here
```
Get a free key at [console.groq.com/keys](https://console.groq.com/keys). Embeddings run **locally**
(no key); only the final answer step calls Groq.

**Console modules (run with `python`):**
```bash
python 01-documents-and-splitters/splitters.py
python 02-vectorstore-and-retriever/vectorstore.py
python 03-rag-chain-lcel/rag_chain.py
python 04-chatbot-with-memory/chatbot.py
```
**Streamlit modules (run with `streamlit run`):**
```bash
streamlit run 05-streamlit-langchain-chatbot/app.py
streamlit run 06-streamlit-rag-app/app.py
```
Modules 01–02 need **no key** (splitting + local retrieval are offline). Modules 03–06 use Groq for
the final answer and print/show a clear message if no key is set.

## Today's exercise
Do both in [`exercises/`](exercises/README.md):
1. **RAG CLI** — build a LangChain RAG chain over a small FAQ and answer questions from the terminal.
2. **Persona Chatbot** — a memory-carrying chatbot with a swappable system persona.

## Latest-syntax notes (LangChain 1.x)
- Splitters live in `langchain_text_splitters`; embeddings in `langchain_huggingface`; the vector
  store in `langchain_chroma` — the modern, non-deprecated homes (older imports from
  `langchain.text_splitter` / `langchain_community` still work but are legacy).
- Build RAG with **LCEL**, not `RetrievalQA`. `RetrievalQA` / `ConversationalRetrievalChain` are the
  old, deprecated way; the composed `retriever | ... | prompt | model | parser` chain is current.
- A **retriever is a Runnable** — that's why it drops straight into a `|` chain.

## The big idea
> RAG isn't a new framework — it's the same `prompt | model | parser` chain from yesterday, with a
> **retriever** bolted on the front to fetch the right context first. Learn to treat retrieval as
> just another Runnable, and "chat with your data" becomes a one-screen app.

➡ Next: **Day 23 — LangGraph** — when a straight `|` chain (even a RAG one) isn't enough and you need
loops, branching, and memory across turns.
