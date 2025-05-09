"""
Test file for Triplet Sum algorithm.
"""

import pytest

from number_conversions import (
    base_to_int,
    binary_to_int,
    hex_to_int,
    int_to_base,
    int_to_binary,
    int_to_hex,
    int_to_octal,
    octal_to_int,
)


@pytest.mark.parametrize(
    "binary_str, expected",
    [
        ("0", 0),
        ("1", 1),
        ("10", 2),
        ("11", 3),
        ("100", 4),
        ("101", 5),
        ("110", 6),
        ("111", 7),
        ("1000", 8),
        ("1001", 9),
        ("1010", 10),
        ("1011", 11),
        ("1100", 12),
        ("1101", 13),
        ("1110", 14),
        ("1111", 15),
        ("10000", 16),
        ("10101", 21),
        ("11010", 26),
        ("11111", 31),
        ("100000", 32),
        ("111111", 63),
        ("1000000", 64),
    ],
)
def test_binary_to_int(binary_str: str, expected: int) -> None:
    """
    Test.
    """
    assert binary_to_int(binary_str) == expected


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, "0"),
        (1, "1"),
        (2, "10"),
        (3, "11"),
        (4, "100"),
        (5, "101"),
        (6, "110"),
        (7, "111"),
        (8, "1000"),
        (9, "1001"),
        (10, "1010"),
        (11, "1011"),
        (12, "1100"),
        (13, "1101"),
        (14, "1110"),
        (15, "1111"),
        (16, "10000"),
        (21, "10101"),
        (26, "11010"),
        (31, "11111"),
        (32, "100000"),
        (63, "111111"),
        (64, "1000000"),
    ],
)
def test_int_to_binary(n: int, expected: str) -> None:
    """
    Test.
    """
    assert int_to_binary(n) == expected


@pytest.mark.parametrize(
    "hex_str, expected",
    [
        ("0", 0),
        ("1", 1),
        ("A", 10),
        ("B", 11),
        ("C", 12),
        ("D", 13),
        ("E", 14),
        ("F", 15),
        ("10", 16),
        ("1A", 26),
        ("1F", 31),
        ("20", 32),
        ("2A", 42),
        ("3E", 62),
        ("64", 100),
        ("7F", 127),
        ("100", 256),
        ("1A3", 419),
        ("FF", 255),
        ("1FF", 511),
        ("1000", 4096),
    ],
)
def test_hex_to_int(hex_str: str, expected: int) -> None:
    """
    Test.
    """
    assert hex_to_int(hex_str) == expected


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, "0"),
        (1, "1"),
        (10, "A"),
        (11, "B"),
        (12, "C"),
        (13, "D"),
        (14, "E"),
        (15, "F"),
        (16, "10"),
        (26, "1A"),
        (31, "1F"),
        (32, "20"),
        (42, "2A"),
        (62, "3E"),
        (100, "64"),
        (127, "7F"),
        (255, "FF"),
        (256, "100"),
        (419, "1A3"),
        (511, "1FF"),
        (4096, "1000"),
    ],
)
def test_int_to_hex(n: int, expected: str) -> None:
    """
    Test.
    """
    assert int_to_hex(n) == expected


@pytest.mark.parametrize(
    "octal_str, expected",
    [
        ("0", 0),
        ("1", 1),
        ("7", 7),
        ("10", 8),
        ("11", 9),
        ("12", 10),
        ("17", 15),
        ("20", 16),
        ("25", 21),
        ("30", 24),
        ("77", 63),
        ("100", 64),
        ("123", 83),
        ("177", 127),
        ("200", 128),
        ("377", 255),
        ("400", 256),
        ("777", 511),
        ("1000", 512),
    ],
)
def test_octal_to_int(octal_str: str, expected: int) -> None:
    """
    Test.
    """
    assert octal_to_int(octal_str) == expected


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, "0"),
        (1, "1"),
        (7, "7"),
        (8, "10"),
        (9, "11"),
        (10, "12"),
        (15, "17"),
        (16, "20"),
        (21, "25"),
        (24, "30"),
        (63, "77"),
        (64, "100"),
        (83, "123"),
        (127, "177"),
        (128, "200"),
        (255, "377"),
        (256, "400"),
        (511, "777"),
        (512, "1000"),
    ],
)
def test_int_to_octal(n: int, expected: str) -> None:
    """
    Test.
    """
    assert int_to_octal(n) == expected


@pytest.mark.parametrize(
    "number_str, base, expected",
    [
        # Binary (base 2)
        ("0", 2, 0),
        ("1", 2, 1),
        ("10", 2, 2),
        ("101", 2, 5),
        ("1111", 2, 15),
        ("100000", 2, 32),
        # Octal (base 8)
        ("0", 8, 0),
        ("7", 8, 7),
        ("10", 8, 8),
        ("17", 8, 15),
        ("77", 8, 63),
        ("1234", 8, 668),
        # Decimal (base 10)
        ("0", 10, 0),
        ("5", 10, 5),
        ("42", 10, 42),
        ("123", 10, 123),
        ("9999", 10, 9999),
        # Hexadecimal (base 16)
        ("0", 16, 0),
        ("A", 16, 10),
        ("F", 16, 15),
        ("10", 16, 16),
        ("1A", 16, 26),
        ("FF", 16, 255),
        ("abc", 16, 2748),
        ("ABC", 16, 2748),
        ("1A3", 16, 419),
        # Invalid base cases (unknown bases return -1)
        ("101", 1, -1),
        ("123", 37, -1),
        ("100", -5, -1),
        ("123", 0, -1),
        ("123", 100, -1),
    ],
)
def test_base_to_int(number_str: str, base: int, expected: int) -> None:
    """
    Test.
    """
    assert base_to_int(number_str, base) == expected


@pytest.mark.parametrize(
    "n, base, expected",
    [
        # Binary
        (0, 2, "0"),
        (1, 2, "1"),
        (2, 2, "10"),
        (11, 2, "1011"),
        (32, 2, "100000"),
        # Octal
        (0, 8, "0"),
        (8, 8, "10"),
        (15, 8, "17"),
        (63, 8, "77"),
        (668, 8, "1234"),
        # Decimal
        (0, 10, "0"),
        (5, 10, "5"),
        (42, 10, "42"),
        (9999, 10, "9999"),
        # Hexadecimal
        (0, 16, "0"),
        (10, 16, "A"),
        (15, 16, "F"),
        (16, 16, "10"),
        (26, 16, "1A"),
        (255, 16, "FF"),
        (2748, 16, "ABC"),
        # Unknown base
        (123, 1, -1),
        (456, 20, -1),
        (789, -2, -1),
    ],
)
def test_int_to_base(n: int, base: int, expected: int) -> None:
    """
    Test.
    """
    assert int_to_base(n, base) == expected
