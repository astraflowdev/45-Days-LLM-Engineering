# 03 — Few-Shot Prompting

**Few-shot** = you include a few **examples** of input → output in the prompt. The model copies the
pattern. This is the single most reliable way to lock **format** and **style**.

```text
Classify the sentiment. Reply with one word.

Review: "Loved it, will come again!"   Sentiment: positive
Review: "Worst service ever."          Sentiment: negative
Review: "It was okay, nothing special." Sentiment: neutral
Review: "The food was cold and late."  Sentiment:
```

The model sees three examples, then completes the fourth — in exactly the same shape.

## Why it works so well
| Few-shot fixes | How |
|----------------|-----|
| Inconsistent format | examples *show* the exact format |
| Wrong label set | examples define the allowed answers |
| Edge-case handling | include a tricky example on purpose |

## Good few-shot habits
- **2–5 examples** is usually plenty (more costs tokens for little gain).
- Make examples **diverse** and **correct** — the model copies mistakes too.
- Keep the **format identical** across examples (same labels, same layout).
- Put the real input **last**, in the same shape, with the answer blank.

```bash
python few_shot.py
```

➡ Next: [04-chain-of-thought](../04-chain-of-thought/)
