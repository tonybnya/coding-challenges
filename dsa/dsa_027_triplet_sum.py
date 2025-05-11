"""
027. Triplet Sum

Given an array of integers, return all triplets [a, b, c] such that a + b + c = 0.
The solution must not contain duplicate triplets (e.g., [1, 2, 3] and [2, 3, 1]
are considered duplicate triplets). If no such triplets are found, return an empty
array.
"""


def triplet_sum_1(nums: list[int]) -> list[list[int]]:
    """
    Naive Solution: Three nested loops
    Time Complexity: O(n^3)
    Space Complexity: O(1)
    """
    n: int = len(nums)
    total: int = 0
    triplets: set = set()

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == total:
                    triplet: tuple = tuple(sorted([nums[i], nums[j], nums[k]]))
                    triplets.add(triplet)

    return [list(triplet) for triplet in triplets]
