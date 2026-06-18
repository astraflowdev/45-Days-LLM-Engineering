"""
Gemini embeddings -- free-tier API (768 dimensions).

Get a free key at https://aistudio.google.com/apikey, then put it in a .env file
in this folder:
    GEMINI_API_KEY=your_key_here

Setup (one time):
    pip install google-generativeai python-dotenv
Run:
    python gemini_embeddings.py
"""

import os

from dotenv import load_dotenv
import google.generativeai as genai

# Reads GEMINI_API_KEY from a .env file (in this folder or a parent).
load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    # Fail clearly instead of with a confusing library error.
    raise SystemExit("Set GEMINI_API_KEY in a .env file first (see the README).")

genai.configure(api_key=api_key)

# text-embedding-004 is Google's free embedding model -> 768-number vectors.
result = genai.embed_content(
    model="models/text-embedding-004",
    content="I love learning about AI.",
    task_type="retrieval_document",   # how the text will be used (see README)
)

embedding = result["embedding"]

print("Model: text-embedding-004")
print("Embedding length:", len(embedding))   # 768
print("First 8 numbers:", [round(x, 4) for x in embedding[:8]])

print()
print("Same idea as the local model -- text in, a vector out -- just 768 dims")
print("and computed on Google's servers instead of your laptop.")
