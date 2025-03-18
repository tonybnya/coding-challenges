"""
Test file for Same Vowel Count algorithm.
"""

import pytest

from dsa_007_same_vowel_count import same_vowel_count_1


def load_test_cases(filename: str) -> list[tuple[str, bool]]:
    """
    Function to load test cases from a text file.
    """
    test_cases = []

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line:
                test_input, expected = line.split("=>")
                expected = expected == "true"

                test_cases.append((test_input, expected))

    return test_cases


@pytest.mark.parametrize(
    "test_input, expected", load_test_cases("tests/test_007_same_vowel_count.txt")
)
def test_same_vowel_count_1(test_input: str, expected: bool) -> None:
    """
    Test for First Solution
    """
    assert same_vowel_count_1(test_input) == expected
