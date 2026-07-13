"""
03 - The RAG chain: retrieval + LCEL = grounded answers.

This is the payoff of the last two modules. RAG is NOT a new framework -- it's
yesterday's prompt | model | parser chain with a RETRIEVER bolted on the front:

    {"context": retriever | format_docs, "question": passthrough}
        | prompt | model | parser

Read it: fetch the relevant chunks -> stitch them into a context string -> drop
that (plus the question) into a prompt -> model answers ONLY from that context
-> parse to plain text. Every arrow is the same LCEL | from Day 21.

Retrieval runs locally (no key). The final model call needs GROQ_API_KEY; without
one we still BUILD the chain and show the retrieved context, then skip the call.

Setup:
    pip install langchain langchain-groq langchain-chroma langchain-huggingface python-dotenv
Run:
    python rag_chain.py
"""

import os
import warnings
warnings.filterwarnings("ignore")
from dotenv import load_dotenv

from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

load_dotenv()
MODEL = "llama-3.1-8b-instant"

# --- 1. Build a retriever (modules 01-02, condensed) ----------------------
docs = [
    Document(page_content="Refunds are processed within 5 business days to the original payment method.",
             metadata={"source": "refunds"}),
    Document(page_content="We ship across India; standard delivery takes 4 to 7 working days.",
             metadata={"source": "shipping"}),
    Document(page_content="Cash on delivery is available for orders under 5000 rupees.",
             metadata={"source": "payment"}),
    Document(page_content="Our office is in Pune; support is open 9am to 6pm, Monday to Saturday.",
             metadata={"source": "support"}),
]
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
retriever = Chroma.from_documents(docs, embedding=embeddings).as_retriever(search_kwargs={"k": 2})

# --- 2. Turn retrieved Documents into a context string --------------------
# The retriever returns list[Document]; the prompt wants a single string. This
# tiny function is the glue -- and we tag each chunk with its source for citing.
def format_docs(retrieved) -> str:
    return "\n".join(f"[{d.metadata['source']}] {d.page_content}" for d in retrieved)

# --- 3. The grounded prompt -----------------------------------------------
# "Answer ONLY from the context" is what makes it RAG and not just a chatbot:
# the model is told to stick to retrieved facts and admit when it can't.
prompt = ChatPromptTemplate.from_messages([
    ("system",
     "You are a support assistant. Answer the question using ONLY the context below. "
     "If the answer isn't in the context, say you don't have that information.\n\n"
     "Context:\n{context}"),
    ("human", "{question}"),
])

# --- 4. Compose the RAG chain ---------------------------------------------
# The dict runs BOTH branches for each input:
#   context  = retriever(question) -> format_docs   (fetch + stitch)
#   question = the input, unchanged (RunnablePassthrough)
# Their outputs fill {context} and {question} in the prompt. Then model, parse.
def build_chain(model):
    return (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | model
        | StrOutputParser()
    )

# --- 5. Run it (or show the wiring offline) -------------------------------
questions = [
    "How long do refunds take?",
    "Can I pay cash when the order arrives?",
    "Do you have a store in Mumbai?",        # not in context -> should say it doesn't know
]

if not os.getenv("GROQ_API_KEY"):
    print("No GROQ_API_KEY -- showing what the retriever feeds the prompt, then stopping.\n")
    for q in questions:
        print(f"Q: {q}")
        print("Retrieved context the model WOULD see:")
        print("  " + format_docs(retriever.invoke(q)).replace("\n", "\n  "))
        print()
    print("With a key, build_chain(model).invoke(question) returns a grounded answer.")
else:
    from langchain_groq import ChatGroq
    chain = build_chain(ChatGroq(model=MODEL, temperature=0))
    for q in questions:
        print(f"Q: {q}")
        print(f"A: {chain.invoke(q)}\n")
    print("Notice the last answer: the model refuses to invent a Mumbai store,")
    print("because the retrieved context doesn't mention one. That's RAG grounding.")
