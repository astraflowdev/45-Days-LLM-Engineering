"""
app.py -- the Streamlit UI for the AI Content Summarizer.

Collects input (PDF / URL / text), calls summarize(), and renders the result.
The UI knows NOTHING about Gemini -- it just calls summarize(text).

Setup: pip install -r requirements.txt   (+ GEMINI_API_KEY in .env)
Run:   streamlit run app.py
"""

import streamlit as st

import loaders
from summarizer import summarize

st.set_page_config(page_title="AI Content Summarizer", page_icon="📝")
st.title("📝 AI Content Summarizer")
st.caption("PDF, article URL, or pasted text -> TL;DR, key points, action items.")

# Pick the input type.
source = st.radio("Input type", ["Paste text", "Article URL", "PDF upload"], horizontal=True)

text = ""
if source == "Paste text":
    text = st.text_area("Paste your content", height=200)
elif source == "Article URL":
    url = st.text_input("Article URL")
    if url:
        with st.spinner("Fetching the page..."):
            text = loaders.load_url(url)
elif source == "PDF upload":
    pdf = st.file_uploader("Upload a PDF", type="pdf")
    if pdf:
        with st.spinner("Reading the PDF..."):
            text = loaders.load_pdf(pdf)

if st.button("Summarize", type="primary"):
    if not text.strip():
        st.warning("Give me some content first.")
    else:
        with st.spinner("Summarizing..."):
            summary = summarize(loaders.clean(text))

        st.subheader("TL;DR")
        st.write(summary.tldr)

        st.subheader("Key points")
        for point in summary.key_points:
            st.markdown(f"- {point}")

        if summary.action_items:
            st.subheader("Action items")
            for item in summary.action_items:
                st.markdown(f"- [ ] {item}")
