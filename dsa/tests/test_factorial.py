"""
Test file.
"""

import pytest

from factorial import factorial_1


def load_test_cases(filepath: str) -> list[tuple[int, int]]:
    """
    Load test cases from the appropriate text file.
    """
    test_cases: list[tuple[int, int]] = []

    with open(filepath, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            input_part, expected_part = line.split("=")

            num: int = int(input_part)
            expected: int = int(expected_part)

            test_cases.append((num, expected))

    return test_cases


@pytest.mark.parametrize(
    "num, expected",
    load_test_cases("./tests/test_factorial.txt"),
)
def test_factorial_1(num: int, expected: int) -> None:
    """
    Tests for Factorial.
    """
    assert factorial_1(num) == expected
