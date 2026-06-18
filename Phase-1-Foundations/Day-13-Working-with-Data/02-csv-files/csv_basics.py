"""
Reading and writing CSV with named columns (standard library).

Run:
    python csv_basics.py
"""

import csv
import os

rows = [
    {"name": "Aarav", "marks": 82},
    {"name": "Priya", "marks": 91},
    {"name": "Rohan", "marks": 74},
]

# ----- Write a CSV with a header row -----
with open("students.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "marks"])
    writer.writeheader()
    writer.writerows(rows)

# ----- Read it back by column name and compute an average -----
total = 0
count = 0
with open("students.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        marks = int(row["marks"])           # CSV values are strings -> convert
        print(f"  {row['name']}: {marks}")
        total += marks
        count += 1

print()
print("Average marks:", round(total / count, 1))

os.remove("students.csv")
