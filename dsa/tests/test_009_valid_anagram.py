"""
Test file for Valid Anagram algorithm.
"""

import pytest

from dsa_009_valid_anagram import valid_anagram_1, valid_anagram_2


def load_test_cases(f: str) -> list[tuple[str, str, bool]]:
    """
    Function to load test cases from a text file.
    """
    tests = []

    with open(f, "r", encoding="utf-8") as file:
        for line in file:
            if line:
                inputs, output = line.split("=")

                s, t = inputs.split(",")
                expected = output.strip().lower() == "true"

                tests.append((s, t, expected))

    return tests


@pytest.mark.parametrize(
    "s, t, expected", load_test_cases("tests/test_009_valid_anagram.txt")
)
def test_valid_anagram_1(s: str, t: str, expected: bool) -> None:
    """
    Test for First Solution.
    """
    assert valid_anagram_1(s, t) == expected


@pytest.mark.parametrize(
    "s, t, expected", load_test_cases("tests/test_009_valid_anagram.txt")
)
def test_valid_anagram_2(s: str, t: str, expected: bool) -> None:
    """
    Test for First Solution.
    """
    assert valid_anagram_2(s, t) == expected
