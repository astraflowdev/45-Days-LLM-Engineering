"""
Exercise 1 -- an ask-anything Streamlit app with retries.

Setup: pip install streamlit google-generativeai python-dotenv  (+ GEMINI_API_KEY in .env)
Run:   streamlit run ask_app.py
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

# TODO 1: add a st.text_area for the user's question
# TODO 2: add a st.button("Ask"); when clicked and the question is non-empty:
#           - with st.spinner("Thinking..."): call the model THROUGH with_retry(...)
#           - show the answer with st.write
# TODO 3 (Exercise 2): also show response.usage_metadata token counts with st.caption/st.metric
