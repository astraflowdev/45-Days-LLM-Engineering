"""
Type hints -- annotating variables and functions.

Hints don't change how code runs (Python ignores them at runtime); they make
code readable, help your editor, and power Pydantic (next module).

Run:
    python type_hints.py
"""

from typing import Optional

# ----- Variable annotations -----
name: str = "Aarav"
age: int = 21
price: float = 49.99
is_member: bool = True
tags: list[str] = ["ai", "python"]
scores: dict[str, int] = {"math": 90, "science": 85}
nickname: Optional[str] = None        # a str OR None


# ----- Function annotations: parameter types and the return type -----
def total_price(price: float, quantity: int) -> float:
    """Return price * quantity. Hints say: two numbers in, a float out."""
    return price * quantity


def greet(person: str, times: int = 1) -> str:
    return f"Hi {person}! " * times


print("name:", name, "| age:", age, "| tags:", tags)
print("total_price(49.99, 3) ->", total_price(49.99, 3))
print("greet('Priya', 2)     ->", greet("Priya", 2))

# Hints are NOT enforced at runtime -- this still runs even though "five" is not int:
sneaky: int = "five"   # type checkers flag it; Python itself does not
print("sneaky (un-enforced hint):", sneaky)
print("That's why Pydantic exists -- it actually CHECKS the types. See module 05.")
