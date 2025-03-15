"""
005. Swap Words

Given a string s, reverse the words.
Note: You may assume that there are no leading or trailing whitespaces
and each word within s is only separated by a single whitespace.

Ex: Given the following string s…
s = "The Daily Byte", return "Byte Daily The".
"""


def swap_words_1(s: str) -> str:
    """
    First Solution
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    words: list[str] = s.split(" ")  # TC & SC = O(n)
    n: int = len(words)
    temp: list[str] = [""] * n  # TC & SC = O(n)

    j: int = 0
    for i in range(n - 1, -1, -1):  # TC = O(n)
        temp[j] = words[i]
        j += 1
    # for word in words[::-1]: # TC = O(n)
    #     temp[j] = word
    #     j += 1

    return " ".join(temp)
