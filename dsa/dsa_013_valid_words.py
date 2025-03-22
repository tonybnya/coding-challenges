"""
013. Valid Words

Given a string 'permitted' and a string array, 'words'.
Valid words are strings within words that only contain permitted characters.
Return the total number of valid words.

Ex: Given the following permitted and words…
permitted = "abc", words = ["d", "ab", "abce"], return 1.

Ex: Given the following permitted and words…
permitted = "ake", words = ["ail", "kea", "a"], return 2.
"""


def valid_words(permitted: str, words: list[str]) -> int:
    """
    Solution:
    Time Complexity: O(n + m) n is the number of words, m is the average length of each word
    Space Complexity: O(k) k is the number of unique characters in the permitted string
    """
    hset: set = set(permitted)
    count: int = 0

    for word in words:
        is_valid = True
        for c in word:
            if c not in hset:
                is_valid = False
                break
        
        if is_valid:
            count += 1

    return count
