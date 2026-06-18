"""
Solution -- Exercise 2: Fetch and parse live data from a public API.

Run: python fetch_and_parse_solution.py
"""

import requests

URL = "https://api.github.com/users/octocat"

response = requests.get(URL, timeout=10)
response.raise_for_status()        # fail loudly on 4xx/5xx

data = response.json()             # dict of the user's public info

print("Name        :", data["name"])
print("Public repos:", data["public_repos"])
print("Followers   :", data["followers"])
