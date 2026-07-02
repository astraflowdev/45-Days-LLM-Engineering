"""
Day 18 - Exercise 1 (SOLUTION): FAQ retrieval bot with Chroma.
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

    question_embeddings = model.encode([faq["question"] for faq in FAQS]).tolist()

    collection.upsert(
        ids=[faq["id"] for faq in FAQS],
        documents=[faq["question"] for faq in FAQS],
        metadatas=[{"answer": faq["answer"]} for faq in FAQS],
        embeddings=question_embeddings,
    )

    user_question = "How do I get my payment back?"
    result = collection.query(
        query_embeddings=[model.encode(user_question).tolist()],
        n_results=1,
        include=["documents", "metadatas", "distances"],
    )

    matched_question = result["documents"][0][0]
    answer = result["metadatas"][0][0]["answer"]
    similarity = 1 - result["distances"][0][0]

    print("User question:", user_question)
    print("Matched FAQ :", matched_question)
    print("Similarity  :", f"{similarity:.3f}")
    print("Answer      :", answer)


if __name__ == "__main__":
    main()
