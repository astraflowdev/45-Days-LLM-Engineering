# Day 18 — Exercises

Use Chroma for real retrieval, not just in the walkthrough.

Fill in the `# TODO`s in each stub, then compare with the `_solution.py`.

```bash
pip install -r requirements.txt
```

## 1. FAQ retrieval bot — `faq_bot.py`
Store a small FAQ inside Chroma, then retrieve the closest answer for a user's question.

- embed the FAQ questions
- upsert them into a Chroma collection
- query the collection with a new user question
- print the matched answer and the retrieved FAQ question

**Try this:** `how do I get my payment back?` should retrieve the refund FAQ.

➡ Solution: [`faq_bot_solution.py`](faq_bot_solution.py)

## 2. Notes chat assistant — `search_your_notes.py`
Build a tiny RAG loop:

- store notes in Chroma
- retrieve the top 2 relevant notes for a question
- send those notes to Groq
- print the grounded answer

Add a fallback: if retrieval looks weak, tell the user you do not have enough notes instead of
hallucinating.

➡ Solution: [`search_your_notes_solution.py`](search_your_notes_solution.py)

➡ Back to [Day 18](../README.md).
