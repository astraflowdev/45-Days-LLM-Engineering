"""
Talking to a web API with requests -- GET, JSON, status codes, and POST.

Uses free public test APIs (no key needed). This is the exact shape of an LLM
call you'll make on Day 9.

Setup: pip install requests
Run:   python http_requests.py
"""

import requests

# ----- GET: ask a server for data -----
# api.github.com returns JSON describing the GitHub API itself.
response = requests.get("https://api.github.com")

# Always check the status before trusting the body.
response.raise_for_status()                  # raises on 4xx/5xx
print("Status code:", response.status_code)  # 200

data = response.json()                        # parse JSON -> dict
print("A field from the JSON:", data["current_user_url"])

print()

# ----- POST: send data to a server -----
# httpbin.org/post echoes back whatever we send -- handy for learning.
payload = {"prompt": "hello", "max_tokens": 50}   # like an LLM request body
headers = {"Authorization": "Bearer fake-key"}    # where an API key would go

post = requests.post(
    "https://httpbin.org/post",
    json=payload,        # json= serializes the dict AND sets Content-Type for us
    headers=headers,
    timeout=10,          # always set a timeout so a hang can't freeze your app
)
post.raise_for_status()

echoed = post.json()
print("Server echoed our body:", echoed["json"])
print("Server saw our header :", echoed["headers"]["Authorization"])
