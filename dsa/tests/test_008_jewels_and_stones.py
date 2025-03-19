"""
Test file for Jewels and Stones Algorithm.
"""

import pytest

from dsa_008_jewels_and_stones import jewels_and_stones_1, jewels_and_stones_2


def load_test_cases(f: str) -> list[tuple[str, str, int]]:
    """
    Function to load test cases from a text file.
    """
    tests = []

    with open(f, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line:
                inputs, output = line.split("=")

                jewels, stones = inputs.split(",")
                expected = int(output)

                tests.append((jewels, stones, expected))

    return tests


@pytest.mark.parametrize(
    "jewels, stones, expected", load_test_cases("tests/test_008_jewels_and_stones.txt")
)
def test_jewels_and_stones_1(jewels: str, stones: str, expected: int) -> None:
    """
    Test for Solution.
    """
    assert jewels_and_stones_1(jewels, stones) == expected


@pytest.mark.parametrize(
    "jewels, stones, expected", load_test_cases("tests/test_008_jewels_and_stones.txt")
)
def test_jewels_and_stones_2(jewels: str, stones: str, expected: int) -> None:
    """
    Test for Solution.
    """
    assert jewels_and_stones_2(jewels, stones) == expected
