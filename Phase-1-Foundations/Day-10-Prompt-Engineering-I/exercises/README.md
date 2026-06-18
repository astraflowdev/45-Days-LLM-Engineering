# Day 10 — Exercises

```bash
pip install google-generativeai python-dotenv   # + GEMINI_API_KEY in .env
```

---

## Exercise 1 — Few-shot sentiment classifier 🎯
Build a classifier that always replies with one of three labels.

**Your task:** in `sentiment_classifier.py`, write a **few-shot** prompt (3 examples) that classifies
a review as `positive`, `negative`, or `neutral`, then classify three new reviews and print each
label. Keep the format identical across examples.

➡ Solution: [`sentiment_classifier_solution.py`](sentiment_classifier_solution.py)

---

## Exercise 2 — Word-problem solver (chain-of-thought) 🧮
Use chain-of-thought to solve a multi-step maths word problem reliably.

**Your task:** in `word_problem.py`, send a word problem with "Let's think step by step" and ask the
model to end with `Final answer: <x>`. Print the full reasoning, then extract and print just the
final-answer line.

*Hint:* split the text on lines and find the one starting with "Final answer".

➡ Solution: [`word_problem_solution.py`](word_problem_solution.py)
