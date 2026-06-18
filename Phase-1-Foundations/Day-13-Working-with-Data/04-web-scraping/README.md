# 04 — Web Scraping (Lightly)

Sometimes the data you want is on a **web page**. **`requests`** fetches the HTML; **BeautifulSoup**
parses it so you can pull out the text you care about.

```python
import requests
from bs4 import BeautifulSoup

html = requests.get("https://example.com", timeout=10).text
soup = BeautifulSoup(html, "html.parser")

print(soup.title.string)                 # the page title
for p in soup.find_all("p"):             # every paragraph
    print(p.get_text(strip=True))
```

## The toolkit
| Call | Gives you |
|------|-----------|
| `soup.title` | the `<title>` element |
| `soup.find("h1")` | first matching tag |
| `soup.find_all("p")` | all matching tags |
| `element.get_text(strip=True)` | clean text inside a tag |

## Scrape responsibly
- Check the site's **terms** and `robots.txt`; don't hammer servers (add small delays).
- Set a **timeout** and a normal `User-Agent` header.
- Pages change — scrapers are brittle. Prefer an official **API** when one exists.

## Why it's here
Scraped article text → cleaned → summarized by your LLM. That's literally Day 15's mini-project input.

```bash
python scrape.py https://example.com
```

➡ Next: [05-text-cleaning](../05-text-cleaning/)
