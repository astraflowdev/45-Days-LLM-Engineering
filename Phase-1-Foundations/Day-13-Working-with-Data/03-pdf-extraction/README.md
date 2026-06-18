# 03 — PDF Extraction

A huge amount of real-world knowledge lives in **PDFs** — notes, textbooks, reports, resumes. To feed
one to an LLM you first **extract its text**. We use **`pdfplumber`** (reliable, good with layout).

```python
import pdfplumber

with pdfplumber.open("notes.pdf") as pdf:
    text = ""
    for page in pdf.pages:
        text += page.extract_text() or ""    # extract_text() can return None on image pages
print(text[:500])
```

## The flow
1. Open the PDF.
2. Loop pages, call `page.extract_text()`.
3. Join into one string (or keep per-page for citations later).

| Library | Notes |
|---------|-------|
| `pdfplumber` | great text + table extraction (our default) |
| `PyPDF2` / `pypdf` | lightweight, simple text |

## Gotchas
- **Scanned PDFs are images** — `extract_text()` returns nothing. Those need OCR (e.g. `pytesseract`),
  which is out of scope today.
- Always guard `extract_text() or ""` — a page can return `None`.
- Big PDFs blow past the context window → you'll **chunk** them in Phase 2.

```bash
python pdf_extract.py path/to/file.pdf
```

> No PDF handy? Export any doc to PDF, or grab a small public one. The script takes the path as an
> argument.

➡ Next: [04-web-scraping](../04-web-scraping/)
