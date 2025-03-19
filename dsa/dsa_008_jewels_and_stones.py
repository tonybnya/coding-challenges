"""
008. Jewels and Stones

This question is asked by Amazon.
Given a string representing your stones and another string representing
a list of jewels, return the number of stones that you have that are also jewels.

Ex: Given the following jewels and stones...

jewels = "abc", stones = "ac", return 2
jewels = "Af", stones = "AaaddfFf", return 3
jewels = "AYOPD", stones = "ayopd", return 0
"""


def jewels_and_stones_1(jewels: str, stones: str) -> int:
    """
    First Solution: Two Hashmaps
    Time Complexity: O(m + n)
    Space Complexity: O(m + n)
    """
    hmap_j: dict = {}  # SC: O(m)
    hmap_s: dict = {}  # SC: O(n)

    for c in jewels:  # TC: O(m)
        hmap_j[c] = hmap_j.get(c, 0) + 1

    for c in stones:  # TC: O(n)
        hmap_s[c] = hmap_s.get(c, 0) + 1

    count: int = 0

    for c in hmap_s.keys():  # TC: O(n)
        if c in hmap_j:
            count += hmap_s[c]

    return count


def jewels_and_stones_2(jewels: str, stones: str) -> int:
    """
    First Solution: One Hashmap
    Time Complexity: O(m + n)
    Space Complexity: O()
    """
    hmap: dict = {}  # SC: O(m)

    for c in stones:
        hmap[c] = hmap.get(c, 0) + 1

    count: int = 0

    for c in jewels:
        if c in hmap:
            count += hmap[c]

    return count
