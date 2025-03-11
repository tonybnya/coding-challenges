"""
Given an array of integers sorted in ascending order and a target value,
return the indexes of any pair of numbers in the array that sum to the target.
The order of the indexes in the result doesn't matter.
If no pair is fund, return an empty array.
"""


def pair_sum_1(nums: list[int], target: int) -> list[int]:
    """
    Naive Solution
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    n: int = len(nums)

    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]

    return []


def pair_sum_2(nums: list[int], target: int) -> list[int]:
    """
    Optimal Solution
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    n: int = len(nums)
    l, r = 0, n - 1

    while l < r:
        s: int = nums[l] + nums[r]

        if s > target:
            r -= 1
        if s < target:
            l += 1
        else:
            return [l, r]

    return []
