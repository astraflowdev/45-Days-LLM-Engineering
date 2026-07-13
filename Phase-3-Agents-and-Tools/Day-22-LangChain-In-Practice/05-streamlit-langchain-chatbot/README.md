# 05 · Streamlit × LangChain Chatbot

Same brain as module 04 — `prompt + MessagesPlaceholder + model` — now **live in a browser**. This is
where Day 19 (Streamlit) and Day 21 (LangChain) finally meet.

```bash
streamlit run app.py          # NOT `python app.py`
```

## Three things the web version adds

| Concern | How |
|---------|-----|
| **Chat UI** | `st.chat_input(...)` for the box, `st.chat_message(role)` for bubbles |
| **Memory** | history in `st.session_state` (survives Streamlit's reruns) |
| **Live typing** | `st.write_stream(chain.stream(...))` streams the reply token by token |

## The rerun trap (why `session_state`)

Remember from Day 19: **every** chat message reruns the whole script top to bottom. A plain
`history = []` would reset on every message. So the conversation must live in `st.session_state`, the
one place that persists across reruns:

```python
if "messages" not in st.session_state:
    st.session_state.messages = []       # created once, kept across reruns
```

Each rerun we **redraw the whole conversation** from `session_state`, then handle the new message. That
"replay history, then append" loop is the standard Streamlit chat pattern.

## Streaming for free

Because the chain is a Runnable, it already has `.stream()` — no extra code. `st.write_stream` consumes
the generator, renders each piece live, **and** returns the finished string to store:

```python
with st.chat_message("assistant"):
    reply = st.write_stream(chain.stream({"history": history, "input": user_text}))
st.session_state.messages.append({"role": "assistant", "content": reply})
```

## Cache the chain, not the answer

```python
@st.cache_resource          # build the model/chain ONCE, reused across reruns
def get_chain():
    ...
```

`cache_resource` is for heavy objects you build once (models, clients, chains) — Day 19, module 06.
Without it you'd reconstruct the Groq client on every keystroke's rerun.

## Bridging session_state ↔ LangChain messages

`session_state` stores plain `{"role", "content"}` dicts (easy to redraw). The chain's placeholder wants
`HumanMessage`/`AIMessage` objects — so just before invoking, we convert:

```python
history = [ (HumanMessage if m["role"] == "user" else AIMessage)(content=m["content"])
            for m in st.session_state.messages[:-1] ]     # all but the new message
```

## Run it

```bash
streamlit run app.py
```
Without a `GROQ_API_KEY` the app shows a friendly notice and `st.stop()`s (no crash). With a key, chat
away — it remembers the conversation and streams replies. Use the sidebar **Clear conversation** button
to reset.

➡ Next: [06 · Streamlit RAG App](../06-streamlit-rag-app/README.md) — add document upload + retrieval for "chat with your docs".
