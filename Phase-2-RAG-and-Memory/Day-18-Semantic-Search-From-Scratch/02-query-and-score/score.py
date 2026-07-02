"""
Day 18 - Step 2: Score a query against the whole corpus at once.

Instead of looping over documents, we normalize every vector to length 1
and do ONE matrix-vector multiply:
    scores = corpus_unit @ query_unit        # shape (N,), one score per doc
For unit-length vectors, dot product == cosine similarity.

Setup: pip install sentence-transformers numpy
Run:   python score.py
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

QUERY = "something to ride to college"


def unit(vectors):
    """Scale each row to length 1 so a dot product equals cosine similarity."""
    norms = np.linalg.norm(vectors, axis=-1, keepdims=True)   # length of each row
    return vectors / norms


def main():
    print("Loading model (first run downloads ~90 MB)...\n")
    model = SentenceTransformer("all-MiniLM-L6-v2")

    corpus_vecs = model.encode(CORPUS)          # (N, 384)
    query_vec = model.encode(QUERY)             # (384,)

    # Normalize, then one matrix-vector multiply scores every document at once.
    corpus_unit = unit(corpus_vecs)             # (N, 384)
    query_unit = unit(query_vec)                # (384,)
    scores = corpus_unit @ query_unit           # (N,)  <- no Python loop

    print(f"Query: {QUERY!r}\n")
    print(f"Scored all {len(CORPUS)} docs in one numpy operation (shape {scores.shape}):\n")
    for doc, score in zip(CORPUS, scores):
        print(f"  {score:+.3f}  {doc}")

    print("\nThe 'bicycle or scooter' note scores highest -- it shares NO words")
    print("with the query, but it shares the meaning. That's semantic search.")


if __name__ == "__main__":
    main()
