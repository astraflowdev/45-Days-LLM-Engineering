# 03 — Gemini Embeddings (Free-Tier API)

Local models are great, but sometimes you want a **hosted** model — nothing to download, strong
quality, scales easily. Google's **Gemini embeddings** are free to use within generous limits.

The model: **`text-embedding-004`**, which returns a **768-number** vector.

| Property | Value |
|----------|-------|
| Provider | Google Gemini (free tier) |
| Model | `text-embedding-004` |
| Output size | **768** dimensions |
| Runs on | Google's servers (needs internet + a key) |
| API key | **yes** — free from Google AI Studio |

## Get a free key (one time)
1. Go to [Google AI Studio → API keys](https://aistudio.google.com/apikey) and create a key.
2. In this folder, make a file named `.env` (the repo's `.gitignore` already ignores it):

```bash
# .env  -- NEVER commit this
GEMINI_API_KEY=your_key_here
```

## Install (one time)
```bash
pip install google-generativeai python-dotenv
```

## What the code does
1. `load_dotenv()` reads `GEMINI_API_KEY` from your `.env`.
2. `genai.configure(api_key=...)` authenticates.
3. `genai.embed_content(model="models/text-embedding-004", content="...")` returns a dict whose
   `["embedding"]` is the 768-number vector.

```bash
python gemini_embeddings.py
```

## `task_type` — a small but important detail
Gemini lets you say how the text will be **used** so it can optimise the vector:
- `retrieval_document` — text you're **storing** (your notes, docs, chunks)
- `retrieval_query` — a **question** you're searching with

Use matching pairs (`retrieval_document` for stored text, `retrieval_query` for the question) and
your search quality goes up. You'll lean on this in Project 2.

## Gotcha
**Never hardcode your key in the `.py` file.** It always comes from the environment / `.env`. A
leaked key can run up someone else's bill — keep it out of Git.

➡ Next: [04-models-and-dimensions](../04-models-and-dimensions/)
