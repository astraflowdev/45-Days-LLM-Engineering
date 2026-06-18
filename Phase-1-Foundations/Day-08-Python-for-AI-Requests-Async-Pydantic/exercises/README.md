# Day 08 — Exercises

Practise the engineering habits from today. Try each yourself, then check `*_solution.py`.

```bash
pip install requests pydantic
```

---

## Exercise 1 — Validate a user profile 🧾
Build a Pydantic model for a signup form and use it to accept good data and reject bad data.

**Your task:** in `profile_validator.py`, define a `Profile` model with `username: str`,
`age: int` (must be ≥ 13), and `email: str`. Create one **valid** profile and print it, then try
an **invalid** one (age `10`) inside a `try/except ValidationError` and print the error message.

*Hint:* use `Field(ge=13)` for the age rule.

➡ Solution: [`profile_validator_solution.py`](profile_validator_solution.py)

---

## Exercise 2 — Fetch and parse live data 🌐
Call a free public API and pull out just the fields you want — the same move you'll make on real
LLM responses.

**Your task:** in `fetch_and_parse.py`, `GET` `https://api.github.com/users/octocat`, call
`raise_for_status()`, then `.json()`, and print the user's `name`, `public_repos`, and `followers`.

*Hint:* the response is a dict — index it with `data["public_repos"]`.

➡ Solution: [`fetch_and_parse_solution.py`](fetch_and_parse_solution.py)
