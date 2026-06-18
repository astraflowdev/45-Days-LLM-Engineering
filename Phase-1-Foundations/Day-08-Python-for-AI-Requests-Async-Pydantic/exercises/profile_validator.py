"""
Exercise 1 -- Validate a user profile with Pydantic.

Setup: pip install pydantic
Run:   python profile_validator.py
"""

from pydantic import BaseModel, Field, ValidationError


# TODO 1: define a Profile model with:
#   - username: str
#   - age: int      (must be >= 13 -> use Field(ge=13))
#   - email: str
# class Profile(BaseModel):
#     ...

# TODO 2: create a VALID profile (age >= 13) and print it

# TODO 3: in a try/except ValidationError, create an INVALID profile (age=10)
#         and print the error message
