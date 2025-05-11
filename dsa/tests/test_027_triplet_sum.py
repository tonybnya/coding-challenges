"""
Test file for Triplet Sum algorithm.
"""

import pytest

from dsa_027_triplet_sum import triplet_sum_1


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([0, -1, 2, -3, 1], [[-1, 0, 1], [-3, 1, 2]]),
        ([-1, 0, 1, 2, -1, -4], [[-1, 0, 1], [-1, -1, 2]]),
        ([0, 0, 0, 0], [[0, 0, 0]]),
        ([1, 2, -2, -1], []),
        ([0, 1], []),
        ([-2, 0, 1, 1, 2], [[-2, 0, 2], [-2, 1, 1]]),
        (
            [-4, -2, -2, 0, 1, 2, 2, 3, 4, 5],
            [[-4, 1, 3], [-4, 2, 2], [-2, -2, 4], [-4, 0, 4], [-2, 0, 2]],
        ),
    ],
)
def test_pair_sum_1(nums: list[int], expected: list[list[int]]) -> None:
    """
    Test for Naive Solution.
    """
    assert triplet_sum_1(nums) == expected
