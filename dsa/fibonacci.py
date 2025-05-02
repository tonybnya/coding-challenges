"""
Fibonacci.
"""


def fibonacci_1(num: int) -> int:
    """
    Recursive Solution.
    Time Complexity: O(2^n)
    Space Complexity: O(n)
    """
    if num < 0:
        return -1

    if num in (0, 1):
        return num

    return fibonacci_1(num - 1) + fibonacci_1(num - 2)


def fibonacci_2(num: int, cache={}) -> int:
    """
    Memoization Solution.
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if num < 0:
        return -1

    if num in (0, 1):
        return num

    if num in cache:
        return cache.get(num)

    cache[num] = fibonacci_2(num - 1, cache) + fibonacci_2(num - 2, cache)

    return cache.get(num)


def fibonacci_3(num: int) -> int:
    """
    Iterative Solution (Bottom-Up).
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if num < 0:
        return -1

    if num in (0, 1):
        return num

    current: int = 0
    parent: int = 1
    grand_parent: int = 0

    for _ in range(num - 1):
        current = parent + grand_parent
        grand_parent = parent
        parent = current

    return current
