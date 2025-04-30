"""
015. Find longest string.
Implement the "find longest string" algorithm in Python by completing
the `find_longest_string()` function. It accepts a list of strings `strings`
and returns the longest string in the list.
"""


def find_longest_string(strings: list[str]) -> str:
    """
    Solution.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    longest: str = ""
    for s in strings:
        if len(s) > len(longest):
            longest = s

    return longest
