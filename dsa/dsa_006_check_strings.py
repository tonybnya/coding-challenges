"""
006. Check Strings

Given two string arrays, word1 and word2, return whether or not
the two arrays represent the same string.

Ex: Given the following word1 and word2…
word1 = ["abc", "d"], word2 = ["ab", "cd"], return true.

Ex: Given the following word1 and word2…
word1 = ["a", "b", "c"], word2 = ["a", "b", "d"], return false.
"""


def check_strings(word1: list[str], word2: list[str]) -> bool:
    """
    Solution
    Time Complexity: O(m + n)
    Space Complexity: O(m + n)
    """
    s1: str = "".join(word1)  # SC: O(m)
    s2: str = "".join(word2)  # SC: O(n)

    m: int = len(s1)
    n: int = len(s2)

    if m != n:
        return False

    i = j = 0
    while i < m:  # TC: O(m) since we've verified m == n
        if s1[i] != s2[j]:
            return False
        i += 1
        j += 1

    return True
