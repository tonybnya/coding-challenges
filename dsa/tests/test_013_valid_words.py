"""
Test file for Valid Words algorithm.
"""

import pytest

from dsa_013_valid_words import valid_words


def load_test_cases(f: str) -> list[tuple[str, list[str], int]]:
    """
    Function to load test cases from a text file.
    """
    tests = []

    with open(f, "r", encoding="utf-8") as file:
        for line in file:
            if line:
                inputs, output = line.split("=")

                permitted, inp = inputs.split(",")
                words = inp.split(" ")

                expected = int(output)

                tests.append((permitted, words, expected))

    return tests


@pytest.mark.parametrize(
    "permitted, words, expected", load_test_cases("tests/test_013_valid_words.txt")
)
def test_valid_words(permitted: str, words: list[str], expected: int) -> None:
    """
    Test for Solution.
    """
    assert valid_words(permitted, words) == expected
