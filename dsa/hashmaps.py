"""
Implementation of a HashMap.
"""

from typing import Any


class HashMap:
    """
    Class definition of a HashMap.
    """

    def __init__(self, size: int) -> None:
        """
        Initialize the list to store the values.
        """
        self.hashmap = [None for i in range(size)]

    def key_to_index(self, key: str) -> int:
        """
        Hashable function that maps a key to an integer.
        This integer is the index of the spot of the value.
        Time Complexity: O(k) k is the length of the key
        Space Complexity: O(1)
        """
        # add the Unicode values of the characters of key
        # Mod (%) the sum of the Unicode values by the size of the hashmap
        # so that the index will always be between 0 and the length of the hashmap
        # s: int = 0
        # for c in key:
        #     s += ord(c)
        s: int = sum(ord(c) for c in key)
        index: int = s % len(self.hashmap)
        return index

    def insert(self, key: str, value: Any) -> None:
        """
        Insert a value in the hashmap.
        """
        index: int = self.key_to_index(key)
        self.hashmap[index] = (key, value)

    def get(self, key) -> Any:
        """
        Get a value from the hashmap.
        """
        index: int = self.key_to_index(key)
        tup: tuple[str, Any] = self.hashmap[index]
        if tup is None:
            raise Exception("sorry, key not found")
        return tup[1]

    def __repr__(self):
        """
        String representation.
        """
        buckets = []
        for v in self.hashmap:
            if v is not None:
                buckets.append(v)
        return str(buckets)
