"""
009. Valid Anagram

This question is asked by Facebook.
Given two strings s and t return whether or not s is an anagram of t.
Note: An anagram is a word formed by reordering the letters of another word.

Ex: Given the following strings...

s = "cat", t = "tac", return true
s = "listen", t = "silent", return true
s = "program", t = "function", return false
"""


def valid_anagram_1(s: str, t: str) -> bool:
    """
    First Solution: Two Hashmaps
    Time Complexity: O(m + n)
    Space Complexity: O(m + n)
    """
    m: int = len(s)
    n: int = len(t)

    if m != n:
        return False

    hmap_s: dict = {}
    hmap_t: dict = {}

    for c in s:
        hmap_s[c] = hmap_s.get(c, 0) + 1

    for c in t:
        hmap_t[c] = hmap_t.get(c, 0) + 1

    return hmap_s == hmap_t


def valid_anagram_2(s: str, t: str) -> bool:
    """
    First Solution:
    Time Complexity: O(m + n)
    Space Complexity: O(m + n)
    """
    m: int = len(s)
    n: int = len(t)

    if m != n:
        return False

    return set(s) == set(t)
