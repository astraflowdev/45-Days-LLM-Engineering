"""
Solution -- Exercise 2: Odd one out.

Run: python odd_one_out_solution.py
"""

from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

sentences = [
    "Python is a great language for AI.",
    "Machine learning models learn from data.",
    "Neural networks power modern AI.",
    "I had chai and samosa for breakfast.",
]

# 1) Embed every sentence.
embs = model.encode(sentences)

# 2) N x N similarity matrix: sim[i][j] = how close sentence i is to sentence j.
sim = util.cos_sim(embs, embs).tolist()

# 3) For each sentence, average its similarity to the OTHERS (skip its own 1.0).
averages = []
for i, row in enumerate(sim):
    others = [score for j, score in enumerate(row) if j != i]
    averages.append(sum(others) / len(others))

# 4) Show the averages and the odd one out (lowest average similarity).
print("Average similarity to the other sentences:")
for sentence, avg in zip(sentences, averages):
    print(f"  {avg:.3f}  {sentence}")

odd_sentence, _ = min(zip(sentences, averages), key=lambda pair: pair[1])
print()
print("Odd one out:", odd_sentence)
print()
print("The 'chai and samosa' line is about food, not AI, so its vector sits far")
print("from the others -- and the average similarity score catches it.")
