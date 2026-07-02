"""
Day 18 - Exercise 2 (STUB): Notes chat assistant with Chroma + Groq.
"""

from pathlib import Path

import chromadb
from dotenv import load_dotenv
from groq import Groq
from sentence_transformers import SentenceTransformer


BASE_DIR = Path(__file__).resolve().parent.parent
DB_DIR = BASE_DIR / "exercise_notes_chroma"
COLLECTION_NAME = "study_notes"

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

    # TODO: embed NOTES and upsert them into the collection

    question = "Why do recursive functions not run forever?"

    # TODO: retrieve the top 2 notes for the question
    matches = None

    # TODO: add a similarity cutoff. If weak, print a fallback message and return.

    # TODO: create a Groq client, build a context block from the retrieved notes,
    # and ask the model to answer from those notes only.
    llm = Groq()
    _ = llm

    print("Question:", question)
    print("TODO: print the grounded answer")


if __name__ == "__main__":
    main()
