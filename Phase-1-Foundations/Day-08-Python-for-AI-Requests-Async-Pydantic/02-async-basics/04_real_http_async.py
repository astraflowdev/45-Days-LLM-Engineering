"""
REAL async over the network -- httpx.AsyncClient.

So far we faked slow calls with asyncio.sleep. Now we hit a REAL public API
several times and watch the same overlap happen for real HTTP.

`requests` (module 01) is synchronous -- it blocks. The async twin is
`httpx.AsyncClient`, whose `await client.get(url)` is a pause point, so many
requests can be in flight at once. This is exactly how you'll call several LLMs
(or one LLM many times) concurrently later in the course.

We use httpbin.org/delay/N, a free endpoint that waits N seconds then replies.

Setup: pip install httpx
Run:   python 04_real_http_async.py     (needs internet)
"""

import asyncio
import time

import httpx

# Each URL tells the server to wait 1 second before replying.
URLS = [
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1",
]


async def fetch(client, url):
    """One real request. `await` pauses HERE while the network is busy."""
    print(f"  start  {url}")
    response = await client.get(url)      # non-blocking network wait
    response.raise_for_status()
    print(f"  done   {url}  ({response.status_code})")
    return response.status_code


async def fetch_sequentially(client):
    """await each request, then the next -> waits add up (~3s)."""
    print("Sequential (await one at a time):")
    start = time.perf_counter()
    for url in URLS:
        await fetch(client, url)
    print(f"  -> took {time.perf_counter() - start:.2f}s\n")


async def fetch_concurrently(client):
    """gather starts all requests, then waits once -> ~1s (the slowest one)."""
    print("Concurrent (asyncio.gather):")
    start = time.perf_counter()
    await asyncio.gather(*(fetch(client, url) for url in URLS))   # * unpacks the list
    print(f"  -> took {time.perf_counter() - start:.2f}s\n")


async def main():
    # One client, reused for every request (opens/reuses connections efficiently).
    async with httpx.AsyncClient(timeout=20) as client:
        await fetch_sequentially(client)
        await fetch_concurrently(client)
    print("Real network calls -- same overlap trick as the fake ones.")


asyncio.run(main())
