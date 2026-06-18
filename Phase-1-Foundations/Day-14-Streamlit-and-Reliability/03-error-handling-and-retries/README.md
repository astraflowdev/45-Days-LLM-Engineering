# 03 — Error Handling & Retries

API calls fail sometimes — a network blip, a `429` rate limit, a momentary server error. A real app
**retries** instead of crashing. The standard technique is **exponential backoff**: wait a little,
then a bit more, then more.

```text
try 1 -> fail -> wait 1s
try 2 -> fail -> wait 2s
try 3 -> fail -> wait 4s
try 4 -> success ✅   (or give up after N)
```

```python
import time

def with_retry(call, max_tries=4):
    for attempt in range(max_tries):
        try:
            return call()
        except Exception as err:
            if attempt == max_tries - 1:
                raise                      # out of retries -> let it fail
            wait = 2 ** attempt            # 1, 2, 4, 8 seconds
            print(f"  attempt {attempt+1} failed ({err}); retrying in {wait}s")
            time.sleep(wait)
```

## Do / don't
| Do | Don't |
|----|-------|
| retry **transient** errors (429, 5xx, timeouts) | retry a `401` bad key (it'll never succeed) |
| back off (grow the wait) | hammer instantly in a tight loop |
| cap the attempts | retry forever |

> Retry the failures that **might** succeed next time; fail fast on the ones that won't.

The script (standard library) shows backoff against a flaky fake function.

```bash
python retry_backoff.py
```

➡ Next: [04-rate-limits-and-cost](../04-rate-limits-and-cost/)
