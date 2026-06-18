# 02 — CSV Files

CSV (comma-separated values) is how spreadsheets and exports travel. Python's built-in **`csv`**
module reads and writes it — and `DictReader`/`DictWriter` let you work with **named columns** instead
of counting positions.

```python
import csv

with open("students.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        print(row["name"], row["marks"])     # access by column name
```

## Reading vs writing
| Class | Use |
|-------|-----|
| `csv.DictReader(f)` | iterate rows as dicts keyed by header |
| `csv.DictWriter(f, fieldnames=[...])` | write dicts as rows (call `writeheader()` first) |

## Gotchas
- Open files with **`newline=""`** — it prevents blank lines on Windows.
- Every value read from CSV is a **string** — convert with `int(...)`/`float(...)` when you need numbers.
- Watch for commas **inside** a field; the `csv` module handles quoting for you (don't split by hand).

The script writes a small CSV, reads it back, and computes an average — all standard library.

```bash
python csv_basics.py
```

➡ Next: [03-pdf-extraction](../03-pdf-extraction/)
