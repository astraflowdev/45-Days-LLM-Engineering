"""
Solution -- Exercise 1: Validate a user profile with Pydantic.

Run: python profile_validator_solution.py
"""

from pydantic import BaseModel, Field, ValidationError


class Profile(BaseModel):
    username: str
    age: int = Field(ge=13)        # ge = "greater than or equal to" 13
    email: str


# 1) Valid data -> a clean object.
good = Profile(username="aarav21", age=21, email="aarav@example.com")
print("Valid profile:", good)

# 2) Invalid data (age below 13) -> caught ValidationError.
try:
    Profile(username="kid", age=10, email="kid@example.com")
except ValidationError as err:
    print()
    print("Rejected the invalid profile:")
    print(err.errors()[0]["msg"])   # e.g. "Input should be greater than or equal to 13"
