"""
Extract text from a PDF with pdfplumber.

Setup: pip install pdfplumber
Run:   python pdf_extract.py path/to/file.pdf
"""

import sys

import pdfplumber


def extract_pdf_text(path: str) -> str:
    """Return all text from a PDF, page by page."""
    chunks = []
    with pdfplumber.open(path) as pdf:
        for i, page in enumerate(pdf.pages, start=1):
            text = page.extract_text() or ""    # None on image-only pages
            chunks.append(text)
            print(f"  page {i}: {len(text)} chars")
    return "\n".join(chunks)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit("Usage: python pdf_extract.py path/to/file.pdf")

    full_text = extract_pdf_text(sys.argv[1])
    print()
    print("Total characters:", len(full_text))
    print("First 300 chars:")
    print(full_text[:300])
