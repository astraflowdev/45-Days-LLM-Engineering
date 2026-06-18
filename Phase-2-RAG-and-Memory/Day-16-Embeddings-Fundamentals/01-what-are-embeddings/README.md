# 01 — What Are Embeddings?

An **embedding** is a list of numbers (a *vector*) that represents the **meaning** of a piece of
text. A model reads "I love samosas" and turns it into something like `[0.12, -0.4, 0.88, …]` —
hundreds of numbers. The magic rule:

> **Text with similar meaning → vectors that point in a similar direction.**

That one property is what makes search, recommendations, and RAG work. "How do I track my code?"
and "version control with Git" share almost no words, but their vectors land close together — so a
computer can tell they *mean* the same thing.

## Why this matters for the rest of Phase 2
| Step | What embeddings do |
|------|--------------------|
| Store your docs | Each chunk of text → a vector, saved in a vector database |
| Ask a question | Your question → a vector |
| Find the answer | Return the chunks whose vectors are **closest** to the question's vector |

This "match by meaning" is called **semantic search**, and it's the heart of a RAG system.

## A tiny, fake illustration
Real embeddings come from a trained model (you'll use one in module 02). To build intuition, the
script hand-makes 3 "meaning" dimensions — `[is_animal, is_food, is_royal]` — and scores how close
words are:

```text
cat     vs dog     -> 1.00   (both animals)
cat     vs tiger   -> 0.98   (both animals)
cat     vs samosa  -> 0.11   (animal vs food)
king    vs samosa  -> 0.00   (royal vs food)
```

The closeness score above is **cosine similarity** (1.0 = same direction, 0.0 = unrelated). You'll
build it properly from scratch on **Day 17** — here just see the idea in action.

Run it (no installs needed):

```bash
python what_are_embeddings.py
```

➡ Next: [02-your-first-embedding](../02-your-first-embedding/)
