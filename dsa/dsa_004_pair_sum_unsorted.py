"""
004. Pair Sum - Unsorted

Given an array of integers, return the indexes of any two numbers that add up
to a target. The order of the indexes in the result doesn't matter.
If no pair is found, return an empty array.
"""


def pair_sum_unsorted_1(nums: list[int], target: int) -> list[int]:
    """
    Naive solution 1: Two loops
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    n: int = len(nums)

    for i in range(n):
        for j in range(i + 1, n):
            s: int = nums[i] + nums[j]
            if s == target:
                return [i, j]

    return []


def pair_sum_unsorted_2(nums: list[int], target: int) -> list[int]:
    """
    Naive solution 2: Sorting + Two pointers (Inward traversal)
    Time Complexity: O(nlogn)
    Space Complexity: O(1)
    """
    n: int = len(nums)
    sorted(nums)

    l, r = 0, n - 1

    while l < r:
        s: int = nums[l] + nums[r]

        if s == target:
            return [l, r]
        elif s > target:
            r -= 1
        else:
            l += 1

    return []


def pair_sum_unsorted_3(nums: list[int], target: int) -> list[int]:
    """
    Optimal solution
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    hmap: dict[int, int] = {}

    for i, num in enumerate(nums):
        diff: int = target - num
        if diff in hmap:
            return [hmap[diff], i]
        hmap[num] = i

    return []
