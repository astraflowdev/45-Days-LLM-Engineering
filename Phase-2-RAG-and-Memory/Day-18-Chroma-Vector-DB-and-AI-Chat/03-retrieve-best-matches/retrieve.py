"""
Day 18 - Step 3: Retrieve the nearest notes from Chroma.
"""

from pathlib import Path

import chromadb
from sentence_transformers import SentenceTransformer


BASE_DIR = Path(__file__).resolve().parent.parent
DB_DIR = BASE_DIR / "chroma_store"
COLLECTION_NAME = "student_notes"

QUERIES = [
    "How do I make a prompt more specific?",
    "What does binary search require first?",
    "How do recursive functions stop?",
]


def print_matches(collection, model, query: str, k: int = 2) -> None:
    query_embedding = model.encode(query).tolist()
    result = collection.query(
        query_embeddings=[query_embedding],
        n_results=k,
        include=["documents", "metadatas", "distances"],
    )

    print(f"\nQuery: {query}")
    for rank, (document, metadata, distance) in enumerate(
        zip(
            result["documents"][0],
            result["metadatas"][0],
            result["distances"][0],
        ),
        start=1,
    ):
        similarity = 1 - distance
        print(
            f"{rank}. similarity={similarity:.3f} topic={metadata.get('topic', 'unknown')} "
            f"-> {document}"
        )


def main() -> None:
    client = chromadb.PersistentClient(path=str(DB_DIR))
    collection = client.get_collection(COLLECTION_NAME)
    model = SentenceTransformer("all-MiniLM-L6-v2")

    print("=" * 72)
    print("Nearest-note retrieval with Chroma")
    print("=" * 72)

    for query in QUERIES:
        print_matches(collection, model, query)


if __name__ == "__main__":
    main()
