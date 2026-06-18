# 04 — Chain-of-Thought

For anything involving **reasoning, maths, or multiple steps**, models do much better when you let
them **think out loud** before answering. That's **chain-of-thought (CoT)**.

## The trick is tiny
Add a line like **"Let's think step by step."**

```text
Q: A shop sells pens at Rs 12 each. I buy 5 and pay with a Rs 100 note.
   How much change do I get? Let's think step by step.
```

The model writes the steps (5 × 12 = 60; 100 − 60 = 40), and the final answer is far more likely to
be right than if it blurts a number immediately.

## Why it helps
A model generates one token at a time. If it commits to an answer first, it can't "go back". Writing
the steps first gives it room to actually work the problem out.

| Task type | CoT helps? |
|-----------|:----------:|
| Arithmetic / word problems | ✅ a lot |
| Multi-step logic / planning | ✅ a lot |
| Simple lookup / classification | ➖ little (and costs tokens) |

## Getting just the final answer
CoT makes the model verbose. Two common fixes:
- Ask it to **end with** `Final answer: <x>` and parse that line.
- Or do the reasoning, then a **second** short call to extract the answer.

> Use CoT when the problem needs **steps**. Skip it for trivial tasks.

```bash
python chain_of_thought.py
```

➡ Next: [05-prompt-structure](../05-prompt-structure/)
