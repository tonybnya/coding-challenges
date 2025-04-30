"""
Test file.
"""

import pytest

from dsa_019_get_follower_prediction import get_follower_prediction


def load_test_cases(filepath: str) -> list[tuple[int, str, int, int]]:
    """
    Load test cases from the appropriate text file.
    """
    test_cases: list[tuple[int, str, int, int]] = []

    with open(filepath, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            input_part, expected_part = line.split("=")

            count_str, influencer_type, months_str = input_part.split(",")

            follower_count: int = int(count_str)
            num_months: int = int(months_str)

            expected: int = int(expected_part)

            test_cases.append((follower_count, influencer_type, num_months, expected))

    return test_cases


@pytest.mark.parametrize(
    "follower_count, influencer_type, num_months, expected",
    load_test_cases("./tests/test_019_get_follower_prediction.txt"),
)
def test_get_follower_prediction(follower_count: int, influencer_type: str, num_months: int, expected: int) -> None:
    """
    Tests for Get Follower Prediction.
    """
    assert (
        get_follower_prediction(follower_count, influencer_type, num_months) == expected
    )
