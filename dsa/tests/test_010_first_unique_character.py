"""
Test file for Valid Anagram algorithm.
"""

import pytest

from dsa_010_first_unique_character import (
    first_unique_character_1,
    first_unique_character_2,
)


def load_test_cases(f: str) -> list[tuple[str, str, bool]]:
    """
    Function to load test cases from a text file.
    """
    tests = []

    with open(f, "r", encoding="utf-8") as file:
        for line in file:
            if line:
                s, output = line.split("=")

                expected = int(output)

                tests.append((s, expected))

    return tests


@pytest.mark.parametrize(
    "s, expected", load_test_cases("tests/test_010_first_unique_character.txt")
)
def test_first_unique_character_1(s: str, expected: int) -> None:
    """
    Test for First Solution.
    """
    assert first_unique_character_1(s) == expected


@pytest.mark.parametrize(
    "s, expected", load_test_cases("tests/test_010_first_unique_character.txt")
)
def test_first_unique_character_2(s: str, expected: int) -> None:
    """
    Test for First Solution.
    """
    assert first_unique_character_2(s) == expected
