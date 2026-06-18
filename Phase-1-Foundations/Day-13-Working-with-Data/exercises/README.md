# Day 13 — Exercises

```bash
pip install pdfplumber beautifulsoup4 requests
```

---

## Exercise 1 — PDF → clean text 📄
Turn a PDF into one clean string ready for an LLM.

**Your task:** in `pdf_to_clean.py`, take a PDF path from the command line, extract all its text with
`pdfplumber`, run it through a `clean()` function (collapse whitespace, strip), and print the first
500 characters plus the total length.

➡ Solution: [`pdf_to_clean_solution.py`](pdf_to_clean_solution.py)

---

## Exercise 2 — Article → clean text 🌐
Get a web article into clean, summarize-ready text.

**Your task:** in `article_to_text.py`, fetch a URL, extract the `<p>` paragraphs with BeautifulSoup,
join + clean them, and print the title and the first 500 characters. This is exactly the input your
Day 15 summarizer will take.

➡ Solution: [`article_to_text_solution.py`](article_to_text_solution.py)
