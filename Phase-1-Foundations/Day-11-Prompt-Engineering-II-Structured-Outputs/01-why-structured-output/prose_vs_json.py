"""
Why structured output -- prose vs JSON (no API key needed).

Shows why a sentence is useless to code while JSON is directly usable.

Run:
    python prose_vs_json.py
"""

import json

# What an unstructured model reply might look like (a string).
prose_reply = "Sure! The person's name is Aarav and they are 21 years old."

# What we actually want back (a JSON string -> parseable into a dict).
json_reply = '{"name": "Aarav", "age": 21}'

print("Prose reply (hard to use):")
print(" ", prose_reply)
print("  -> to get the age you'd have to parse English. Fragile and error-prone.")
print()

print("JSON reply (easy to use):")
data = json.loads(json_reply)        # str -> dict
print(" ", data)
print("  -> data['name'] =", data["name"], "| data['age'] =", data["age"], f"({type(data['age']).__name__})")
print()
print("Code wants structured data. Next: make the model ALWAYS return JSON.")
