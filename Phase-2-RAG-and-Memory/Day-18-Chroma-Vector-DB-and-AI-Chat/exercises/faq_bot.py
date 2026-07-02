"""
Day 18 - Exercise 1 (STUB): FAQ retrieval bot with Chroma.
"""

from pathlib import Path

import chromadb
from sentence_transformers import SentenceTransformer


BASE_DIR = Path(__file__).resolve().parent.parent
DB_DIR = BASE_DIR / "exercise_faq_chroma"
COLLECTION_NAME = "faq_collection"

FAQS = [
    {
        "id": "faq-1",
        "question": "How do I request a refund?",
        "answer": "Refunds can be requested within 7 days from the orders page.",
    },
    {
        "id": "faq-2",
        "question": "When will my certificate be issued?",
        "answer": "Certificates are issued after the final demo and attendance check.",
    },
    {
        "id": "faq-3",
        "question": "How can I reset my portal password?",
        "answer": "Use the forgot-password link on the login page and follow the email steps.",
    },
]


def main() -> None:
    model = SentenceTransformer("all-MiniLM-L6-v2")
    client = chromadb.PersistentClient(path=str(DB_DIR))
    collection = client.get_or_create_collection(
        name=COLLECTION_NAME,
        metadata={"hnsw:space": "cosine"},
    )

    # TODO: embed the FAQ questions
    question_embeddings = None

    # TODO: upsert FAQs into Chroma with ids, documents, answers in metadata, and embeddings

    user_question = "How do I get my payment back?"

    # TODO: embed the user question and query the collection for the best match
    result = None

    print("User question:", user_question)
    print("TODO: print the matched FAQ question and answer")


if __name__ == "__main__":
    main()
