# Day 13 — Working with Data

LLMs are only as useful as the **data you feed them**. Real inputs come as JSON, CSV, PDFs, and web
pages. Today you learn to **read, extract, and clean** all four — the raw material for tomorrow's
summarizer and for all of Phase 2's RAG.

## Learning objectives
By the end of today you can:
- Read and write **JSON** and **CSV** (standard library)
- Extract text from **PDFs**
- Pull text from a **web page** with BeautifulSoup
- **Clean** messy text so a model gets a tidy input

## Modules (work through them in order)

| # | Module | What it covers |
|--:|--------|----------------|
| 01 | [json-files](01-json-files/) | `json`: load/dump, dicts ↔ files |
| 02 | [csv-files](02-csv-files/) | `csv.DictReader`/`DictWriter` |
| 03 | [pdf-extraction](03-pdf-extraction/) | Pull text from PDFs with `pdfplumber` |
| 04 | [web-scraping](04-web-scraping/) | `requests` + BeautifulSoup |
| 05 | [text-cleaning](05-text-cleaning/) | Whitespace, noise, length — prep for the model |

Then practise in **[exercises/](exercises/)**.

## Setup
```bash
pip install -r requirements.txt        # pdfplumber, beautifulsoup4, requests (json/csv are built in)
```

## How to run
```bash
python 01-json-files/json_basics.py     # standard library, runs anywhere
```

## Today's exercise
Extract text from a **PDF** and turn a **web article** into clean text ready to summarize. See
[`exercises/`](exercises/).

➡ Next (Day 14): Streamlit crash course + reliability (retries, rate limits, cost).
