"""
Context-window budgeting -- a standard-library estimate (no API key needed).

The context window holds prompt tokens + answer tokens together. This script
uses the rough rule "1 token ~= 4 characters" to show how to budget space and
leave room for the answer.

Run:
    python context_budget.py
"""

# A made-up small window so the numbers are easy to read.
# (Real Gemini models are far larger -- this is just to show the idea.)
CONTEXT_WINDOW = 1000          # total tokens allowed (prompt + answer)
ANSWER_BUDGET = 300            # tokens we want to reserve for the model's reply

paragraph = (
    "Retrieval-augmented generation lets a model answer questions using your own "
    "documents instead of only what it memorised during training. "
)


def estimate_tokens(text):
    # Rough heuristic: ~4 characters per token. Good enough for budgeting.
    return max(1, len(text) // 4)


per_paragraph = estimate_tokens(paragraph)
prompt_budget = CONTEXT_WINDOW - ANSWER_BUDGET
max_paragraphs = prompt_budget // per_paragraph

print("Context window      :", CONTEXT_WINDOW, "tokens (prompt + answer)")
print("Reserve for answer  :", ANSWER_BUDGET, "tokens")
print("Left for the prompt :", prompt_budget, "tokens")
print("Tokens per paragraph:", per_paragraph)
print()
print("So you can fit about", max_paragraphs, "paragraphs of context and still")
print("leave room for a", ANSWER_BUDGET, "-token answer.")
print()
print("When your document is bigger than this, you don't stuff it all in --")
print("you retrieve only the relevant chunks. That is RAG (Phase 2).")
