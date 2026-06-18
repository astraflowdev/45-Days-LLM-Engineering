# 01 — Streamlit Basics

**Streamlit** turns a Python script into a web app — no HTML, CSS, or JavaScript. You write top-to-
bottom Python; Streamlit renders it in the browser and **re-runs the whole script** on every
interaction.

```python
import streamlit as st

st.title("My First AI App")
st.write("Hello! This is a web app written in pure Python.")
name = st.text_input("Your name")
if name:
    st.success(f"Welcome, {name}!")
```

## The core display calls
| Call | Shows |
|------|-------|
| `st.title` / `st.header` | headings |
| `st.write` | almost anything (text, data, charts) |
| `st.markdown` | formatted markdown |
| `st.success` / `st.error` / `st.info` | colored status boxes |

## The mental model
> Streamlit **re-runs your whole script** from top to bottom every time the user interacts. That's
> what makes it simple — and why **session state** (module 02) matters for remembering things.

## Run it
```bash
streamlit run hello_app.py
```
It opens at `http://localhost:8501`. (Don't use `python hello_app.py` — Streamlit needs its own
runner.)

➡ Next: [02-widgets-and-state](../02-widgets-and-state/)
