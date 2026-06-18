# Day 11 — Exercises

```bash
pip install google-generativeai pydantic python-dotenv   # + GEMINI_API_KEY in .env
```

---

## Exercise 1 — Resume parser 📄
Extract a structured profile from a paragraph of resume text.

**Your task:** in `resume_parser.py`, define a Pydantic `Candidate` model (`name: str`,
`years_experience: int`, `skills: list[str]`), use JSON mode to extract it from the given resume
blurb, validate into the model, and print the object.

➡ Solution: [`resume_parser_solution.py`](resume_parser_solution.py)

---

## Exercise 2 — Extract with retry 🔁
Make extraction robust to a bad reply.

**Your task:** in `extract_with_retry.py`, define a Pydantic `Event` model (`title: str`,
`date: str`, `attendees: int` with `ge=0`), and write a loop that asks for JSON, validates, and
**retries up to 3 times** (feeding the validation error back) before giving up.

*Hint:* `Event.model_validate_json(resp.text)` parses + validates in one call.

➡ Solution: [`extract_with_retry_solution.py`](extract_with_retry_solution.py)
