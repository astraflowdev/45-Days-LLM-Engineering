"""
Solution -- Exercise 1: PDF to clean text.

Run: python pdf_to_clean_solution.py path/to/file.pdf
"""

import re
import sys

import pdfplumber


def clean(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def pdf_to_text(path: str) -> str:
    parts = []
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            parts.append(page.extract_text() or "")
    return clean("\n".join(parts))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit("Usage: python pdf_to_clean_solution.py path/to/file.pdf")

    text = pdf_to_text(sys.argv[1])
    print("Total characters:", len(text))
    print("First 500 chars:")
    print(text[:500])
