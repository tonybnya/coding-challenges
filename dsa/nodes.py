"""
Implementation of a Node.
"""


class Node:
    """
    Class definition of a Node.
    """

    def __init__(self, val: int | str | None) -> None:
        """
        Initialisation of a Node.
        """
        self.val = val
        self.next = None

    def set_next(self, node: "Node"):
        """
        Set the next node to the given node
        """
        self.next = node

    def __repr__(self) -> str:
        """
        Return the string representation of a Node.
        Time Complexity: O(1)
        """
        return f"[{self.val}]"
