"""
Solution -- Exercise 2: web article to clean text.

Run: python article_to_text_solution.py https://example.com
"""

import re
import sys

import requests
from bs4 import BeautifulSoup


def clean(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def article_to_text(url: str) -> tuple[str, str]:
    html = requests.get(url, timeout=10, headers={"User-Agent": "Mozilla/5.0"}).text
    soup = BeautifulSoup(html, "html.parser")
    title = soup.title.string.strip() if soup.title else "(no title)"
    body = clean(" ".join(p.get_text(" ", strip=True) for p in soup.find_all("p")))
    return title, body


if __name__ == "__main__":
    url = sys.argv[1] if len(sys.argv) > 1 else "https://example.com"
    title, body = article_to_text(url)
    print("Title:", title)
    print("Length:", len(body), "chars")
    print("First 500 chars:")
    print(body[:500] or "(no paragraph text found)")
