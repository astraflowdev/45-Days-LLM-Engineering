"""
Estimating LLM cost from token counts (standard library -- runs anywhere).

Prices below are ILLUSTRATIVE placeholders (per 1,000 tokens). Always check the
provider's current pricing page -- the point here is the formula.

Run:
    python cost_estimate.py
"""

# Illustrative prices per 1,000 tokens (NOT real -- check the provider).
INPUT_PRICE_PER_1K = 0.0001
OUTPUT_PRICE_PER_1K = 0.0003


def estimate_cost(in_tokens, out_tokens):
    return (in_tokens / 1000) * INPUT_PRICE_PER_1K + (out_tokens / 1000) * OUTPUT_PRICE_PER_1K


# Pretend a call used these tokens (you'd read them from response.usage_metadata).
calls = [
    ("short Q&A", 50, 80),
    ("summarize a page", 1200, 250),
    ("stuff a whole doc", 18000, 400),
]

print(f"{'call':22} {'in':>6} {'out':>6} {'est. cost':>12}")
print("-" * 50)
total = 0.0
for name, in_toks, out_toks in calls:
    cost = estimate_cost(in_toks, out_toks)
    total += cost
    print(f"{name:22} {in_toks:>6} {out_toks:>6} {cost:>12.6f}")

print("-" * 50)
print(f"{'TOTAL':22} {'':>6} {'':>6} {total:>12.6f}")
print()
print("Notice how 'stuff a whole doc' dominates -- that's why RAG retrieves only")
print("the relevant chunks instead of sending everything (Phase 2).")
