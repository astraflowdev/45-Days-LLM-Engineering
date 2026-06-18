"""
Exercise 1 -- PDF to clean text.

Setup: pip install pdfplumber
Run:   python pdf_to_clean.py path/to/file.pdf
"""

import re
import sys

import pdfplumber

# TODO 1: write clean(text) -> collapse whitespace with re.sub(r"\s+", " ", text) and strip
# TODO 2: read the PDF path from sys.argv
# TODO 3: extract all page text with pdfplumber (guard page.extract_text() or "")
# TODO 4: clean it, then print the first 500 chars and the total length
