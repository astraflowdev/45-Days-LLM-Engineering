"""
Day 18 - Exercise 2 (STUB): Search your notes, with a confidence cutoff.

Index a list of notes, return the top-k for a query -- BUT if even the best
match scores below a threshold, say "no relevant note found" instead of
returning junk. A good search engine knows when it has no answer.

Fill in each TODO, then compare with search_your_notes_solution.py.

Setup: pip install sentence-transformers numpy
Run:   python search_your_notes.py
"""

import numpy as np
from sentence_transformers import SentenceTransformer

NOTES = [
    "Mom's birthday is on the 14th, book a cake",
    "Reset the wifi router by holding the back button for 10 seconds",
    "The gym membership renews on the 1st of every month",
    "Professor moved the algorithms exam to next Tuesday",
    "Recipe for paneer butter masala is saved in the kitchen drawer",
]

THRESHOLD = 0.25      # below this, treat it as "no good match"


def unit(vectors):
    """Scale each row to length 1 so a dot product equals cosine similarity."""
    return vectors / np.linalg.norm(vectors, axis=-1, keepdims=True)


def main():
    print("Loading model (first run downloads ~90 MB)...\n")
    model = SentenceTransformer("all-MiniLM-L6-v2")

    # TODO 1: embed all NOTES once and normalize -> notes_unit (the index)
    # notes_unit = ...

    def search(query, k=3):
        # TODO 2: embed + normalize the query, score against notes_unit
        # TODO 3: take the top-k indices (np.argsort(...)[::-1][:k])
        # TODO 4: return a list of (score, note), best first
        return []

    for query in ["when is the exam?", "how to bake bread"]:
        print(f"Query: {query!r}")
        results = search(query)
        # TODO 5: if results is empty OR the best score < THRESHOLD,
        #         print "no relevant note found"; otherwise print the ranked results.
        print()


if __name__ == "__main__":
    main()
