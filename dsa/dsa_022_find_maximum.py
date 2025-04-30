"""
014. Find maximum.
Implement the "find maximum" algorithm in Python by completing
the `find_maximum()` function. It accepts a list of integers `nums`
and returns the largest number in the list.
"""

from typing import Optional


def find_maximum(nums: list[int]) -> Optional[int]:
    """
    Solution.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not nums:
        return None

    # negative infinity
    maximum = float("-inf")  # or `-float("inf")`
    for num in nums:
        if num > maximum:
            maximum = num
    return maximum
