"""
010. First Unique Character

This question is asked by Microsoft.
Given a string, return the index of its first unique character.
If a unique character does not exist, return -1.

Ex: Given the following strings...

"abcabd", return 2
"thedailybyte", return 1
"developer", return 0
"""


def first_unique_character_1(s: str) -> int:
    """
    First Solution: Two loops
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    n: int = len(s)

    for i in range(n):
        unique: bool = True
        for j in range(n):
            if i != j and s[j] == s[i]:
                unique = False
                break

        if unique:
            return i

    return -1
