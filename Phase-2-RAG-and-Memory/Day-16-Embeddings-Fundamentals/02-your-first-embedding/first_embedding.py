"""
Your first real embedding -- local and free with sentence-transformers.

Downloads a small model once (~90 MB), then runs on CPU offline. No API key.

Setup (one time):
    pip install sentence-transformers
Run:
    python first_embedding.py
"""

from sentence_transformers import SentenceTransformer

# all-MiniLM-L6-v2: small, fast, free. Maps any text -> a 384-number vector.
# Loading the model the first time downloads it; after that it is cached.
model = SentenceTransformer("all-MiniLM-L6-v2")

sentences = [
    "I love learning about AI.",
    "Machine learning is fascinating.",
    "The samosa was crispy and hot.",
]

# encode() turns each sentence into its embedding vector.
# Pass a LIST -> you get a 2-D NumPy array: one row (vector) per sentence.
embeddings = model.encode(sentences)

print("Number of sentences:", len(sentences))
print("Shape of embeddings:", embeddings.shape)        # (3, 384)
print("Each sentence -> a vector of", embeddings.shape[1], "numbers")

print()
print("First 8 numbers of sentence 1's embedding:")
print(embeddings[0][:8])

print()
print("These raw numbers are not meant to be read by humans.")
print("What matters: similar sentences get similar vectors (see the exercise).")
