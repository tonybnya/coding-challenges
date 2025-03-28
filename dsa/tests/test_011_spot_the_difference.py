"""
Test file for Spot the Difference algorithm.
"""

import pytest

from dsa_011_spot_the_difference import spot_the_difference_1, spot_the_difference_2


def load_test_cases(f: str) -> list[tuple[str, str, str]]:
    """
    Function to laod test cases from a text file.
    """
    tests = []

    with open(f, "r", encoding="utf-8") as file:
        for line in file:
            if line:
                inputs, output = line.split("=")

                expected = output.strip()
                s, t = inputs.split(",")

                tests.append((s, t, expected))

    return tests


@pytest.mark.parametrize(
    "s, t, expected", load_test_cases("tests/test_011_spot_the_difference.txt")
)
def test_spot_the_difference_1(s: str, t: str, expected: str) -> None:
    """
    Test for First Solution.
    """
    assert spot_the_difference_2(s, t) == expected


@pytest.mark.parametrize(
    "s, t, expected", load_test_cases("tests/test_011_spot_the_difference.txt")
)
def test_spot_the_difference_2(s: str, t: str, expected: str) -> None:
    """
    Test for Second Solution.
    """
    assert spot_the_difference_2(s, t) == expected
