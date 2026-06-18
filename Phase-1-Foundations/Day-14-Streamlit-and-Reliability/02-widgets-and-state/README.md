# 02 — Widgets & Session State

Widgets collect input; **session state** remembers things across the re-runs Streamlit does on every
click.

## Common widgets
| Widget | Returns |
|--------|---------|
| `st.text_input(...)` | a string |
| `st.text_area(...)` | a longer string |
| `st.button(...)` | `True` on the run where it was clicked |
| `st.selectbox(..., options)` | the chosen option |
| `st.slider(...)` | a number |
| `st.file_uploader(...)` | an uploaded file object |

## Why session state is needed
Because the script re-runs every interaction, plain variables reset each time. `st.session_state` is
a dict that **persists** across re-runs:

```python
if "count" not in st.session_state:
    st.session_state.count = 0          # initialise once

if st.button("Add one"):
    st.session_state.count += 1         # survives the re-run

st.write("Count:", st.session_state.count)
```

This is exactly how you keep **chat history**, a loaded document, or a running total alive.

## Pattern to remember
> Initialise a key **if it's not already in** `st.session_state`, then read/update it. Without this,
> your counter (or chat) resets to zero on every click.

## Run it
```bash
streamlit run state_app.py
```

➡ Next: [03-error-handling-and-retries](../03-error-handling-and-retries/)
