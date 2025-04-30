"""
023. Does Name Exist

Complete the `does_name_exist` function. It should loop over all of the
first/last name combinations in the `firstnames` and `lastnames` lists.
If it finds a combination that matches the `fullname` it should return `True`.
If the full name isn't found, it should return `False` instead.
"""


def does_name_exist(firstnames: list[str], lastnames: list[str], fullname: str) -> bool:
    """
    Solution.
    Time Complexity: O()
    Space Complexity: O()
    """
    for first in firstnames:
        for last in lastnames:
            comb: str = f"{first} {last}"
            if comb == fullname:
                return True

    return False
