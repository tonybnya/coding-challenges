"""
Given an array of integers, modify the array in place to move all zeros
to the end while maintaining the relative order of non-zero elements.
"""


def shift_zeros_to_the_end_1(nums: list[int]) -> list[int]:
    """
    Naive Solution
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    n: int = len(nums)
    temp: list[int] = [0] * n

    j: int = 0

    for num in nums:
        if num != 0:
            temp[j] = num
            j += 1

    return temp
