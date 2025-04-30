"""
Test file.
"""

from typing import Optional

import pytest

from dsa_014_find_minimum import find_minimum


def load_test_cases(filepath: str) -> list[tuple[list[int], Optional[int]]]:
    """
    Load test cases from the appropriate text file.
    """
    test_cases: list[tuple[list[int], Optional[int]]] = []

    with open(filepath, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            input_part, expected_part = line.split("=")
            nums: list[int] = (
                [int(n) for n in input_part.split(",") if n] if input_part else []
            )
            if expected_part == "None":
                expected = None
            else:
                expected = int(expected_part)
            test_cases.append((nums, expected))

    return test_cases


@pytest.mark.parametrize(
    "nums, expected", load_test_cases("./tests/test_014_find_minimum.txt")
)
def test_find_minimum(nums: list[int], expected: Optional[int]) -> None:
    """
    Tests for Find Minimum.
    """
    assert find_minimum(nums) == expected
