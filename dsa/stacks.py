"""
Implementation of a Stack.
"""


class Stack:
    """
    Class definition of a Stack.
    Last In First Out (LIFO) data structure.
    """

    def __init__(self) -> None:
        """
        Initialisation with an empty list.
        """
        self.items = []

    def is_empty(self) -> bool:
        """
        Return True is the Stack is empty, otherwise False.
        Time Complexity: O(1)
        """
        return len(self.items) == 0

    def push(self, item: int) -> None:
        """
        Push an item to the Stack.
        Time Complexity: O(1)
        """
        self.items.append(item)

    def pop(self) -> int:
        """
        Remove and return the top item of the Stack.
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Pop from an empty stack.")
        return self.items.pop()

    def peek(self) -> int:
        """
        Return the top item without removing it from the Stack.
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Peek from an empty stack.")
        return self.items[-1]

    def size(self) -> int:
        """
        Get the size/length of the Stack.
        Time Complexity: O(1)
        """
        return len(self.items)

    def __repr__(self) -> str:
        """
        Return a string representation of the Stack.
        Time Complexity: O(1)
        """
        return f"Stack(bottom → top): {self.items}"
