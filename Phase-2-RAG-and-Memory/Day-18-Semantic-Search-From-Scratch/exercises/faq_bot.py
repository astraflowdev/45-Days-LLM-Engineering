"""
Day 18 - Exercise 1 (STUB): FAQ answer bot.

Match a user's free-text question to the closest stored FAQ question,
then return that FAQ's answer. Embed the FAQ questions once, score the
user's question against them, pick the best.

Fill in each TODO, then compare with faq_bot_solution.py.

Setup: pip install sentence-transformers numpy
Run:   python faq_bot.py
"""

import numpy as np
from sentence_transformers import SentenceTransformer

# (question, answer) pairs -- our knowledge base.
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

    # TODO 1: embed all FAQ questions (the corpus) and normalize -> faq_unit
    # faq_unit = ...

    # TODO 2: embed and normalize the user's question -> query_unit
    # query_unit = ...

    # TODO 3: score the user's question against every FAQ question (one matrix-vector multiply)
    # scores = ...

    # TODO 4: find the index of the BEST match (hint: np.argmax)
    # best = ...

    # TODO 5: print the matched question, its answer (FAQ[best][1]), and the score
    print("Fill in the TODOs to answer:", repr(USER_QUESTION))


if __name__ == "__main__":
    main()
