"""
Problem 15 - Class gradebook   (SOLUTION)

Run:
    python q15_gradebook_solution.py

Logic note:
  This is the capstone: a dict whose VALUES are lists (nested data). sum(marks)/
  len(marks) is the average per student. topper() reuses averages() instead of
  recomputing -- build small functions and stack them. "best so far" finds the max.
"""

def averages(gradebook):
    """Return {name: average mark rounded to 2 decimals}."""
    result = {}
    for name, marks in gradebook.items():
        result[name] = round(sum(marks) / len(marks), 2)
    return result
 

def topper(gradebook):
    """Return (name, average) for the student with the highest average."""
    avgs = averages(gradebook)
    best_name = ""
    best_avg = -1
    for name, avg in avgs.items():
        if avg > best_avg:
            best_name = name
            best_avg = avg
    return (best_name, best_avg)


if __name__ == "__main__":
    book = {"Asha": [88, 92, 79], "Ravi": [70, 65, 80], "Meena": [95, 99, 91]}
    print("averages:", averages(book))
    name, avg = topper(book)
    print(f"topper  : {name} with {avg}")
