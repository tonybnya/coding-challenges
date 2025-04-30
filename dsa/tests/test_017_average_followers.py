"""
Test file.
"""

import pytest

from dsa_017_average_followers import average_followers


def load_test_cases(filepath: str) -> list[tuple[list[int], float]]:
    """
    Load test cases from the appropriate text file.
    """
    test_cases: list[tuple[list[int], float]] = []

    with open(filepath, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            input_part, expected_part = line.split("=")
            nums: list[int] = (
                [int(n) for n in input_part.split(",")] if input_part else []
            )
            expected: float = float(expected_part)
            test_cases.append((nums, expected))

    return test_cases


@pytest.mark.parametrize(
    "nums, expected", load_test_cases("./tests/test_017_average_followers.txt")
)
def test_average_followers(nums: list[int], expected: float) -> None:
    """
    Tests for Average Followers.
    """
    assert average_followers(nums) == expected
