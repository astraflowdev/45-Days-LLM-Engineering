# Day 15 — Mini-Project 1: AI Content Summarizer 🚀

This is your **first shipped product**. It ties together everything from Days 8–14: load data, prompt
an LLM, get structured output, wrap it in a UI, make it reliable — and **deploy it to a public URL**.

## What you're building
An **AI Content Summarizer**:
- **Input:** a PDF upload, an article URL, or pasted text
- **Output:** a structured summary — a one-line **TL;DR**, **key points**, and **action items**
- **Stack:** Streamlit + Gemini + Python (all free tier)
- **Deployed:** free on Hugging Face Spaces or Streamlit Community Cloud

## Where each day shows up
| From | Used for |
|------|----------|
| Day 8 | Pydantic models, dotenv for the key |
| Day 9 | the Gemini call |
| Day 11 | JSON mode + validated structured output |
| Day 13 | PDF / URL / text loaders + cleaning |
| Day 14 | Streamlit UI, retries, spinner |

## The repo layout
```
Day-15.../
├── README.md            <- you are here (brief + build plan)
├── 01-architecture/     <- how the app is wired (data flow)
├── app/                 <- the complete, deployable app
│   ├── app.py           <- Streamlit UI
│   ├── summarizer.py    <- Gemini + Pydantic structured summary
│   ├── loaders.py       <- PDF / URL / text -> clean text
│   ├── requirements.txt
│   ├── .env.example
│   └── README.md        <- the app's own README (for the deploy repo/Space)
└── DEPLOY.md            <- step-by-step deploy guide
```

## Run it locally
```bash
cd app
pip install -r requirements.txt
cp .env.example .env      # then put your GEMINI_API_KEY in .env
streamlit run app.py
```

## Build plan (the 45-min independent block, x a few sessions)
1. Read `01-architecture/`.
2. Get `summarizer.py` returning a validated `Summary` for pasted text.
3. Add the loaders (PDF, URL).
4. Wire the Streamlit UI in `app.py`.
5. Add retries + a spinner + token readout.
6. **Deploy** (see `DEPLOY.md`) and record a ~2-min demo.

## Deliverables (for the phase)
- ✅ Deployed app at a public URL
- ✅ Public GitHub repo with a polished README
- ✅ ~2-min demo video
- ✅ Works on all three inputs (PDF, URL, text)

➡ Next: **Phase 2 — RAG & Memory** (Day 16: embeddings).
