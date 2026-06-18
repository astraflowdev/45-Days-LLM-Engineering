# 05 — Prompt Structure: The Anatomy of a Good Prompt

Most "the model won't listen" problems are really **vague prompt** problems. A well-structured prompt
has clear parts and clear boundaries.

## The building blocks
| Part | Purpose |
|------|---------|
| **Role** | who the model is ("You are a resume reviewer.") |
| **Task** | exactly what to do |
| **Context / input** | the data to work on |
| **Format** | the shape of the output |
| **Constraints** | length, tone, what to avoid |

## Use delimiters
Wrap user/data text in clear markers so the model can't confuse instructions with content:

```text
Summarize the review between <review> tags in one sentence.

<review>
{the actual review text}
</review>
```

Delimiters (`<tags>`, triple quotes, `###`) also reduce **prompt injection** — text inside the data
is less likely to be treated as a new instruction (more on that in Phase 3).

## Be specific, not polite
The model doesn't need "please" — it needs **precision**. Compare:
- ❌ "Tell me about this product."
- ✅ "In 3 bullet points, list this product's key features for a buyer. Max 12 words each."

## A reusable template
The script builds a prompt from these parts with `str.format(...)` — the start of a prompt template
library (you'll grow this all course).

```bash
python prompt_template.py
```

➡ Next: practise in [../exercises/](../exercises/)
