"""
Day 18 - Exercise 2 (SOLUTION): Search your notes, with a confidence cutoff.

Index the notes once, score a query, return the top-k -- but if even the
best score is below THRESHOLD, report "no relevant note found" instead of
surfacing a weak, misleading result. "how to bake bread" has no good match
here, so the cutoff catches it.

Setup: pip install sentence-transformers numpy
Run:   python search_your_notes_solution.py
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

    notes_unit = unit(model.encode(NOTES))             # embed the index once

    def search(query, k=3):
        query_unit = unit(model.encode(query))
        scores = notes_unit @ query_unit
        order = np.argsort(scores)[::-1][:k]           # best k, high score first
        return [(float(scores[i]), NOTES[i]) for i in order]

    for query in ["when is the exam?", "how to bake bread"]:
        print(f"Query: {query!r}")
        results = search(query)

        # A good search engine knows when it has nothing relevant.
        if not results or results[0][0] < THRESHOLD:
            print(f"  no relevant note found (best score < {THRESHOLD})")
        else:
            for rank, (score, note) in enumerate(results, start=1):
                flag = "" if score >= THRESHOLD else "  (weak)"
                print(f"  #{rank}  {score:+.3f}  {note}{flag}")
        print()


if __name__ == "__main__":
    main()
