"""
Challenge 1: Python - Real-World Problem

Task: Write a Python function that takes a list of dictionaries
representing employees and returns the average salary of all employees.
Each dictionary has keys name, age, and salary.
"""
employees = [
    {"name": "Alice", "age": 30, "salary": 50000},
    {"name": "Bob", "age": 25, "salary": 60000},
    {"name": "Charlie", "age": 35, "salary": 70000}
]


def average_salary(employees: dict[str, str | int]) -> int :
    # Your code here
    salaries: int = 0
    for employee in employees:
        salaries += employee.get("salary")
    return salaries // len(employees)
