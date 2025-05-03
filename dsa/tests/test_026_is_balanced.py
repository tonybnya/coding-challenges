"""
Test file.
"""

import pytest

from dsa_026_is_balanced import is_balanced


def load_test_cases(filepath: str) -> list[tuple[str, bool]]:
    """
    Load test cases from the appropriate text file.
    """
    test_cases: list[tuple[str, bool]] = []

    with open(filepath, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            input_str, expected_part = line.split("=")

            expected: bool = bool(int(expected_part))

            test_cases.append((input_str, expected))

    return test_cases


@pytest.mark.parametrize(
    "input_str, expected",
    load_test_cases("./tests/test_026_is_balanced.txt"),
)
def test_is_balanced(input_str: str, expected: bool) -> None:
    """
    Tests for Is Balanced problem.
    """
    assert is_balanced(input_str) == expected
