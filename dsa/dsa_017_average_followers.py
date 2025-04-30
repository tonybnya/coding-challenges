"""
017. Average Followers.
Implement the "Average followers" algorithm in Python by completing
the `average_followers()` function. It accepts a list of numbers `nums`
and returns the average of the given list of numbers.
"""

from dsa_016_add_numbers import add_numbers


def average_followers(nums: list[int]) -> float:
    """
    Solution.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not nums:
        return 0.0

    s: int = add_numbers(nums)
    return s / len(nums)
