"""
Fibonacci.
"""


def fibonacci_1(num: int) -> int:
    """
    Recursive Solution.
    Time Complexity: O()
    Space Complexity: O()
    """
    if num < 0:
        return -1

    if num in (0, 1):
        return num

    return fibonacci_1(num - 1) + fibonacci_1(num - 2)


def fibonacci_2(num: int, cache={}) -> int:
    """
    Memoization Solution.
    Time Complexity: O()
    Space Complexity: O()
    """
    if num < 0:
        return -1

    if num in (0, 1):
        return num

    if num in cache:
        return cache.get(num)

    cache[num] = fibonacci_2(num - 1, cache) + fibonacci_2(num - 2, cache)

    return cache.get(num)
