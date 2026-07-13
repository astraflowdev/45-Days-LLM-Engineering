# Day 21 — LangChain Fundamentals

**Phase 3 · Agents & Tools — Day 1.** Phase 2 gave us the moving parts (models, embeddings,
retrieval, a real RAG app). Now we pick up **LangChain**, the framework those parts snap into —
and the foundation for LangGraph and the agents we build next.

> **What you learn:** the ~20% of LangChain you actually use every day — chat models, prompt
> templates, **LCEL** (`prompt | model | parser`), output parsers, runnable composition, and
> conversation memory — all on free **Groq**, using the **latest LangChain 1.x** syntax.

## Why a framework now?

We called Groq directly since Day 9 and it worked. LangChain earns its place by giving every model
the **same interface** and letting the pieces **compose** — swap providers in one line, and reuse
the same prompts, chains, parsers, memory, and (soon) tools and agents on top. Today is the on-ramp
to the rest of Phase 3.

## Learning objectives
By the end of today you can:
- Call any chat model through one interface (`ChatGroq`, `.invoke()`, message objects).
- Write reusable prompts with `ChatPromptTemplate` and fill in `{variables}`.
- Build chains with **LCEL** — the `|` operator — and use `invoke` / `batch` / `stream`.
- Get **typed data** out of a model with `with_structured_output` + Pydantic.
- Branch and combine steps with `RunnableLambda` / `RunnableParallel` / `RunnablePassthrough`
  (and recognise this as the RAG wiring).
- Add conversation memory the current, non-deprecated way (`MessagesPlaceholder` + a history list).

## What this reuses
| From    | Idea used here                                        |
|---------|-------------------------------------------------------|
| Day 9   | Calling Groq — now through `ChatGroq`                  |
| Day 8   | Pydantic — now to define **output** schemas           |
| Day 16  | "Append every turn" memory — now via a prompt slot    |
| Day 20  | The RAG shape (retrieve → prompt → answer) — now as an LCEL chain |

## Module index
| # | Folder | You learn |
|---|--------|-----------|
| 01 | [`01-why-langchain/`](01-why-langchain/README.md) | Raw Groq vs `ChatGroq`; message objects; one interface, any provider |
| 02 | [`02-prompt-templates/`](02-prompt-templates/README.md) | `ChatPromptTemplate`, `{variables}`, `format_messages` |
| 03 | [`03-lcel-chains/`](03-lcel-chains/README.md) | LCEL — the `\|` operator; `prompt \| model \| parser`; invoke/batch/stream |
| 04 | [`04-output-parsers/`](04-output-parsers/README.md) | `StrOutputParser` vs `with_structured_output` (typed Pydantic output) |
| 05 | [`05-runnables/`](05-runnables/README.md) | `RunnableLambda` / `Parallel` / `Passthrough` — and the RAG wiring |
| 06 | [`06-memory/`](06-memory/README.md) | Conversation memory with `MessagesPlaceholder` (non-deprecated) |

### Exercises
| Folder | Practise |
|--------|----------|
| [`exercises/`](exercises/README.md) | Translator Chain (LCEL + `batch`) · Structured Extractor (`with_structured_output`) |

### Presentation
A branded slide deck — **LangChain: Intro, Chains & Agents** — introduces the topic and previews
agents/LangGraph: [`presentation/index.html`](presentation/index.html) (open in a browser; see the
[speaker notes](presentation/README.md)).

## How to run

**Setup (once).** Install with the real CPython (see repo `CLAUDE.md`):
```bash
pip install langchain langchain-groq python-dotenv
```
Create a `.env` in the folder you run from with your free Groq key:
```
GROQ_API_KEY=your_key_here
```
Get a free key at [console.groq.com/keys](https://console.groq.com/keys).

**Run the modules in order:**
```bash
python 01-why-langchain/why_langchain.py
python 02-prompt-templates/prompt_templates.py
python 03-lcel-chains/lcel_chains.py
python 04-output-parsers/structured_output.py
python 05-runnables/composition.py
python 06-memory/conversation_memory.py
```
Every script is built to run **without a key** — it shows the wiring (templates, `|` flow, schemas,
memory growth) offline and skips only the live network call. Add a key to see real answers.

## Today's exercise
Do both in [`exercises/`](exercises/README.md):
1. **Translator Chain** — one `prompt | model | parser` chain, three languages via `batch`.
2. **Structured Extractor** — pull a typed `Contact` out of an email signature.

## Latest-syntax notes (LangChain 1.x)
- Chains are **LCEL**: `prompt | model | parser`. `LLMChain` / `SequentialChain` are legacy — don't use them.
- Structured output is `model.with_structured_output(PydanticModel)`, not hand-parsed JSON.
- Simple memory is `MessagesPlaceholder` + your own history list. `RunnableWithMessageHistory` is
  **deprecated**; heavier state moves to **LangGraph**.

## The big idea
> LangChain isn't magic — it's one honest interface (`invoke`) and one operator (`|`). Learn those,
> and every piece (prompt, model, parser, retriever, tool) snaps together the same way. That's the
> base the rest of Phase 3 builds agents on.

➡ Next: **Day 22 — LangChain in Practice** — put it all to work: build **RAG with LangChain**
(splitters, vector store, retriever, an LCEL RAG chain) and a **Streamlit × LangChain chatbot**.
