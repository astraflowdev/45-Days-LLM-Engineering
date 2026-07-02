"""
Day 18 - Step 3: Turn scores into a ranked top-k answer.

np.argsort returns the INDICES that sort the scores; reverse it for
best-first, slice the top k, and map each index back to its document.
We wrap it into search(query, k) -> list of (score, document), best first.

Setup: pip install sentence-transformers numpy
Run:   python top_k.py
"""

import numpy as np
from sentence_transformers import SentenceTransformer

CORPUS = [
    "Buy milk and eggs from the market",
    "A bicycle or scooter is a cheap way to commute",
    "Finish the data structures assignment by Friday",
    "Recipe: boil rice, then add dal and spices",
    "Book train tickets for the Diwali trip home",
]


def unit(vectors):
    """Scale each row to length 1 so a dot product equals cosine similarity."""
    return vectors / np.linalg.norm(vectors, axis=-1, keepdims=True)


def main():
    print("Loading model (first run downloads ~90 MB)...\n")
    model = SentenceTransformer("all-MiniLM-L6-v2")

    # Embed the corpus once, up front.
    corpus_unit = unit(model.encode(CORPUS))

    def search(query, k=3):
        """Return the k documents most similar to query, best first."""
        query_unit = unit(model.encode(query))
        scores = corpus_unit @ query_unit            # (N,) cosine score per doc
        order = np.argsort(scores)[::-1]             # indices, highest score first
        top = order[:k]                              # keep the best k indices
        return [(float(scores[i]), CORPUS[i]) for i in top]

    for query in ["something to ride to college", "what should I cook for dinner"]:
        print(f"Query: {query!r}")
        for rank, (score, doc) in enumerate(search(query, k=3), start=1):
            print(f"  #{rank}  {score:+.3f}  {doc}")
        print()


if __name__ == "__main__":
    main()
