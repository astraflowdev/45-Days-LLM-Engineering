"""
Exercise 2 -- Odd one out.

Most of these sentences are about one topic; one is not. Use embeddings to find
the sentence least similar to the rest.

Setup: pip install sentence-transformers
Run:   python odd_one_out.py
"""

from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

sentences = [
    "Python is a great language for AI.",
    "Machine learning models learn from data.",
    "Neural networks power modern AI.",
    "I had chai and samosa for breakfast.",
]

# TODO 1: embed all sentences with model.encode(...)
# TODO 2: build the N x N similarity matrix with util.cos_sim(embs, embs).tolist()
# TODO 3: for each sentence i, average its similarity to the OTHERS (skip j == i)
# TODO 4: print each sentence with its average, then print the lowest (the odd one out)
