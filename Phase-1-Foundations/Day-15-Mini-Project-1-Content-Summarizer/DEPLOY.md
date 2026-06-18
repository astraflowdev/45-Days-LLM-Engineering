# Deploy Guide — Mini-Project 1

Two free options. Both need your `GEMINI_API_KEY` set as a **secret** on the platform (never commit
`.env`).

---

## Option A — Streamlit Community Cloud (easiest)
1. Push the `app/` contents to a **public GitHub repo** (with `app.py` and `requirements.txt`).
2. Go to [share.streamlit.io](https://share.streamlit.io) → **New app** → pick the repo/branch and
   `app.py`.
3. In **Advanced settings → Secrets**, add:
   ```toml
   GEMINI_API_KEY = "your_key_here"
   ```
   (Streamlit secrets are read by `os.environ` too, so the app needs no change.)
4. Deploy. You get a public `*.streamlit.app` URL.

---

## Option B — Hugging Face Spaces
1. Create a new **Space** at [huggingface.co/new-space](https://huggingface.co/new-space) → SDK:
   **Streamlit**.
2. Upload `app.py`, `summarizer.py`, `loaders.py`, and `requirements.txt`.
3. In **Settings → Variables and secrets**, add a secret `GEMINI_API_KEY`.
4. The Space builds and serves a public URL automatically.

---

## Pre-flight checklist
- [ ] `.env` is **git-ignored** (the key is a platform secret, not in the repo)
- [ ] `requirements.txt` lists every import
- [ ] App runs locally with `streamlit run app.py`
- [ ] Tested all three inputs (PDF, URL, text)
- [ ] README has a screenshot + the live URL

## Demo (the "+ demo" part)
Record a ~2-minute walkthrough (Loom / phone screen-record): paste an article, click Summarize, show
the TL;DR + key points + action items. Add the link to your README and LinkedIn.
