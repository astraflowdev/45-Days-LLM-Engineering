"""
Day 18 - Exercise 1 (SOLUTION): FAQ answer bot.

Embed the FAQ questions once, embed the user's question, score with cosine,
and return the answer for the closest FAQ. "how do I get my money back?"
matches the refund FAQ with no shared keywords -- meaning wins.

Setup: pip install sentence-transformers numpy
Run:   python faq_bot_solution.py
"""

import numpy as np
from sentence_transformers import SentenceTransformer

FAQ = [
    ("How do I reset my password?",
     "Go to Settings > Security > Reset Password and follow the email link."),
    ("What is your refund policy?",
     "Refunds are available within 30 days of purchase, no questions asked."),
    ("How long does shipping take?",
     "Standard shipping takes 3-5 business days within India."),
    ("Do you offer student discounts?",
     "Yes -- students get 20% off with a valid college ID."),
]

USER_QUESTION = "how do I get my money back?"


def unit(vectors):
    """Scale each row to length 1 so a dot product equals cosine similarity."""
    return vectors / np.linalg.norm(vectors, axis=-1, keepdims=True)


def main():
    print("Loading model (first run downloads ~90 MB)...\n")
    model = SentenceTransformer("all-MiniLM-L6-v2")

    questions = [q for q, a in FAQ]

    faq_unit = unit(model.encode(questions))           # corpus, embedded once
    query_unit = unit(model.encode(USER_QUESTION))     # the user's question
    scores = faq_unit @ query_unit                     # one score per FAQ

    best = int(np.argmax(scores))                      # index of the closest FAQ
    matched_q, answer = FAQ[best]

    print(f"User asked: {USER_QUESTION!r}\n")
    print(f"Closest FAQ (score {scores[best]:+.3f}): {matched_q!r}")
    print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
