"""
012. Intersection of Numbers

This question is asked by Google. Given two integer arrays,
return their intersection.
Note: the intersection is the set of elements that are common to both arrays.

Ex: Given the following arrays...

nums1 = [2, 4, 4, 2], nums2 = [2, 4], return [2, 4]
nums1 = [1, 2, 3, 3], nums2 = [3, 3], return [3]
nums1 = [2, 4, 6, 8], nums2 = [1, 3, 5, 7], return []
"""


def intersection_of_numbers_1(nums1: list[int], nums2: list[int]) -> list[int]:
    """
    Naive Solution: Two Loops
    Time Complexity: O(m * n)
    Space Complexity: O()  # ?
    """
    m: int = len(nums1)
    n: int = len(nums2)

    res: list[int] = []

    for i in range(m):
        for j in range(n):
            if nums1[i] == nums2[j]:
                res.append(nums1[i])

    return list(set(res))


def intersection_of_numbers_2(nums1: list[int], nums2: list[int]) -> list[int]:
    """
    Naive Solution: Hashset
    Time Complexity: O(m + n)  # m = len(nums1), n = len(nums2)
    Space Complexity: O(m)
    """
    hset: set = set()

    for num in nums1:
        hset.add(num)

    res: list[int] = []
    for num in nums2:
        if num in hset:
            res.append(num)
            hset.remove(num)

    return res
