"""
Test file for Get Influencer Score.
"""

import pytest

from dsa_020_get_influencer_score import get_influencer_score


def load_test_cases(filename: str) -> list[tuple[float, int, int]]:
    """
    Function to load test cases from a text file.
    """
    test_cases: list[tuple[float, int, int]] = []

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line:
                input_part, expected_part = line.split("=")

                percentage_str, num_str = input_part.split(",")
                average_engagement_percentage: float = float(percentage_str)
                num_followers: int = int(num_str)

                expected: int = int(expected_part)

                test_cases.append(
                    (average_engagement_percentage, num_followers, expected)
                )

    return test_cases


@pytest.mark.parametrize(
    "average_engagement_percentage, num_followers, expected",
    load_test_cases("./tests/test_020_get_influencer_score.txt"),
)
def test_get_influencer_score(
    average_engagement_percentage: float, num_followers: int, expected: int
) -> None:
    """
    Test for Get Influencer Score.
    """
    assert (
        get_influencer_score(average_engagement_percentage, num_followers) == expected
    )
