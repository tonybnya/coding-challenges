"""
Test file.
"""

import pytest

from search import binary, linear


def load_test_cases(filepath: str) -> list[tuple[list[int], int, bool]]:
    """
    Load test cases from the appropriate text file.
    """
    test_cases: list[tuple[list[int], int, bool]] = []

    with open(filepath, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            part_one, expected_part = line.split("=")

            first, last = part_one.split("#")
            nums: list[int] = [int(n) for n in first.split(",")] if first else []
            target: int = int(last)

            expected: bool = bool(int(expected_part))

            test_cases.append((nums, target, expected))

    return test_cases


@pytest.mark.parametrize(
    "nums, target, expected",
    load_test_cases("./tests/test_binary_search.txt"),
)
def test_binary(nums: list[int], target: int, expected: bool) -> None:
    """
    Tests for Binary Search.
    """
    assert binary(nums, target) == expected


@pytest.mark.parametrize(
    "nums, target, expected",
    load_test_cases("./tests/test_linear_search.txt"),
)
def test_linear(nums: list[int], target: int, expected: bool) -> None:
    """
    Tests for Linear Search.
    """
    assert linear(nums, target) == expected
