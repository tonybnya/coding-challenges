"""
Test file.
"""

import pytest

from dsa_025_count_marketers import count_marketers


def load_test_cases(filepath: str) -> list[tuple[list[str], int]]:
    """
    Load test cases from the appropriate text file.
    """
    test_cases: list[tuple[list[str], int]] = []

    with open(filepath, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            input_part, expected_part = line.split("=")

            job_titles: list[str] = input_part.split(",") if input_part else []
            expected: int = int(expected_part)

            test_cases.append((job_titles, expected))

    return test_cases


@pytest.mark.parametrize(
    "job_titles, expected",
    load_test_cases("./tests/test_025_count_marketers.txt"),
)
def test_count_marketers(job_titles: list[str], expected: int) -> None:
    """
    Tests for Count Marketers.
    """
    assert count_marketers(job_titles) == expected
