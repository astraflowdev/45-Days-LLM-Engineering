# 05 — Text Cleaning

Raw text from PDFs and web pages is messy: extra whitespace, blank lines, stray symbols, page numbers.
Feeding that to an LLM wastes tokens and confuses it. A quick **clean-up** pass pays off.

## The usual suspects
| Problem | Fix |
|---------|-----|
| Runs of spaces/newlines | collapse with `re.sub(r"\s+", " ", text)` |
| Leading/trailing space | `text.strip()` |
| Blank lines | drop empty lines |
| Weird unicode quotes/dashes | normalize or replace |
| Way too long | truncate to a token budget (Day 9) |

```python
import re

def clean(text: str) -> str:
    text = re.sub(r"\s+", " ", text)     # collapse all whitespace to single spaces
    return text.strip()
```

## Don't over-clean
Keep meaningful structure (paragraph breaks, lists) when it helps the model understand. Cleaning is
about removing **noise**, not flattening everything.

## Where it fits
`extract (PDF/web)` → **`clean`** → `chunk (Phase 2)` → `embed/retrieve` → `prompt the model`. The
cleaner the input, the better and cheaper the output.

```bash
python clean_text.py
```

➡ Next: practise in [../exercises/](../exercises/)
