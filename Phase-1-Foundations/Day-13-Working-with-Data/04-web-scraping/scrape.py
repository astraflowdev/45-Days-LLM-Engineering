"""
Fetch a web page and extract its text with BeautifulSoup.

Setup: pip install requests beautifulsoup4
Run:   python scrape.py https://example.com
"""

import sys

import requests
from bs4 import BeautifulSoup


def fetch_text(url: str) -> tuple[str, str]:
    """Return (page title, all paragraph text) for a URL."""
    html = requests.get(url, timeout=10, headers={"User-Agent": "Mozilla/5.0"}).text
    soup = BeautifulSoup(html, "html.parser")

    title = soup.title.string.strip() if soup.title else "(no title)"
    paragraphs = [p.get_text(strip=True) for p in soup.find_all("p")]
    body = "\n".join(p for p in paragraphs if p)
    return title, body


if __name__ == "__main__":
    url = sys.argv[1] if len(sys.argv) > 1 else "https://example.com"
    title, body = fetch_text(url)

    print("Title:", title)
    print("Paragraph text (first 300 chars):")
    print(body[:300] or "(no <p> text found)")
