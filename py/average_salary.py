"""
Challenge 1: Python - Real-World Problem

Task: Write a Python function that takes a list of dictionaries
representing employees and returns the average salary of all employees.
Each dictionary has keys name, age, and salary.
"""

employees = [
    {"name": "Alice", "age": 30, "salary": 50000},
    {"name": "Bob", "age": 25, "salary": 60000},
    {"name": "Charlie", "age": 35, "salary": 70000},
]


def average_salary(employees: list[dict[str, str | int]]) -> float:
    """
    Calculate the average salary of a list of employees.

    Args:
        employees: A list of dictionaries where each dictionary contains
                  keys 'name', 'age', and 'salary'.

    Returns:
        The average salary as a float.
    """
    # Your code here
    salaries: int = sum(employee.get("salary", 0) for employee in employees)
    return salaries / len(employees)
