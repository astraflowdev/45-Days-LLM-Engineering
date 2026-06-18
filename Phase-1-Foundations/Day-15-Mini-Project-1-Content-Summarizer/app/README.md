# AI Content Summarizer

Summarize a PDF, an article URL, or pasted text into a **TL;DR + key points + action items**.
Built with Streamlit + Gemini (free tier).

## Run locally
```bash
pip install -r requirements.txt
cp .env.example .env        # add your GEMINI_API_KEY
streamlit run app.py
```

## How it works
- `loaders.py` — turns PDF / URL / text into clean text
- `summarizer.py` — Gemini in JSON mode → a validated Pydantic `Summary` (with retries)
- `app.py` — the Streamlit UI (it only calls `summarize(text)`)

## Deploy
See [`../DEPLOY.md`](../DEPLOY.md) for Hugging Face Spaces and Streamlit Community Cloud steps. Set
`GEMINI_API_KEY` as a **secret** in the hosting platform — never commit it.

## Tech
Python · Streamlit · google-generativeai · Pydantic · pdfplumber · BeautifulSoup
