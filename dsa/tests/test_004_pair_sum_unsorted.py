"""
Test file for Pair Sum Unsorted algorithm.
"""

import pytest

from dsa_004_pair_sum_unsorted import (
    pair_sum_unsorted_1,
    pair_sum_unsorted_2,
    pair_sum_unsorted_3,
)


def load_test_cases(f: str) -> list[tuple[list[int], int, list[int]]]:
    """
    Function to laod test cases from a text file.
    """
    tests = []

    with open(f, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line:
                inputs, output = line.split("=")
                input_1, input_2 = inputs.split("->")

                inp = input_1.split(",")
                nums = [] if inp[0] == "" else [int(n) for n in inp]

                target = int(input_2)

                out = output.split(",")
                expected = [] if out[0] == "" else [int(n) for n in out]
                tests.append((nums, target, expected))

    return tests


@pytest.mark.parametrize(
    "nums, target, expected", load_test_cases("tests/test_004_pair_sum_unsorted.txt")
)
def test_pair_sum_unsorted_1(nums: list[int], target: int, expected: list[int]) -> None:
    """
    Test for Naive Solution.
    """
    assert pair_sum_unsorted_1(nums, target) == expected


# @pytest.mark.parametrize(
#     "nums, target, expected", load_test_cases("tests/test_004_pair_sum_unsorted.txt")
# )
# def test_pair_sum_unsorted_2(nums: list[int], target: int, expected: list[int]) -> None:
#     """
#     Test for Optimal Solution.
#     """
#     assert pair_sum_unsorted_2(nums, target) == expected


@pytest.mark.parametrize(
    "nums, target, expected", load_test_cases("tests/test_004_pair_sum_unsorted.txt")
)
def test_pair_sum_unsorted_3(nums: list[int], target: int, expected: list[int]) -> None:
    """
    Test for Optimal Solution.
    """
    assert pair_sum_unsorted_3(nums, target) == expected
