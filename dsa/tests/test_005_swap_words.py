"""
Test file for Swap Words algorithm.
"""

import pytest

from dsa_005_swap_words import swap_words_1, swap_words_2


def load_test_cases(filename: str) -> list[tuple[str, str]]:
    """
    Function to load test cases from a text file.
    """
    test_cases = []

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line:
                test_input, expected = line.split("=>")
                test_cases.append((test_input, expected))

    return test_cases


@pytest.mark.parametrize(
    "test_input, expected", load_test_cases("tests/test_005_swap_words.txt")
)
def test_swap_words_1(test_input: str, expected: str) -> None:
    """
    Test for first solution.
    """
    assert swap_words_1(test_input) == expected


@pytest.mark.parametrize(
    "test_input, expected", load_test_cases("tests/test_005_swap_words.txt")
)
def test_swap_words_2(test_input: str, expected: str) -> None:
    """
    Test for second solution.
    """
    assert swap_words_2(test_input) == expected
