"""
Day 18 - Exercise 2 (SOLUTION): Notes chat assistant with Chroma + Groq.
"""

from pathlib import Path

import chromadb
from dotenv import load_dotenv
from groq import Groq
from sentence_transformers import SentenceTransformer


BASE_DIR = Path(__file__).resolve().parent.parent
DB_DIR = BASE_DIR / "exercise_notes_chroma"
COLLECTION_NAME = "study_notes"
MODEL_NAME = "llama-3.3-70b-versatile"

NOTES = [
    "Linked lists are good for cheap inserts but slow random access.",
    "A stack follows last in, first out. Function calls use the call stack.",
    "Prompt examples reduce ambiguity and help the model copy the output format.",
    "Recursion should reduce the problem size and must have a base case.",
]


def main() -> None:
    load_dotenv()
    model = SentenceTransformer("all-MiniLM-L6-v2")
    client = chromadb.PersistentClient(path=str(DB_DIR))
    collection = client.get_or_create_collection(
        name=COLLECTION_NAME,
        metadata={"hnsw:space": "cosine"},
    )

    note_embeddings = model.encode(NOTES).tolist()
    collection.upsert(
        ids=[f"note-{index}" for index in range(1, len(NOTES) + 1)],
        documents=NOTES,
        embeddings=note_embeddings,
    )

    question = "Why do recursive functions not run forever?"
    result = collection.query(
        query_embeddings=[model.encode(question).tolist()],
        n_results=2,
        include=["documents", "distances"],
    )

    matches = []
    for document, distance in zip(result["documents"][0], result["distances"][0]):
        matches.append({"document": document, "similarity": 1 - distance})

    best_similarity = matches[0]["similarity"]
    if best_similarity < 0.35:
        print("I do not have enough notes to answer that confidently.")
        return

    context_block = "\n".join(
        f"- similarity={match['similarity']:.3f} {match['document']}" for match in matches
    )

    llm = Groq()
    response = llm.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": (
                    "Answer only from the provided notes. If the notes are insufficient, say so."
                ),
            },
            {
                "role": "user",
                "content": f"Notes:\n{context_block}\n\nQuestion: {question}",
            },
        ],
        temperature=0.2,
    )

    answer = response.choices[0].message.content or ""

    print("Question:", question)
    print("\nRetrieved notes:")
    for match in matches:
        print(f"- similarity={match['similarity']:.3f} {match['document']}")
    print("\nAnswer:", answer)


if __name__ == "__main__":
    main()
