# 02 — A Gemini Provider Function

Step one of "one interface": wrap Gemini in a small, boring function with a **uniform signature** —
prompt in, string out.

```python
def ask_gemini(prompt: str) -> str:
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])
    model = genai.GenerativeModel("gemini-2.0-flash")
    return model.generate_content(prompt).text
```

That's the whole idea: the **outside** sees `ask_gemini(prompt) -> str`. The messy details
(configure, model name, response parsing) stay **inside**.

## Keep the signature identical across providers
Every provider function you write today will look like:

```python
def ask_<provider>(prompt: str) -> str: ...
```

Same input, same output. That sameness is what lets module 05 treat them interchangeably.

| Inside (varies per provider) | Outside (always the same) |
|------------------------------|---------------------------|
| SDK, model name, config | `ask_x(prompt: str) -> str` |

```bash
python gemini_provider.py
```

➡ Next: [03-groq-provider](../03-groq-provider/)
