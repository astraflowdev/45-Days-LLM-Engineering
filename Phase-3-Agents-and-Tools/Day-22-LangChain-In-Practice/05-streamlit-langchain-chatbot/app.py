"""
05 - Streamlit x LangChain chatbot: the module-04 chain, live in a browser.

Same brain as module 04 (prompt + MessagesPlaceholder + model), now with:
    - Streamlit chat widgets (st.chat_input, st.chat_message)
    - conversation memory in st.session_state (survives Streamlit's reruns)
    - streaming replies via st.write_stream(chain.stream(...))

Day 19 taught the Streamlit rerun model and session_state; Day 21 taught the
chain. This module is where they meet.

Setup:
    pip install streamlit langchain langchain-groq python-dotenv
    echo GROQ_API_KEY=your_key > .env
Run  (note: streamlit run, NOT python):
    streamlit run app.py
"""

import os
from dotenv import load_dotenv
import streamlit as st

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage

load_dotenv()
MODEL = "llama-3.1-8b-instant"

st.set_page_config(page_title="LangChain Chatbot", page_icon="💬")
st.title("💬 LangChain + Groq Chatbot")

# --- 1. Need a key to talk to the model -----------------------------------
if not os.getenv("GROQ_API_KEY"):
    st.info("Add GROQ_API_KEY to a .env file to chat. Get a free key at console.groq.com/keys.")
    st.stop()      # halt the script cleanly -- nothing below runs without a key

# --- 2. Build the chain ONCE and cache it ---------------------------------
# cache_resource: build the model/chain a single time, not on every rerun.
# (A chat message triggers a full script rerun -- Day 19 -- so caching matters.)
@st.cache_resource
def get_chain():
    from langchain_groq import ChatGroq
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant for an Indian e-commerce store. Keep replies concise."),
        MessagesPlaceholder("history"),
        ("human", "{input}"),
    ])
    model = ChatGroq(model=MODEL, temperature=0.3)
    return prompt | model | StrOutputParser()

chain = get_chain()

# --- 3. Conversation memory lives in session_state ------------------------
# session_state persists across reruns; a plain variable would reset every time.
if "messages" not in st.session_state:
    st.session_state.messages = []          # list of {"role", "content"}

# --- 4. Redraw the whole conversation on every rerun ----------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# --- 5. Handle a new message ----------------------------------------------
if user_text := st.chat_input("Ask me anything..."):
    # Show + store the user's message.
    st.session_state.messages.append({"role": "user", "content": user_text})
    with st.chat_message("user"):
        st.markdown(user_text)

    # Rebuild LangChain history from session_state for the placeholder.
    history = []
    for m in st.session_state.messages[:-1]:      # everything except the new msg
        cls = HumanMessage if m["role"] == "user" else AIMessage
        history.append(cls(content=m["content"]))

    # Stream the reply. chain.stream(...) yields text pieces; st.write_stream
    # renders them live AND returns the full string when done.
    with st.chat_message("assistant"):
        reply = st.write_stream(chain.stream({"history": history, "input": user_text}))

    # Store the assistant reply so it's there on the next rerun.
    st.session_state.messages.append({"role": "assistant", "content": reply})

# --- Sidebar: a reset button ----------------------------------------------
with st.sidebar:
    st.header("Chat")
    st.caption(f"{len(st.session_state.messages)} messages so far.")
    if st.button("Clear conversation"):
        st.session_state.messages = []
        st.rerun()
