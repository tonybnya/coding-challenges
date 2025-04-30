"""
Test file.
"""

import pytest

from dsa_016_add_numbers import add_numbers


def load_test_cases(filepath: str) -> list[tuple[list[int], int]]:
    """
    Load test cases from the appropriate text file.
    """
    test_cases: list[tuple[list[int], int]] = []

    with open(filepath, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            input_part, expected_part = line.split("=")
            nums: list[int] = (
                [int(n) for n in input_part.split(",")] if input_part else []
            )
            expected: int = int(expected_part)
            test_cases.append((nums, expected))

    return test_cases


@pytest.mark.parametrize(
    "nums, expected", load_test_cases("./tests/test_016_add_numbers.txt")
)
def test_add_numbers(nums: list[int], expected: int) -> None:
    """
    Tests for Add Numbers.
    """
    assert add_numbers(nums) == expected
