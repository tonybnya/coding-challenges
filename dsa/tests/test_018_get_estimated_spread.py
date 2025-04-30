"""
Test file.
"""

import pytest

from dsa_018_get_estimated_spread import get_estimated_spread


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
    "nums, expected", load_test_cases("./tests/test_018_get_estimated_spread.txt")
)
def test_get_estimated_spread(nums: list[int], expected: float) -> None:
    """
    Tests for Get Estimated Spread.
    """
    # assert get_estimated_spread(nums) == expected
    # allows a small margin of error, so 11.4869... will still pass for 11.49
    assert get_estimated_spread(nums) == pytest.approx(expected, abs=0.01)
