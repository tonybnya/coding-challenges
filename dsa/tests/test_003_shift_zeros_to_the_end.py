"""
Test file for Shift Zeros to the End algorithm.
"""

import pytest

from dsa_003_shift_zeros_to_the_end import (
    shift_zeros_to_the_end_1,
    shift_zeros_to_the_end_2,
)


def load_test_cases(f: str) -> list[tuple[list[int], list[int]]]:
    """
    Function to load test cases from a text file.
    """
    tests = []

    with open(f, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line:
                inp, output = line.split("=")

                nums = [] if inp == "?" else [int(n) for n in inp.split(",")]
                expected = [] if output == "?" else [int(n) for n in output.split(",")]

                tests.append((nums, expected))

    return tests


@pytest.mark.parametrize(
    "nums, expected", load_test_cases("tests/test_003_shift_zeros_to_the_end.txt")
)
def test_003_shift_zeros_to_the_end_1(nums, expected) -> None:
    """
    Test for Naive Solution.
    """
    assert shift_zeros_to_the_end_1(nums) == expected


@pytest.mark.parametrize(
    "nums, expected", load_test_cases("tests/test_003_shift_zeros_to_the_end.txt")
)
def test_003_shift_zeros_to_the_end_2(nums, expected) -> None:
    """
    Test for Naive Solution.
    """
    assert shift_zeros_to_the_end_2(nums) == expected
