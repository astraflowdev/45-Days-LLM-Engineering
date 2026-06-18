# 02 — Tokens & Tokenization

LLMs don't read words or letters — they read **tokens**. A token is a chunk of text, often a word
or part of a word. Roughly: **1 token ≈ 4 characters ≈ ¾ of a word** in English.

```text
"I love samosas"  ->  ["I", " love", " samos", "as"]   (about 4 tokens)
```

Why you must care:
| Tokens decide… | Because |
|----------------|---------|
| **Cost** | APIs bill per token (in + out) |
| **Limits** | the context window is measured in tokens |
| **Speed** | more tokens = slower responses |

## Counting tokens
Gemini can count tokens for you before you send a request:

```python
model = genai.GenerativeModel("gemini-2.0-flash")
print(model.count_tokens("How many tokens is this?").total_tokens)
```

## Things that surprise beginners
- **Spaces and punctuation** are part of tokens too.
- **Non-English** text (e.g. Hindi in Devanagari) often uses **more** tokens per word.
- Numbers and code can tokenize oddly — never assume "1 word = 1 token".

Run it (needs `GEMINI_API_KEY`):

```bash
python count_tokens.py
```

➡ Next: [03-context-windows](../03-context-windows/)
