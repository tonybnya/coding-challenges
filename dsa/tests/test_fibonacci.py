"""
Test file.
"""

import pytest

from fibonacci import fibonacci_2, fibonacci_3


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


# @pytest.mark.parametrize(
#     "num, expected",
#     load_test_cases("./tests/test_fibonacci.txt"),
# )
# def test_fibonacci_1(num: int, expected: int) -> None:
#     """
#     Tests for Recursive solution.
#     """
#     assert fibonacci_1(num) == expected


@pytest.mark.parametrize(
    "num, expected",
    load_test_cases("./tests/test_fibonacci.txt"),
)
def test_fibonacci_2(num: int, expected: int) -> None:
    """
    Tests for solution with memoization.
    """
    assert fibonacci_2(num) == expected


@pytest.mark.parametrize(
    "num, expected",
    load_test_cases("./tests/test_fibonacci.txt"),
)
def test_fibonacci_3(num: int, expected: int) -> None:
    """
    Tests for solution with memoization.
    """
    assert fibonacci_3(num) == expected
