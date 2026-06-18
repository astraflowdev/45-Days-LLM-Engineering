"""
loaders.py -- turn any input (PDF, URL, raw text) into clean text.

Reuses the Day 13 patterns. Each loader returns a clean string ready for the
summarizer.

Setup: pip install pdfplumber requests beautifulsoup4
"""

import re

import pdfplumber
import requests
from bs4 import BeautifulSoup


def clean(text: str) -> str:
    """Collapse whitespace and trim -- fewer tokens, clearer input."""
    return re.sub(r"\s+", " ", text).strip()


def load_pdf(file_or_path) -> str:
    """Extract clean text from a PDF (a path or a file-like object)."""
    parts = []
    with pdfplumber.open(file_or_path) as pdf:
        for page in pdf.pages:
            parts.append(page.extract_text() or "")
    return clean("\n".join(parts))


def load_url(url: str) -> str:
    """Fetch a web page and return clean paragraph text."""
    html = requests.get(url, timeout=15, headers={"User-Agent": "Mozilla/5.0"}).text
    soup = BeautifulSoup(html, "html.parser")
    return clean(" ".join(p.get_text(" ", strip=True) for p in soup.find_all("p")))


def load_text(text: str) -> str:
    """Clean pasted text."""
    return clean(text)
