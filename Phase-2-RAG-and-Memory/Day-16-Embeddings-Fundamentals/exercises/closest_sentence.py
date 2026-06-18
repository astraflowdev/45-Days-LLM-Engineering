"""
Exercise 1 -- Find the closest sentence (semantic match).

Given a query and candidate sentences, use embeddings to find which candidate is
closest in MEANING to the query (not just matching words).

Setup: pip install sentence-transformers
Run:   python closest_sentence.py
"""

from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

query = "How do I keep my code in version control?"
candidates = [
    "Git lets you track changes and collaborate.",
    "Samosas taste best when fresh and hot.",
    "Python is a popular programming language.",
]

# TODO 1: embed the query and the candidates with model.encode(...)
# TODO 2: score each candidate with util.cos_sim(query_emb, candidate_embs)
#         (it returns a 1 x N tensor; .tolist()[0] gives a plain list)
# TODO 3: print each candidate with its score, then print the best match
