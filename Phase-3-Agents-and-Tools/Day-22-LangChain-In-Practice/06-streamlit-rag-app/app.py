"""
06 - Chat With Your Docs, LangChain edition (the day's capstone).

Day 20 built this with a hand-rolled chunker + raw Chroma. Here we rebuild it on
LangChain, so the whole app is standard, swappable pieces:

    upload text -> RecursiveCharacterTextSplitter -> HuggingFaceEmbeddings
                -> Chroma (in session) -> retriever -> LCEL RAG chain -> streamed answer

What ties the day together:
    - modules 01-03 : splitter, vector store/retriever, the RAG chain
    - module 05     : Streamlit chat UI, session_state, streaming
Embeddings are LOCAL (no key); only the final answer calls Groq.

Setup:
    pip install streamlit langchain langchain-groq langchain-chroma \
                langchain-huggingface langchain-text-splitters sentence-transformers python-dotenv
    echo GROQ_API_KEY=your_key > .env
Run  (streamlit run, NOT python):
    streamlit run app.py
"""

import os
import warnings
warnings.filterwarnings("ignore")
from dotenv import load_dotenv
import streamlit as st

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

load_dotenv()
MODEL = "llama-3.1-8b-instant"

st.set_page_config(page_title="Chat With Your Docs", page_icon="📄")
st.title("📄 Chat With Your Docs — LangChain edition")

SAMPLE = (
    "Refunds are processed within 5 business days to the original payment method.\n"
    "We ship across India; standard delivery takes 4 to 7 working days.\n"
    "Cash on delivery is available for orders under 5000 rupees.\n"
    "Our office is in Pune; support is open 9am to 6pm, Monday to Saturday."
)


# --- Embeddings model: build once, reuse across reruns --------------------
@st.cache_resource
def get_embeddings():
    return HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")


# --- Sidebar: load documents, build the index -----------------------------
with st.sidebar:
    st.header("1. Load documents")
    uploaded = st.file_uploader("Upload .txt / .md files", type=["txt", "md"],
                                accept_multiple_files=True)
    pasted = st.text_area("...or paste text", value=SAMPLE, height=160)
    k = st.slider("Chunks to retrieve (k)", 1, 6, 3)

    if st.button("Build / rebuild index", type="primary"):
        # Gather raw text from uploads + the paste box.
        texts = []
        for f in uploaded or []:
            texts.append((f.name, f.read().decode("utf-8", errors="ignore")))
        if pasted.strip():
            texts.append(("pasted", pasted))

        if not texts:
            st.warning("Add a file or paste some text first.")
        else:
            # Split each source into chunks, keeping its filename as metadata.
            splitter = RecursiveCharacterTextSplitter(chunk_size=400, chunk_overlap=60)
            docs = []
            for name, text in texts:
                for chunk in splitter.split_text(text):
                    docs.append(Document(page_content=chunk, metadata={"source": name}))
            # Build an in-session vector store + retriever.
            store = Chroma.from_documents(docs, embedding=get_embeddings())
            st.session_state.retriever = store.as_retriever(search_kwargs={"k": k})
            st.session_state.n_chunks = len(docs)
            st.session_state.messages = []          # fresh chat for a new corpus
            st.success(f"Indexed {len(docs)} chunks from {len(texts)} source(s).")

    if "n_chunks" in st.session_state:
        st.caption(f"Index ready: {st.session_state.n_chunks} chunks.")


# --- The grounded prompt + answer chain -----------------------------------
prompt = ChatPromptTemplate.from_messages([
    ("system",
     "You are a document assistant. Answer using ONLY the context below. "
     "If the answer isn't in the context, say you don't have that information.\n\n"
     "Context:\n{context}"),
    ("human", "{question}"),
])

def format_docs(docs) -> str:
    return "\n".join(f"[{d.metadata['source']}] {d.page_content}" for d in docs)


# --- Main pane: ask questions about the loaded docs -----------------------
if "retriever" not in st.session_state:
    st.info("👈 Load documents and click **Build index** to start chatting with them.")
    st.stop()

st.session_state.setdefault("messages", [])
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if question := st.chat_input("Ask about your documents..."):
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)

    # Retrieve first so we can both answer from and DISPLAY the sources.
    hits = st.session_state.retriever.invoke(question)
    context = format_docs(hits)

    with st.chat_message("assistant"):
        if not os.getenv("GROQ_API_KEY"):
            # Offline: show the retrieved context so the app is still usable/testable.
            answer = ("(No GROQ_API_KEY set — showing the retrieved context instead of an answer.)"
                      f"\n\n{context}")
            st.markdown(answer)
        else:
            from langchain_groq import ChatGroq
            chain = prompt | ChatGroq(model=MODEL, temperature=0) | StrOutputParser()
            answer = st.write_stream(chain.stream({"context": context, "question": question}))
        # Show which chunks grounded the answer.
        with st.expander("Sources used"):
            for d in hits:
                st.markdown(f"**[{d.metadata['source']}]** {d.page_content}")

    st.session_state.messages.append({"role": "assistant", "content": answer})
