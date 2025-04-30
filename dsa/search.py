"""
Search Algorithms.
"""


def linear(nums: list[int], target: int) -> bool:
    """
    Linear Search.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if len(nums) == 0:
        return False

    for num in nums:
        if num == target:
            return True

    return False


def binary(nums: list[int], target: int) -> bool:
    """
    Binary Search.
    Time Complexity: O(logn)
    Space Complexity: O(1)
    """
    if len(nums) == 0:
        return False

    l, r = 0, len(nums) - 1
    while l <= r:
        mid: int = l + (r - l) // 2
        if nums[mid] == target:
            return True
        if nums[mid] > target:
            r = mid - 1
        if nums[mid] < target:
            l = mid + 1

    return False
