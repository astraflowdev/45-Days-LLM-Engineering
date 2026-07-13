# 04 · A Conversational Chain with Memory

A RAG chain answers **one** question. A **chatbot** has to remember the conversation, so *"what did I
just ask?"* works. We build that memory with the exact Day-21 pieces — this is the **brain** we'll put
behind a Streamlit UI in the next module.

## The memory slot: `MessagesPlaceholder`

```python
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a friendly store assistant. Keep replies short."),
    MessagesPlaceholder("history"),      # ← all past turns get injected here
    ("human", "{input}"),                # ← this turn's new message
])
```

`MessagesPlaceholder("history")` is an **empty slot**. At invoke time you fill it with the list of
past messages, so the model always sees the whole conversation before answering the new line.

## The recipe (three steps, every turn)

```python
chain = prompt | model | StrOutputParser()
history = []                                    # this list IS the memory

def chat(user_text):
    reply = chain.invoke({"history": history, "input": user_text})
    history.append(HumanMessage(content=user_text))   # remember both sides
    history.append(AIMessage(content=reply))
    return reply
```

1. Keep a `history` list of past messages.
2. Each turn, invoke with `{"history": history, "input": user_text}`.
3. Append **both** the user message **and** the reply to `history`.

The placeholder re-injects all of `history` on the next call — that's the entire trick behind
conversation memory.

## Why append both sides?

If you only stored the user's messages, the bot would see your questions but not its own past
answers — and lose the thread. Storing `HumanMessage` **and** `AIMessage` gives it the full dialogue,
which is how it can resolve *"what order number did I give?"* three turns later.

## This vs. Day 16

Day 16 did the same "append every turn" idea with raw dicts and the Groq SDK. Here it's the same idea
expressed in LangChain: a **prompt slot** (`MessagesPlaceholder`) instead of manual list-stuffing, and
a reusable **chain** instead of a bare API call. Same concept, cleaner seams.

## A note on `RunnableWithMessageHistory`

LangChain *has* a wrapper (`RunnableWithMessageHistory`) that automates the append-both-sides step —
but it's being phased out, and the manual `history` list above is the clear, supported path for a
simple chat. Heavier, persistent memory (across sessions, keyed by user) is a **LangGraph checkpointer**
job — that's Day 23.

## Run it

```bash
python chatbot.py
```
It runs a scripted 3-turn conversation. **With** a key the bot really recalls your name and order
number; **without** one, an offline stand-in reports how many past messages it can see — proof the
history is growing and being re-injected. The **interactive** version is the next module.

➡ Next: [05 · Streamlit × LangChain Chatbot](../05-streamlit-langchain-chatbot/README.md) — this chain, live in a browser.
