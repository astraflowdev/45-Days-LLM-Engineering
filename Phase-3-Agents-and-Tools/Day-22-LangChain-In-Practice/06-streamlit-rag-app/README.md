# 06 · Chat With Your Docs — LangChain Edition

The day's capstone. Day 20 built "chat with your documents" with a hand-rolled chunker and raw Chroma.
Here we rebuild it on **LangChain**, so every stage is a standard, swappable piece — and the whole app
is under 100 lines.

```bash
streamlit run app.py          # NOT `python app.py`
```

## The full pipeline, on one screen

```
upload / paste text
      │  RecursiveCharacterTextSplitter            (module 01)
      ▼
   chunks ──► HuggingFaceEmbeddings ──► Chroma ──► retriever   (module 02)
                                                      │
question ─────────────────────────────────────────────┤
                                                      ▼
              retrieve ► format_docs ► prompt ► model ► answer  (module 03)
                                                      │
                                          st.write_stream + Sources  (module 05)
```

Nothing here is new — it's modules 01→03 (RAG) wearing the module-05 (Streamlit) UI.

## Two places state lives

| State | Where | Why |
|-------|-------|-----|
| the **embeddings model** | `@st.cache_resource` | heavy, build once, reused every rerun |
| the **retriever** (your indexed docs) | `st.session_state.retriever` | depends on *this session's* uploads — rebuilt when you click Build |
| the **chat history** | `st.session_state.messages` | survives reruns (Day 19) |

The embeddings *model* is the same for everyone, so it's cached. The *index* is per-user, per-upload,
so it lives in `session_state` and is rebuilt on demand.

## Building the index

```python
splitter = RecursiveCharacterTextSplitter(chunk_size=400, chunk_overlap=60)
docs = [Document(page_content=chunk, metadata={"source": name})
        for name, text in sources for chunk in splitter.split_text(text)]
store = Chroma.from_documents(docs, embedding=get_embeddings())
st.session_state.retriever = store.as_retriever(search_kwargs={"k": k})
```

Each chunk keeps its **filename in metadata**, which powers the **"Sources used"** panel — so every
answer is auditable back to the document it came from.

## Retrieve-then-answer (so we can show sources)

Instead of a single fused chain, we retrieve **explicitly** first, then answer — because we want to
*display* the chunks that grounded the reply:

```python
hits = retriever.invoke(question)          # the chunks (also shown as Sources)
context = format_docs(hits)
chain = prompt | model | StrOutputParser()
answer = st.write_stream(chain.stream({"context": context, "question": question}))
```

Same grounding rule as module 03 — *answer ONLY from context* — so the bot won't invent facts your
documents don't contain.

## Try these
1. Click **Build index** with the sample text, then ask *"How long do refunds take?"* → grounded answer
   + a Sources panel citing `[pasted]`.
2. Ask *"Do you have a store in Delhi?"* → it should say it doesn't have that information.
3. Upload your own `.txt` notes, rebuild, and quiz them.

## Run it

```bash
streamlit run app.py
```
Embeddings/retrieval are **local** (no key), so indexing and the Sources panel work offline; without a
`GROQ_API_KEY` the app shows the retrieved context in place of a generated answer. Add a key for real
grounded answers.

## Where this goes
You've now shipped a real RAG app on LangChain. But it still answers each question in isolation — no
follow-ups like *"and what about express?"* that depend on the last turn. Making retrieval
**conversation-aware**, plus loops and branching, is what **LangGraph** is for.

➡ Next: **Day 23 — LangGraph** — state machines for AI: loops, branching, and memory beyond a single chain.
