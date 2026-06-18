"""
Exercise 2 -- Fetch and parse live data from a public API.

Setup: pip install requests
Run:   python fetch_and_parse.py
"""

import requests

URL = "https://api.github.com/users/octocat"

# TODO 1: GET the URL
# TODO 2: call raise_for_status() to fail loudly on a bad response
# TODO 3: parse the JSON body with .json()
# TODO 4: print the user's "name", "public_repos", and "followers"
