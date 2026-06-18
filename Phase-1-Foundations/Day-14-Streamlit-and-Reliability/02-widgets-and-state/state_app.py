"""
Widgets + session state -- a counter that survives Streamlit's re-runs.

Setup: pip install streamlit
Run:   streamlit run state_app.py
"""

import streamlit as st

st.title("Widgets & Session State")

# Streamlit re-runs this script on every click, so plain variables would reset.
# session_state persists across re-runs. Initialise the key ONCE.
if "count" not in st.session_state:
    st.session_state.count = 0

# A selectbox and a button (each is a widget).
step = st.selectbox("Step size", [1, 5, 10])

if st.button(f"Add {step}"):
    st.session_state.count += step       # this change is remembered

if st.button("Reset"):
    st.session_state.count = 0

st.metric("Count", st.session_state.count)
st.caption("Without session_state, the count would reset to 0 on every click.")
