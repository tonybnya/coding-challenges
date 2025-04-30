"""
016. Add Numbers.
Implement the "add numbers" algorithm in Python by completing
the `add_numbers()` function. It accepts a list of numbers `nums`
and returns the sum of all of them.
"""


def add_numbers(nums: list[int]) -> int:
    """
    Solution.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not nums:
        return 0

    s: int = 0

    for num in nums:
        s += num

    return s
