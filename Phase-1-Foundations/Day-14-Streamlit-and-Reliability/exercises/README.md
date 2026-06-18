# Day 14 — Exercises

```bash
pip install streamlit google-generativeai python-dotenv   # + GEMINI_API_KEY in .env
```

---

## Exercise 1 — Ask-anything Streamlit app 🤖
Build a tiny web app: a text box, a button, and the model's answer — with a retry wrapper so a blip
doesn't crash it.

**Your task:** in `ask_app.py`, add a `st.text_area` for the question and a button; on click, call
Gemini **through a retry helper** and show the answer with `st.write`. Show a spinner while it runs
(`with st.spinner(...)`).

Run with: `streamlit run ask_app.py`

➡ Solution: [`ask_app_solution.py`](ask_app_solution.py)

---

## Exercise 2 — Token & cost readout 💰
Add transparency to the app.

**Your task:** in the solution app (or your own), after each answer also display the **prompt tokens,
output tokens, and total** from `response.usage_metadata` using `st.metric` or `st.caption`. (Stretch:
multiply by an illustrative price to show an estimated cost.)

➡ See it wired in [`ask_app_solution.py`](ask_app_solution.py).
