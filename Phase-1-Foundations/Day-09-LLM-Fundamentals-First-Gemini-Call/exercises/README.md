# Day 09 — Exercises

```bash
pip install google-generativeai python-dotenv   # + GEMINI_API_KEY in .env
```

Try each yourself, then check `*_solution.py`.

---

## Exercise 1 — Command-line chatbot 💬
Build a chatbot you can talk to in a loop, that **remembers the conversation**.

**Your task:** in `chatbot.py`, start a chat with `model.start_chat()`, then loop: read input with
`input()`, send it with `chat.send_message(...)`, print the reply. Quit when the user types `quit`.

*Hint:* `chat = model.start_chat()` keeps history for you across `send_message` calls.

➡ Solution: [`chatbot_solution.py`](chatbot_solution.py)

---

## Exercise 2 — Temperature explorer 🌡️
See how temperature changes answers for the **same** prompt.

**Your task:** in `temperature_explorer.py`, pick one prompt and call the model at temperatures
`0.0`, `0.7`, and `1.4`, printing each answer under its temperature. Notice how variety increases.

*Hint:* use `GenerationConfig(temperature=t)` in `generate_content(...)`.

➡ Solution: [`temperature_explorer_solution.py`](temperature_explorer_solution.py)
