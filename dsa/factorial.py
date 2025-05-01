"""
Factorial.
"""


def factorial_1(num: int) -> int:
    """
    Naive Solution.
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if num < 0:
        return -1

    if num == 0 or num == 1:
        return 1

    return num * factorial_1(num - 1)
