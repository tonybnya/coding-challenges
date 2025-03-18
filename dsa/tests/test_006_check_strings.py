"""
Test file for Check Strings algorithm.
"""

import pytest

from dsa_006_check_strings import check_strings


def load_test_cases(filename: str) -> list[tuple[list[str], list[str], bool]]:
    """
    Function to laod test cases from a text file.
    """
    test_cases = []

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line:
                inputs, out = line.split("=>")
                in1, in2 = inputs.split(",")

                word1 = in1.split("-")
                word2 = in2.split("-")

                expected = out == "true"

                test_cases.append((word1, word2, expected))

    return test_cases


@pytest.mark.parametrize(
    "word1, word2, expected", load_test_cases("tests/test_006_check_strings.txt")
)
def test_check_strings(word1: list[str], word2: list[str], expected: bool) -> None:
    """
    Test for the solution.
    """
    assert check_strings(word1, word2) == expected
