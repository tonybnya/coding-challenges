"""
Test file.
"""

import pytest

from sorting import bubble, insertion, merge, quick


def load_test_cases(filepath: str) -> list[tuple[list[int], list[int]]]:
    """
    Load test cases from the appropriate text file.
    """
    test_cases: list[tuple[list[int], list[int]]] = []

    with open(filepath, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            input_part, expected_part = line.split("=")

            arr: list[int] = [int(n) for n in input_part.split(",")]
            expected: list[int] = [int(n) for n in expected_part.split(",")]

            test_cases.append((arr, expected))

    return test_cases


@pytest.mark.parametrize(
    "arr, expected",
    load_test_cases("./tests/test_sorting.txt"),
)
def test_bubble(arr: list[int], expected: list[int]) -> None:
    """
    Tests for Bubble Sort.
    """
    assert bubble(arr) == expected


@pytest.mark.parametrize(
    "arr, expected",
    load_test_cases("./tests/test_sorting.txt"),
)
def test_insertion(arr: list[int], expected: list[int]) -> None:
    """
    Tests for Insertion Sort.
    """
    assert insertion(arr) == expected


@pytest.mark.parametrize(
    "arr, expected",
    load_test_cases("./tests/test_sorting.txt"),
)
def test_merge(arr: list[int], expected: list[int]) -> None:
    """
    Tests for Merge Sort.
    """
    assert merge(arr) == expected


@pytest.mark.parametrize(
    "arr, expected",
    load_test_cases("./tests/test_sorting.txt"),
)
def test_quick(arr: list[int], expected: list[int]) -> None:
    """
    Tests for Quick Sort.
    """
    assert quick(arr) == expected


# @pytest.mark.parametrize(
#     "arr, expected",
#     load_test_cases("./tests/test_sorting.txt"),
# )
# def test_selection(arr: list[int], expected: list[int]) -> None:
#     """
#     Tests for Selection Sort.
#     """
#     assert selection(arr) == expected
