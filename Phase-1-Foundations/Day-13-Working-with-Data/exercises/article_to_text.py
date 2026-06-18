"""
Exercise 2 -- web article to clean text.

Setup: pip install requests beautifulsoup4
Run:   python article_to_text.py https://example.com
"""

import re
import sys

import requests
from bs4 import BeautifulSoup

# TODO 1: write clean(text) -> collapse whitespace and strip
# TODO 2: fetch the URL (set a timeout + User-Agent header)
# TODO 3: parse with BeautifulSoup, get the title and all <p> text
# TODO 4: join + clean the paragraphs, print the title and first 500 chars
