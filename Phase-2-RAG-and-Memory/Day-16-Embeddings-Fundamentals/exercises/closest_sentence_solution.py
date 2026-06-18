"""
Solution -- Exercise 1: Find the closest sentence (semantic match).

Run: python closest_sentence_solution.py
"""

from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

query = "How do I keep my code in version control?"
candidates = [
    "Git lets you track changes and collaborate.",
    "Samosas taste best when fresh and hot.",
    "Python is a popular programming language.",
]

# 1) Turn the query and candidates into embedding vectors.
query_emb = model.encode(query)
candidate_embs = model.encode(candidates)

# 2) cos_sim gives a 1 x N tensor of similarity scores (1.0 = identical meaning).
scores = util.cos_sim(query_emb, candidate_embs).tolist()[0]

# 3) Show each candidate's score and the winner.
print("Query:", query)
print()
for sentence, score in zip(candidates, scores):
    print(f"  {score:.3f}  {sentence}")

best_sentence, best_score = max(zip(candidates, scores), key=lambda pair: pair[1])
print()
print("Closest match:", best_sentence)
print()
print("Notice the 'Git...' line wins even though it shares NO words with the")
print("query. That is semantic search -- matching by meaning, powered by embeddings.")
