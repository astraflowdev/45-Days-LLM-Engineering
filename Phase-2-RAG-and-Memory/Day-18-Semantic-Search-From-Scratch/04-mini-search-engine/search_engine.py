"""
Day 18 - Step 4: A reusable SemanticSearch class + a live query loop.

Everything from steps 1-3, packaged into one object:
    engine = SemanticSearch()
    engine.add(documents)            # embed + remember (build the index)
    engine.search(query, k)          # top-k most similar, best first
Same shape as a real vector DB's add/query -- you're building a baby Chroma.

Setup: pip install sentence-transformers numpy
Run:   python search_engine.py       (type queries; 'quit' or Ctrl+C to exit)
"""

import numpy as np
from sentence_transformers import SentenceTransformer


class SemanticSearch:
    """A tiny in-memory semantic search engine over a list of documents."""

    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
        self.documents = []          # the raw text
        self.vectors = None          # (N, 384) matrix of unit-length embeddings

    def _unit(self, vectors):
        """Scale each row to length 1 so a dot product equals cosine similarity."""
        return vectors / np.linalg.norm(vectors, axis=-1, keepdims=True)

    def add(self, documents):
        """Embed new documents once and append them to the index."""
        new_vecs = self._unit(self.model.encode(documents))
        self.documents.extend(documents)
        # Stack onto whatever we already have, so add() can be called repeatedly.
        self.vectors = new_vecs if self.vectors is None else np.vstack([self.vectors, new_vecs])

    def search(self, query, k=3):
        """Return the k documents most similar to query as (score, document), best first."""
        query_unit = self._unit(self.model.encode(query))
        scores = self.vectors @ query_unit            # one score per document
        order = np.argsort(scores)[::-1][:k]          # best k indices, high score first
        return [(float(scores[i]), self.documents[i]) for i in order]


CORPUS = [
    "Buy milk and eggs from the market",
    "A bicycle or scooter is a cheap way to commute to college",
    "Finish the data structures assignment by Friday",
    "Recipe: boil rice, then add dal and spices",
    "Book train tickets for the Diwali trip home",
    "The local bus pass costs 300 rupees a month",
    "Make chai with ginger and cardamom in the morning",
    "Submit the physics lab report before the deadline",
]


def main():
    print("Loading model (first run downloads ~90 MB)...\n")
    engine = SemanticSearch()
    engine.add(CORPUS)
    print(f"Indexed {len(CORPUS)} documents. Type a query (or 'quit').\n")

    while True:
        try:
            query = input("search> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nbye!")
            break
        if not query:
            continue
        if query.lower() in {"quit", "exit"}:
            print("bye!")
            break
        for rank, (score, doc) in enumerate(engine.search(query, k=3), start=1):
            print(f"  #{rank}  {score:+.3f}  {doc}")
        print()


if __name__ == "__main__":
    main()
