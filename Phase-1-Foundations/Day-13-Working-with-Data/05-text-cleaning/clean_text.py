"""
Cleaning messy extracted text (standard library -- runs anywhere).

Run:
    python clean_text.py
"""

import re

# Pretend this came out of a PDF / web page: extra spaces, blank lines, newlines.
messy = """

   The   quick    brown fox

   jumped over the lazy dog.


   Page 1 of 3

"""


def clean(text: str) -> str:
    # 1. Collapse every run of whitespace (spaces, tabs, newlines) into one space.
    text = re.sub(r"\s+", " ", text)
    # 2. Trim the ends.
    return text.strip()


cleaned = clean(messy)

print("Before (repr):", repr(messy[:40]), "...")
print("After        :", cleaned)
print()
print(f"Shrank from {len(messy)} chars to {len(cleaned)} -- fewer tokens, clearer input.")
