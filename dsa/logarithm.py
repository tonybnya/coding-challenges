"""
Logarithm.
"""


def log2(num: int) -> int:
    """
    Solution.
    Time Complexity: O()
    Space Complexity: O()
    """
    if num <= 0:
        return -1

    count: int = 0
    while num > 1:
        num //= 2
        count += 1

    return count
