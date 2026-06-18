"""
Solution -- Exercises 1 & 2: ask-anything Streamlit app with retries + token readout.

Setup: pip install streamlit google-generativeai python-dotenv  (+ GEMINI_API_KEY in .env)
Run:   streamlit run ask_app_solution.py
"""

import os
import time

from dotenv import load_dotenv
import google.generativeai as genai
import streamlit as st

load_dotenv()
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-2.0-flash")


def with_retry(call, max_tries=3):
    for attempt in range(max_tries):
        try:
            return call()
        except Exception:
            if attempt == max_tries - 1:
                raise
            time.sleep(2 ** attempt)


st.title("Ask Anything")
st.caption("Powered by Gemini, with a retry wrapper so a blip won't crash it.")

question = st.text_area("Your question")

if st.button("Ask") and question.strip():
    with st.spinner("Thinking..."):
        response = with_retry(lambda: model.generate_content(question))

    st.write(response.text)

    # Exercise 2: transparency -- show token usage.
    usage = response.usage_metadata
    col1, col2, col3 = st.columns(3)
    col1.metric("Prompt tokens", usage.prompt_token_count)
    col2.metric("Output tokens", usage.candidates_token_count)
    col3.metric("Total tokens", usage.total_token_count)
