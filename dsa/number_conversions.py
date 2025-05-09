"""
Set of functions to convert numbers.
"""


def binary_to_int(binary_str: str) -> int:
    """
    Convert binary string to integer (e.g., '1011' -> 11)
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    n: int = len(binary_str)
    power: int = n - 1
    integer: int = 0
    i: int = 0
    while i < n:
        integer += int(binary_str[i]) * 2**power
        power -= 1
        i += 1
    return integer


def int_to_binary(n: int) -> str:
    """
    Convert integer to binary string (e.g., 11 -> '1011')
    Time Complexity: O(logn)
    Space Complexity: O(logn)
    """
    if n == 0:
        return "0"
    binary_str: str = ""
    while n > 0:
        quotient, remainder = divmod(n, 2)
        binary_str += str(remainder)
        n = quotient
    return binary_str[::-1]


def hex_to_int(hex_str: str) -> int:
    """
    Convert hex string to integer (e.g., '1A' -> 26)
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    hex_values: dict[str, int] = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "A": 10,
        "B": 11,
        "C": 12,
        "D": 13,
        "E": 14,
        "F": 15,
    }
    n: int = len(hex_str)
    power: int = n - 1
    integer: int = 0
    i: int = 0
    while i < n:
        # Convert to uppercase to handle both upper and lowercase letters
        c: str = hex_str[i].upper()
        value: int | None = hex_values.get(c)
        integer += value * 16**power
        power -= 1
        i += 1
    return integer


def int_to_hex(n: int) -> str:
    """
    Convert integer to hex string (e.g., 26 -> '1A')
    Time Complexity: O(logn)
    Space Complexity: O(logn)
    """
    hex_values: dict[str, int] = {
        0: "0",
        1: "1",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "A",
        11: "B",
        12: "C",
        13: "D",
        14: "E",
        15: "F",
    }
    if n == 0:
        return "0"
    hex_str: str = ""
    while n > 0:
        quotient, remainder = divmod(n, 16)
        hex_str += hex_values.get(remainder)
        n = quotient
    return hex_str[::-1]


def octal_to_int(octal_str: str) -> int:
    """
    Convert octal string to integer (e.g., '17' -> 15)
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    n: int = len(octal_str)
    power: int = n - 1
    integer: int = 0
    i: int = 0
    while i < n:
        c: str = octal_str[i]
        value: int = int(c) * 8**power
        integer += value
        power -= 1
        i += 1
    return integer


def int_to_octal(n: int) -> str:
    """
    Convert integer to octal string (e.g., 15 -> '17')
    Time Complexity: O(logn)
    Space Complexity: O(logn)
    """
    if n == 0:
        return "0"
    octal_str: str = ""
    while n > 0:
        quotient, remainder = divmod(n, 8)
        octal_str += str(remainder)
        n = quotient
    return octal_str[::-1]


def base_to_int(number_str: str, base: int) -> int:
    """
    Convert string from base-N to integer (e.g., '1A', 16 -> 26)
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    match base:
        case 2:
            return binary_to_int(number_str)
        case 8:
            return octal_to_int(number_str)
        case 10:
            return int(number_str)
        case 16:
            return hex_to_int(number_str)
        case _:
            return -1


def int_to_base(n: int, base: int) -> int | str:
    """
    Convert integer to base-N string (e.g., 26, 16 -> '1A')
    Time Complexity: O(logn)
    Space Complexity: O(logn)
    """
    if n == 0:
        return "0"
    digits = "0123456789ABCDEF"
    result = ""
    if base not in (2, 8, 10, 16):
        return -1
    while n > 0:
        n, remainder = divmod(n, base)
        result += digits[remainder]
    return result[::-1]
