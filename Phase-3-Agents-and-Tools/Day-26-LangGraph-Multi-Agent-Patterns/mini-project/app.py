"""
SoftDesk Content Crew -- Streamlit UI (thin wrapper over step6_content_crew.run)

The whole crew lives in step6_content_crew.py. This file is ONLY the web layer:
take a topic, call run(), show the blurb + the review notes + a "How the crew built
this" trail. Each browser session gets its own thread_id, so the crew's memory of
"blurbs produced this session" stays per-user.

Run it (needs GROQ_API_KEY in a .env file in this folder):
    streamlit run app.py
"""

import os
import uuid

import streamlit as st
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="SoftDesk Content Crew", page_icon="*")
st.title("SoftDesk Content Crew")
st.caption("A LangGraph team: researcher -> writer -> parallel review -> editor")

# Direct-LLM policy: a key is required. Guard before importing the crew (importing
# it constructs a ChatGroq client).
if not os.getenv("GROQ_API_KEY"):
    st.warning("Set GROQ_API_KEY in a .env file next to this app to run the crew.")
    st.stop()

from step6_content_crew import run  # noqa: E402  (import after the key guard)

# One thread_id per browser session -> the crew remembers this session's blurbs.
if "thread_id" not in st.session_state:
    st.session_state.thread_id = f"session-{uuid.uuid4().hex[:8]}"

topic = st.text_input("What should the crew write a blurb about?",
                      placeholder="e.g. a free 45-day AI engineering bootcamp")

if st.button("Run the crew", type="primary") and topic.strip():
    with st.spinner("The crew is working (research -> write -> review -> edit)..."):
        result = run(topic.strip(), thread_id=st.session_state.thread_id)

    st.subheader("Final blurb")
    st.success(result["blurb"])

    with st.expander("How the crew built this"):
        st.write(" -> ".join(result["trail"]))
        st.markdown("**Review panel notes:**")
        for note in result["reviews"]:
            st.markdown(f"- {note}")

    st.caption(f"Blurbs produced this session: {result['produced_so_far']}")
