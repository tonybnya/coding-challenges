"""
Implementation of a Queue.
"""


class Queue:
    """
    Class definition of a Queue.
    First In First Out (FIFO) data structure.
    """

    def __init__(self) -> None:
        """
        Initialisation with an empty list.
        """
        self.items = []

    def is_empty(self) -> bool:
        """
        Return True is the Queue is empty, otherwise False.
        Time Complexity: O(1)
        """
        return len(self.items) == 0

    def push(self, item: int | str) -> None:  # push or `enqueue`
        """
        Add an item to the tail of the Queue.
        Time Complexity: O(n)
        """
        self.items.insert(0, item)

    def pop(self) -> int | str | None:  # pop or `dequeue`
        """
        Remove and return the item to the head of the Queue.
        Time Complexity: O(1)
        """
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self) -> int | str | None:
        """
        Return the item to the head without removing it from the Queue.
        Time Complexity: O(1)
        """
        if self.is_empty():
            return None
        return self.items[-1]

    def size(self) -> int:
        """
        Get the size/length of the Queue.
        Time Complexity: O(1)
        """
        return len(self.items)

    def __repr__(self) -> str:
        """
        Return a string representation of the Queue.
        Time Complexity: O(1)
        """
        return f"Queue(tail → head): {self.items}"
