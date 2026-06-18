"""
Models & dimensions -- vector size and what "normalized" means.

Uses the local sentence-transformers model (no API key). Shows the vector size
and how normalizing scales a vector's length to exactly 1.0 (same direction).

Setup (one time):
    pip install sentence-transformers numpy
Run:
    python models_and_dimensions.py
"""

import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
text = "Retrieval-augmented generation needs good embeddings."

# Raw embedding: 384 numbers; its length (magnitude) is some arbitrary value.
raw = model.encode(text)
print("Dimensions (all-MiniLM-L6-v2):", raw.shape[0])               # 384
print("Raw vector length:", round(float(np.linalg.norm(raw)), 4))

# Normalized embedding: same DIRECTION (meaning), length scaled to exactly 1.0.
# Most similarity math assumes unit-length vectors, so this matters a lot.
unit = model.encode(text, normalize_embeddings=True)
print("Normalized vector length:", round(float(np.linalg.norm(unit)), 4))  # 1.0

print()
print("Different models = different sizes AND different vector 'spaces':")
print("  all-MiniLM-L6-v2 (local)  -> 384 dims")
print("  Gemini text-embedding-004 -> 768 dims")
print("Rule: only compare vectors made by the SAME model. Never mix the two.")
