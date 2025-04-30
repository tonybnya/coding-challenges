"""
Test file.
"""

from typing import Optional

import pytest

from dsa_023_does_name_exist import does_name_exist


def load_test_cases(filepath: str) -> list[tuple[list[str], list[str], str, bool]]:
    """
    Load test cases from the appropriate text file.
    """
    test_cases: list[tuple[list[str], list[str], str, bool]] = []

    with open(filepath, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            part_one, expected_part = line.split("=")

            names_part, fullname = part_one.split("#")

            first, last = names_part.split("+")
            firstnames = first.split(",")
            lastnames = last.split(",")

            expected: bool = bool(int(expected_part))

            test_cases.append((firstnames, lastnames, fullname, expected))

    return test_cases


@pytest.mark.parametrize(
    "firstnames, lastnames, fullname, expected",
    load_test_cases("./tests/test_023_does_name_exist.txt"),
)
def test_find_maximum(
    firstnames: list[str], lastnames: list[str], fullname: str, expected: bool
) -> None:
    """
    Tests for Does Name Exist.
    """
    assert does_name_exist(firstnames, lastnames, fullname) == expected
