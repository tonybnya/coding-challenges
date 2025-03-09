import pytest

from algo_001_palindrome import is_palindrome


def load_test_cases(filename):
    test_cases = []
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line:  # Ignore empty lines
                test_input, expected = line.rsplit(
                    ",", 1
                )  # Split input and expected value
                expected = expected.strip().lower() == "true"  # Convert to boolean
                test_cases.append((test_input, expected))
    return test_cases


@pytest.mark.parametrize(
    "test_input, expected", load_test_cases("tests/test_001_palindrome.txt")
)
def test_is_palindrome(test_input, expected):
    assert is_palindrome(test_input) == expected
