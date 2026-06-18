# 05 — Streaming Responses

A long answer can take several seconds. If the UI just freezes, it feels broken. **Streaming** shows
the answer **token by token as it's generated** — like ChatGPT typing — so it feels instant.

## Streaming in Gemini
Pass `stream=True` and loop over the chunks:

```python
response = model.generate_content("Write a short poem about Python.", stream=True)
for chunk in response:
    print(chunk.text, end="", flush=True)     # print pieces as they arrive
```

## In Streamlit it's one line
Streamlit can consume a generator of text chunks directly:

```python
st.write_stream(chunk.text for chunk in response)
```

## Why it matters
| Without streaming | With streaming |
|-------------------|----------------|
| blank screen for 5s | text appears immediately |
| feels frozen | feels fast and alive |
| user may refresh/leave | user stays engaged |

It doesn't make the model faster — it makes the **wait visible**, which is most of the perceived speed.

## Gotcha
When streaming, you assemble the full text yourself (concatenate the chunks) if you need it
afterwards — and token usage is reported at the end.

```bash
python stream_console.py        # console streaming (needs GEMINI_API_KEY)
```

➡ Next: practise in [../exercises/](../exercises/)
