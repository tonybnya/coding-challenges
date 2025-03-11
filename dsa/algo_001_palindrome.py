"""
Task: Implement a function that checks if a given string is a palindrome.
A palindrome is a string that reads the same forwards and backwards
(ignoring spaces, punctuation, and capitalization).
"""


def is_palindrome(s: str) -> bool:
    """
    Optimal solution
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    i: int = 0
    j: int = len(s) - 1

    while i < j:
        if not s[i].isalnum():
            i += 1
            continue
        if not s[j].isalnum():
            j -= 1
            continue
        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1

    return True
