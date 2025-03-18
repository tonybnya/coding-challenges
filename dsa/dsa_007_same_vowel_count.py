"""
007. Same Vowel Count

Given an even length string, s, return whether or not
the first half of s and the second half of s contain the same number of vowels.

Ex: Given the following string s…
s = "laptop", return true (there is one vowel in "lap" and one vowel in "top").

Ex: Given the following string s…
s = "computer", return false.
"""


def same_vowel_count_1(s: str) -> bool:
    """
    First Solution: Two Pointers (two loops)
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    vowels = ("a", "e", "i", "o", "u", "y")  # SC: O(6) -> 6 is a constant, so O(1)
    n: int = len(s)

    mid: int = n // 2
    lhv, rhv = 0, 0

    l, r = 0, n - 1

    for l in range(mid):
        if s[l].lower() in vowels:
            lhv += 1

    for r in range(n - 1, mid - 1, -1):
        if s[r].lower() in vowels:
            rhv += 1

    return lhv == rhv
