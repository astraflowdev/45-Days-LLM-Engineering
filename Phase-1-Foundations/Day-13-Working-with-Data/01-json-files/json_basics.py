"""
Reading and writing JSON (standard library -- runs anywhere).

Run:
    python json_basics.py
"""

import json

# ----- object -> JSON string -----
profile = {"name": "Aarav", "age": 21, "skills": ["python", "ai"]}
text = json.dumps(profile, indent=2)
print("As a JSON string:")
print(text)

# ----- JSON string -> object -----
back = json.loads(text)
print()
print("Parsed back to a dict:", back)
print("back['skills'] ->", back["skills"])

# ----- write to / read from a file -----
with open("profile.json", "w", encoding="utf-8") as f:
    json.dump(profile, f, indent=2)

with open("profile.json", encoding="utf-8") as f:
    from_file = json.load(f)

print()
print("Read back from profile.json:", from_file["name"])

# Clean up the file we just made.
import os
os.remove("profile.json")
