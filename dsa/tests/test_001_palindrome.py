"""
Test file for Palindrome algorithm.
"""

import pytest

from algo_001_palindrome import is_palindrome


def load_test_cases(filename):
    """
    Function to load test cases from a text file.
    """
    test_cases = []

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line:
                test_input, expected = line.rsplit(",", 1)
                expected = expected.strip().lower() == "true"
                test_cases.append((test_input, expected))

    return test_cases


@pytest.mark.parametrize(
    "test_input, expected", load_test_cases("tests/test_001_palindrome.txt")
)
def test_is_palindrome(test_input, expected):
    """
    Test for Optimal Solution.
    """
    assert is_palindrome(test_input) == expected
