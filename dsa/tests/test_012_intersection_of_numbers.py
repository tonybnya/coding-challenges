"""
Test file for Intersection of Numbers algorithm.
"""

import pytest

from dsa_012_intersection_of_numbers import intersection_of_numbers


def load_test_cases(f: str) -> list[tuple[list[int], list[int], list[int]]]:
    """
    Function to load test cases from a text file.
    """
    tests = []

    with open(f, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line:
                inputs, output = line.split("=")
                input1, input2 = inputs.split("->")

                inp1 = input1.split(",")
                nums1 = [] if inp1[0] == "" else [int(n) for n in inp1]

                inp2 = input2.split(",")
                nums2 = [] if inp2[0] == "" else [int(n) for n in inp2]

                out = output.split(",")
                expected = [] if out[0] == "" else [int(n) for n in out]

                tests.append((nums1, nums2, expected))

    return tests


@pytest.mark.parametrize(
    "nums1, nums2, expected",
    load_test_cases("tests/test_012_intersection_of_numbers.txt"),
)
def test_intersection_of_numbers(
    nums1: list[int], nums2: list[int], expected: list[int]
) -> None:
    """
    Test for Solution.
    """
    assert intersection_of_numbers(nums1, nums2) == expected
