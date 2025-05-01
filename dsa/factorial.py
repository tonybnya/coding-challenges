"""
Factorial.
"""


def factorial_1(num: int) -> int:
    """
    Recursive Solution.
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if num < 0:
        return -1

    if num in (0, 1):
        return 1

    return num * factorial_1(num - 1)


def factorial_2(num: int) -> int:
    """
    Iterative Solution.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if num < 0:
        return -1

    if num in (0, 1):
        return 1

    result: int = 1

    for i in range(2, num + 1):
        result *= i

    return result
