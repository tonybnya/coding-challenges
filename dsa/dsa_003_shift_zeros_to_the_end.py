"""
Given an array of integers, modify the array in place to move all zeros
to the end while maintaining the relative order of non-zero elements.
"""


def shift_zeros_to_the_end_1(nums: list[int]) -> list[int]:
    """
    Naive Solution: Temporary list
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


def shift_zeros_to_the_end_2(nums: list[int]) -> None:
    """
    Optimal Solution
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    n: int = len(nums)
    i, j = 0, 0

    for i in range(n):
        if nums[i] != 0:
            nums[j], nums[i] = nums[i], nums[j]
            j += 1

    while j < n:
        nums[j] = 0
        j += 1

    return nums
