# Day 16 — Exercises

Put embeddings to work. Both exercises use the free local model from module 02, so no API key is
needed.

```bash
pip install sentence-transformers
```

Try each yourself first, then check the `*_solution.py` file.

---

## Exercise 1 — Find the closest sentence 🔎
Given a **query** and a list of **candidate** sentences, use embeddings to find which candidate is
closest in **meaning** to the query — even when they share no words.

**Your task:** in `closest_sentence.py`, embed the query and the candidates, score each candidate
with `util.cos_sim(...)`, print every candidate with its score, and print the best match.

*Hint:* `util.cos_sim(query_emb, candidate_embs)` returns a `1 x N` tensor; `.tolist()[0]` gives a
plain list of scores. The right answer shares **no keywords** with the query — that's the point.

➡ Solution: [`closest_sentence_solution.py`](closest_sentence_solution.py)

---

## Exercise 2 — Odd one out 🧩
Given a list of sentences where most are about one topic and one is not, use embeddings to find the
**odd one out** — the sentence least similar to the rest.

**Your task:** in `odd_one_out.py`, embed all sentences, build the `N x N` similarity matrix with
`util.cos_sim(embs, embs)`, compute each sentence's **average** similarity to the *others* (skip its
own self-score of 1.0), and print the sentence with the lowest average.

*Hint:* loop over each row; for row `i`, average the scores at positions `j != i`.

➡ Solution: [`odd_one_out_solution.py`](odd_one_out_solution.py)
