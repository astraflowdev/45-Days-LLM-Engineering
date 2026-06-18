"""
What an embedding is -- a tiny, hand-made illustration (no model, no installs).

We fake 3 "meaning" dimensions and score how close words are. Real embeddings
(modules 02-04) come from a trained model and have hundreds of dimensions, but
the idea is exactly this: similar meaning -> vectors that point the same way.

Run:
    python what_are_embeddings.py
"""

from math import sqrt

# Pretend each word is described by 3 hand-picked "meaning" features:
#   [ is_animal , is_food , is_royal ]
# A real model LEARNS these numbers automatically from billions of sentences;
# here we just set them by hand so you can see what is going on.
vectors = {
    "cat":    [0.90, 0.10, 0.00],
    "dog":    [0.90, 0.10, 0.00],
    "tiger":  [0.95, 0.00, 0.20],
    "samosa": [0.00, 0.95, 0.00],
    "king":   [0.10, 0.00, 0.95],
}


def closeness(a, b):
    """Cosine similarity: 1.0 = same direction (same meaning), 0.0 = unrelated.

    You'll build this from scratch on Day 17 -- for now just trust the score.
    """
    dot = sum(x * y for x, y in zip(a, b))
    mag_a = sqrt(sum(x * x for x in a))
    mag_b = sqrt(sum(y * y for y in b))
    return dot / (mag_a * mag_b)


print("Each word is a vector (a list of numbers):")
for word, vec in vectors.items():
    print(f"  {word:7} -> {vec}")

print()
print("How close in meaning (1.0 = identical direction):")
pairs = [("cat", "dog"), ("cat", "tiger"), ("cat", "samosa"), ("king", "samosa")]
for a, b in pairs:
    score = closeness(vectors[a], vectors[b])
    print(f"  {a:7} vs {b:7} -> {score:.2f}")

print()
print("Notice: cat~dog and cat~tiger score high; cat~samosa is near 0.")
print("That is the whole idea of embeddings: similar meaning -> nearby vectors.")
