"""
Test file.
"""

import pytest

from dsa_015_find_longest_string import find_longest_string


def load_test_cases(filepath: str) -> list[tuple[list[str], str]]:
    """
    Load test cases from the appropriate text file.
    """
    test_cases: list[tuple[list[str], str]] = []

    with open(filepath, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            input_part, expected = line.split("=")
            strings: list[str] = [s for s in input_part.split(" ")]
            test_cases.append((strings, expected))

    return test_cases


@pytest.mark.parametrize(
    "strings, expected", load_test_cases("./tests/test_015_find_longest_string.txt")
)
def test_find_minimum(strings: list[str], expected: str) -> None:
    """
    Tests for Find Longest String.
    """
    assert find_longest_string(strings) == expected
