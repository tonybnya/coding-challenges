"""
014. Find minimum.
Implement the "find minimum" algorithm in Python by completing
the `find_minimum()` function. It accepts a list of integers `nums`
and returns the smallest number in the list.
"""

from typing import Optional


def find_minimum(nums: list[int]) -> Optional[int]:
    """
    Solution.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not nums:
        return None

    # positive infinity
    minimum = float("inf")
    for num in nums:
        if num < minimum:
            minimum = num
    return minimum
