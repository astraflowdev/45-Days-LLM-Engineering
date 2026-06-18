# Day 14 — Streamlit Crash Course + Reliability

Two things stand between your code and a **real product**: a **UI** people can use, and **reliability**
so it doesn't fall over on a rate limit. Today you get both — then tomorrow you ship Mini-Project 1.

## Learning objectives
By the end of today you can:
- Build a web UI in pure Python with **Streamlit**
- Use **widgets** and **session state** for interactivity
- Handle errors with **retries + backoff**
- Respect **rate limits** and track **cost**
- **Stream** responses so the UI feels fast

## Modules (work through them in order)

| # | Module | What it covers |
|--:|--------|----------------|
| 01 | [streamlit-basics](01-streamlit-basics/) | Your first Streamlit app |
| 02 | [widgets-and-state](02-widgets-and-state/) | Inputs, buttons, `st.session_state` |
| 03 | [error-handling-and-retries](03-error-handling-and-retries/) | Retry with exponential backoff |
| 04 | [rate-limits-and-cost](04-rate-limits-and-cost/) | Stay under limits; estimate spend |
| 05 | [streaming-responses](05-streaming-responses/) | Show tokens as they arrive |

Then practise in **[exercises/](exercises/)**.

## Setup
```bash
pip install -r requirements.txt        # streamlit, google-generativeai, python-dotenv
```

## How to run
Streamlit apps launch with **`streamlit run`**, not `python`:
```bash
streamlit run 01-streamlit-basics/hello_app.py
```
The pure-Python modules (03, 04) still run with `python`.

## Today's exercise
Build a small **AI ask-anything** Streamlit app with retries and a token/cost readout. See
[`exercises/`](exercises/).

➡ Next (Day 15): **Mini-Project 1** — build + deploy + demo the AI Content Summarizer.
