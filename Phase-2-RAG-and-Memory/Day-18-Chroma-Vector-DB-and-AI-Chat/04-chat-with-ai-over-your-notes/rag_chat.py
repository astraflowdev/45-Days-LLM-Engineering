"""
Day 18 - Step 4: Retrieve notes from Chroma, then answer with Groq.
"""

from pathlib import Path

import chromadb
from dotenv import load_dotenv
from groq import Groq
from sentence_transformers import SentenceTransformer


BASE_DIR = Path(__file__).resolve().parent.parent
DB_DIR = BASE_DIR / "chroma_store"
COLLECTION_NAME = "student_notes"
MODEL_NAME = "llama-3.3-70b-versatile"


def retrieve_context(collection, embedder, question: str, k: int = 2):
    query_embedding = embedder.encode(question).tolist()
    result = collection.query(
        query_embeddings=[query_embedding],
        n_results=k,
        include=["documents", "metadatas", "distances"],
    )

    matches = []
    for document, metadata, distance in zip(
        result["documents"][0],
        result["metadatas"][0],
        result["distances"][0],
    ):
        matches.append(
            {
                "document": document,
                "topic": metadata.get("topic", "unknown"),
                "distance": distance,
                "similarity": 1 - distance,
            }
        )
    return matches


def build_context_block(matches) -> str:
    lines = []
    for index, match in enumerate(matches, start=1):
        lines.append(
            f"[Source {index} | topic={match['topic']} | similarity={match['similarity']:.3f}] "
            f"{match['document']}"
        )
    return "\n".join(lines)


def ask_groq(client: Groq, question: str, context_block: str) -> str:
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": (
                    "You answer only from the retrieved notes. If the notes are not enough, say "
                    "'I do not have enough notes to answer that confidently.' Keep answers short."
                ),
            },
            {
                "role": "user",
                "content": f"Retrieved notes:\n{context_block}\n\nQuestion: {question}",
            },
        ],
        temperature=0.2,
    )
    return response.choices[0].message.content or ""


def main() -> None:
    load_dotenv()
    llm = Groq()
    chroma_client = chromadb.PersistentClient(path=str(DB_DIR))
    collection = chroma_client.get_collection(COLLECTION_NAME)
    embedder = SentenceTransformer("all-MiniLM-L6-v2")

    print("=" * 72)
    print("RAG chat over your saved notes")
    print("=" * 72)
    print("Ask a question about the notes. Type 'quit' to exit.")

    while True:
        question = input("\nYou: ").strip()
        if not question:
            continue
        if question.lower() in {"quit", "exit"}:
            print("Bye.")
            break

        matches = retrieve_context(collection, embedder, question, k=2)
        context_block = build_context_block(matches)
        answer = ask_groq(llm, question, context_block)

        print("\nRetrieved context:")
        for match in matches:
            print(
                f"- [{match['topic']}] similarity={match['similarity']:.3f} "
                f"{match['document']}"
            )

        print(f"\nAssistant: {answer}")


if __name__ == "__main__":
    main()
