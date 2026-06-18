"""
Your first Streamlit app.

Setup: pip install streamlit
Run:   streamlit run hello_app.py     (NOT `python hello_app.py`)
"""

import streamlit as st

# Streamlit runs this whole script top-to-bottom on every interaction.
st.title("My First AI App")
st.write("Hello! This is a web app written in pure Python.")

# A text input -- whatever the user types comes back as a string.
name = st.text_input("What's your name?")

if name:
    st.success(f"Welcome, {name}! You just built a web app with zero HTML.")
else:
    st.info("Type your name above to see this update.")
