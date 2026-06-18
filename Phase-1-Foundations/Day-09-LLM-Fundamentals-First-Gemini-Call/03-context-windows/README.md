# 03 — Context Windows

The **context window** is the maximum number of tokens a model can handle **at once** — and it
covers *both* your input **and** its output:

```text
context window  =  prompt tokens  +  answer tokens
```

If you blow past it, the API errors (or silently drops text). Modern Gemini models have very large
windows (hundreds of thousands of tokens), but it still matters:

| Why it matters | Even with a big window |
|----------------|------------------------|
| Cost | you pay for every token in the window |
| Speed | bigger prompts = slower replies |
| Quality | models can "lose" details buried in a huge prompt |

## The practical rules
1. **Count before you send** (module 02) when stuffing in a big document.
2. **Leave room for the answer** — if the answer needs ~1,000 tokens, don't fill the window to the brim.
3. When a document is too big, you **chunk + retrieve** only the relevant parts — that's **RAG**,
   the whole of Phase 2.

## A mental model
Think of the context window as the model's **short-term memory / desk space**. It can only look at
what's on the desk right now. It has no memory of past calls unless *you* send the history again.

This script estimates how many copies of a paragraph would fit in a window and shows the
"leave room for the answer" idea.

```bash
python context_budget.py
```

➡ Next: [04-temperature-and-sampling](../04-temperature-and-sampling/)
