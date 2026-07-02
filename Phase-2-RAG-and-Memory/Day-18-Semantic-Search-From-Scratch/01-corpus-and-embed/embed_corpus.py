"""
Day 18 - Step 1: Embed a whole corpus once into a matrix.

A "corpus" is all the documents you want to search. We embed the entire
list in ONE call and get back an (N x 384) matrix -- row i is docs[i].
That matrix is the searchable knowledge base for the rest of today.

Setup: pip install sentence-transformers numpy
Run:   python embed_corpus.py
"""

from sentence_transformers import SentenceTransformer

# Our tiny "knowledge base" -- five everyday notes (the corpus).
CORPUS = [
    "Buy milk and eggs from the market",
    "A bicycle or scooter is a cheap way to commute",
    "Finish the data structures assignment by Friday",
    "Recipe: boil rice, then add dal and spices",
    "Book train tickets for the Diwali trip home",
]


def main():
    print("Loading model (first run downloads ~90 MB)...\n")
    model = SentenceTransformer("all-MiniLM-L6-v2")

    # ONE call embeds the whole list -> a matrix, one row per document.
    vectors = model.encode(CORPUS)

    print(f"Corpus has {len(CORPUS)} documents.")
    print(f"Embedding matrix shape: {vectors.shape}   (rows = documents, cols = 384 features)\n")

    # Each row of the matrix lines up with each document.
    for i, doc in enumerate(CORPUS):
        row = vectors[i]
        print(f"  row {i}: shape {row.shape}  first 3 numbers {row[:3].round(3)}  <- {doc!r}")

    print("\nThis (N x 384) matrix IS our searchable knowledge base.")
    print("Next: embed a query and compare it to every row at once.")


if __name__ == "__main__":
    main()
