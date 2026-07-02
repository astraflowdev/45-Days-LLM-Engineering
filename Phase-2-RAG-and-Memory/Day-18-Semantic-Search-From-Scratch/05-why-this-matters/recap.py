"""
Day 18 - Step 5: Why today matters (offline recap, no model needed).

The semantic search you built IS the retrieval step of RAG. This script
needs no internet and no embedding model -- it just prints the big picture
and where the hand-rolled version stops scaling, so the idea sticks.

Run:   python recap.py
"""


def main():
    print("=" * 64)
    print("  What you built today = the 'R' in RAG (Retrieval)")
    print("=" * 64)
    print(
        """
RAG = Retrieval-Augmented Generation. To answer questions about YOUR
documents, an AI first finds the relevant bits, then answers from them:

    1. RETRIEVE   <- your SemanticSearch.search() does exactly this
       embed the question, find the most similar document chunks
    2. AUGMENT
       paste those chunks into the prompt as context
    3. GENERATE
       the LLM answers using that context (and can cite it)
"""
    )

    print("Where the hand-rolled (numpy) version breaks as you grow:\n")
    rows = [
        ("No persistence", "re-embeds the whole corpus every run", "vector DB saves to disk"),
        ("Linear scan",    "scores EVERY vector, slow at millions",  "ANN index (HNSW)"),
        ("No metadata",    "no filtering, no easy update/delete",    "DB stores + filters metadata"),
    ]
    print(f"  {'Problem':<16}{'What happens':<40}{'Fixed by'}")
    print(f"  {'-'*15:<16}{'-'*39:<40}{'-'*22}")
    for problem, happens, fix in rows:
        print(f"  {problem:<16}{happens:<40}{fix}")

    print(
        """
The MATH never changes -- still embeddings + cosine similarity. A vector
database just makes it persistent, fast, and manageable at scale.

Rule of thumb:
  - a few hundred docs, throwaway script   -> numpy like today is fine
  - thousands+, must persist, needs filters -> use a vector DB

Next: Day 19 swaps our in-memory matrix for Chroma -- a real vector DB.
"""
    )


if __name__ == "__main__":
    main()
