"""
EXERCISE 1 - RAG CLI.

Build a LangChain RAG chain over a small FAQ, then answer questions in the
terminal. Fill in every TODO, then run:
    python rag_cli.py
Compare with rag_cli_solution.py. Retrieval works with no key; the answer
step needs GROQ_API_KEY (skips gracefully without one).
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

FAQS = [
    ("hours",    "We are open every day from 10am to 9pm, including public holidays."),
    ("parking",  "Free customer parking is available in the basement, levels B1 and B2."),
    ("returns",  "Unused items can be returned within 15 days with the original bill."),
    ("wifi",     "Free WiFi is available; ask any staff member for today's password."),
]

# TODO 1: turn FAQS into a list of Document(page_content=..., metadata={"source": topic}).
docs = ...

# TODO 2: build embeddings (HuggingFaceEmbeddings, model_name="all-MiniLM-L6-v2")
#         and a Chroma store from docs, then a retriever with search_kwargs={"k": 2}.
retriever = ...

def format_docs(retrieved) -> str:
    # TODO 3: join the retrieved docs into one string like "[source] content" per line.
    ...

prompt = ChatPromptTemplate.from_messages([
    ("system", "Answer using ONLY the context. If it's not there, say you don't know.\n\n"
               "Context:\n{context}"),
    ("human", "{question}"),
])

def build_chain(model):
    # TODO 4: return the LCEL RAG chain:
    #   {"context": retriever | format_docs, "question": RunnablePassthrough()}
    #     | prompt | model | StrOutputParser()
    ...

QUESTIONS = ["When do you close?", "Where can I park?", "Do you sell laptops?"]

if __name__ == "__main__":
    if not os.getenv("GROQ_API_KEY"):
        print("No GROQ_API_KEY -- showing retrieved context per question:\n")
        for q in QUESTIONS:
            print(f"Q: {q}")
            print("  " + format_docs(retriever.invoke(q)).replace("\n", "\n  "), "\n")
    else:
        from langchain_groq import ChatGroq
        chain = build_chain(ChatGroq(model=MODEL, temperature=0))
        for q in QUESTIONS:
            print(f"Q: {q}\nA: {chain.invoke(q)}\n")
