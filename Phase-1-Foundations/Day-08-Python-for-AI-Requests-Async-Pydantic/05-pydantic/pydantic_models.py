"""
Pydantic -- models that validate data automatically.

This is the backbone of structured LLM output later in the course: define the
shape you want, feed in JSON/dict, get a clean validated object (or a clear error).

Setup: pip install pydantic
Run:   python pydantic_models.py
"""

from pydantic import BaseModel, Field, ValidationError


# A model is just a class with typed fields.
class Product(BaseModel):
    name: str
    price: float = Field(gt=0)     # must be greater than 0
    tags: list[str] = []           # default: empty list


# ----- 1) Valid data -> a clean object -----
pen = Product(name="Gel Pen", price=10.0, tags=["stationery"])
print("Valid product:", pen)
print("Access a field:", pen.name, "costs Rs", pen.price)

# ----- 2) Parse straight from a dict (e.g. JSON you got from an API/LLM) -----
raw = {"name": "Notebook", "price": "55", "tags": ["paper"]}   # price is a STRING
book = Product(**raw)
print("Coerced price '55' (str) ->", book.price, type(book.price).__name__)  # 55.0 float

# ----- 3) Invalid data -> a clear ValidationError (caught, not a crash) -----
try:
    Product(name="Broken", price=-5)        # price must be > 0
except ValidationError as err:
    print("Caught a validation error (price must be > 0):")
    print(err.errors()[0]["msg"])

# ----- 4) Back to a plain dict when you need one -----
print("As a dict:", pen.model_dump())
