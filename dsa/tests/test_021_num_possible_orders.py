"""
Test file for Number of Possible Orders.
"""

import pytest

from dsa_021_num_possible_orders import num_possible_orders


def load_test_cases(filename: str) -> list[tuple[int, int]]:
    """
    Function to load test cases from a text file.
    """
    test_cases: list[tuple[int, int]] = []

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line:
                input_part, expected_part = line.split("=")

                num: int = int(input_part)
                expected: int = int(expected_part)

                test_cases.append((num, expected))

    return test_cases


@pytest.mark.parametrize(
    "num, expected", load_test_cases("./tests/test_021_num_possible_orders.txt")
)
def test_num_possible_orders(num: int, expected: int) -> None:
    """
    Test for Number of Possible Orders.
    """
    assert num_possible_orders(num) == expected
