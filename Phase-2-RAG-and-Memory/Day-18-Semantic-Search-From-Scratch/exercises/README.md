# Day 18 — Exercises

Put today's loop to work: **embed a corpus once → score a query → return the best match(es).** Both
use the **local** model (`all-MiniLM-L6-v2`) and the vectorized cosine from the modules — no API key.

Fill in the `# TODO`s in each stub, then check against the `_solution.py`.

```bash
pip install -r requirements.txt        # numpy, sentence-transformers
```

## 1. FAQ answer bot — `faq_bot.py`
A support bot has a fixed list of **FAQ question → answer** pairs. A user types a question in their
*own* words; you must return the answer to the **closest** stored FAQ.

- Embed all the FAQ **questions** once (your corpus).
- Embed the user's question, score it against every FAQ question, take the **best** one.
- Print the matched FAQ question, its **answer**, and the similarity score.

**Try this:** user asks `"how do I get my money back?"` → should match the FAQ about **refunds**,
even though it never says "money back". Meaning over keywords, doing real work.

➡ Solution: [`faq_bot_solution.py`](faq_bot_solution.py)

## 2. Search your notes (with a confidence cutoff) — `search_your_notes.py`
Index a list of personal notes and return the top-k for a query — **but** add a **threshold**: if even
the best match scores below a cutoff (say `0.25`), say *"no relevant note found"* instead of returning
a weak result.

- Build the index (embed all notes once).
- For a query, get the top-k scored notes.
- If the top score is below the threshold, print a "nothing relevant" message instead.

This teaches a real production habit: **a search engine should know when it has *no* good answer**
rather than confidently returning junk. (Tomorrow's vector DB returns scores too — same idea.)

➡ Solution: [`search_your_notes_solution.py`](search_your_notes_solution.py)

➡ Back to [Day 18](../README.md).
