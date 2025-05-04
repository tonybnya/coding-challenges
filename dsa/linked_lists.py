"""
Implementation of a Linked List.
"""

from typing import Iterator

from nodes import Node


class LinkedList:
    """
    Class definition of a Linked List.
    head node -> node -> node -> node -> tail node
    """

    def __init__(self) -> None:
        """
        Initialisation of a Linked List.
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self.head: Node | None = None

    def __iter__(self) -> Iterator[Node]:
        """
        Make the Linked List iterable.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        temp: Node | None = self.head
        while temp is not None:
            yield temp
            temp = temp.next

    def add_to_tail(self, node: Node) -> None:
        """
        Add a node to the tail of the Linked List.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if self.head is None:
            self.head = node
            return

        # temp: Node = self.head
        # while temp.next:
        #     temp = temp.next
        # temp.next = node
        last_node: Node | None = None
        for n in self:
            last_node = n
        last_node.next = node

    def add_to_head(self, node: Node) -> None:
        """
        Add a node to the head of the Linked List.
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        node.next = self.head
        self.head = node

    def add_to_middle(self, i: int, node: Node) -> None:
        """
        Add a node to the ith index
        Time Complexity: O(n) (traverse up to ith node, so O(i) ?)
        Space Complexity: O(1)
        """
        if self.head is None:
            self.add_to_head(node)
            return

        dummy: Node | None = None
        temp: Node | None = self.head
        index: int = 0
        while temp and index < i:
            dummy = temp
            temp = temp.next
            index += 1

        node.next = temp
        dummy.next = node

    def remove_to_tail(self) -> Node:
        """
        Remove a node to the tail of the Linked List.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if self.head is None:
            return None

        if self.head.next is None:
            removed: Node | None = self.head
            self.head = None
            return removed

        dummy: Node | None = None
        temp: Node | None = self.head
        while temp.next:
            dummy = temp
            temp = temp.next

        dummy.next = None

        return temp

    def remove_to_head(self) -> Node | None:
        """
        Remove a node to the head of the Linked List.
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if self.head is None:
            return None

        removed: Node = self.head
        self.head = self.head.next
        removed.next = None

        return removed

    def remove_to_middle(self, i: int) -> Node | None:
        """
        Remove the ith node of the Linked List.
        Time Complexity: O(n) (traverse up to ith node, so O(i)?)
        Space Complexity: O(1)
        """
        if self.head is None:
            return None

        if i == 0:
            return self.remove_to_head()

        dummy: Node | None = None
        temp: Node | None = self.head
        index: int = 0
        while temp and index < i:
            dummy = temp
            temp = temp.next
            index += 1

        dummy.next = temp.next
        temp.next = None

        return temp

    def __repr__(self) -> str:
        """
        Return the string representation of a Node.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        nodes = []
        current = self.head
        while current and hasattr(current, "val"):
            nodes.append(current.val)
            current = current.next

        return " -> ".join(nodes)

    # def ll_to_list(self, linked_list: "LinkedList") -> list[int | str | None]:
    def ll_to_list(self) -> list[int | str | None]:
        """
        Transform a Linked List into a regular list.
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        lst: list[int | str | None] = []
        # for node in linked_list:
        for node in self:
            lst.append(node.val)
        return lst
