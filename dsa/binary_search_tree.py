"""
Implementation of a Binary Search Tree.
"""


class BSTNode:
    """
    Class definition of a Binary Search Tree (BST).
    """

    def __init__(self, val: int | str | None = None) -> None:
        """
        Initialisation.
        """
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val: int | str | None) -> None:
        """
        Insert a value in a BST.
        Time Complexity: O(logn)
        Space Complexity: O(logn) due to recursion stack
        """
        if self.val is None:
            self.val = val
            return
        if self.val == val:
            return
        if val < self.val:
            if self.left is None:
                self.left = BSTNode(val)
                return
            self.left.insert(val)
            return
        if val > self.val:
            self.right = BSTNode(val)
            return
        self.right.insert(val)
        return

    def get_min(self) -> int | str:
        """
        Get the minimum value in the BST.
        The minimum value in the BST is located in the leftmost node.
        Time Complexity: O(h)
        Space Complexity: O(1)
        """
        # Recursive approach uses O(h) TC and O(h) SC due to recursion stack
        # if self.left is None:
        #     return self.val
        # return self.left.get_min()
        temp: BSTNode = self
        while temp.left is not None:
            temp = temp.left
        return temp.val

    def get_max(self) -> int | str:
        """
        Get the maximum value in the BST.
        The maximum value in the BST is located in the rightmost node.
        Time Complexity: O(h)
        Space Complexity: O(1)
        """
        # Recursive approach uses O(h) TC and O(h) SC due to recursion stack
        # if self.right is None:
        #     return self.val
        # return self.right.get_max()
        temp: BSTNode = self
        while temp.right is not None:
            temp = temp.right
        return temp.val

    def delete(self, val: int | str | None) -> None:
        """
        Delete a node containing val in the BST.
        Time Complexity: O(logn)
        Space Complexity: O(h)
        """
        if self.val is None:
            return
        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)
            return self
        if val > self.val:
            if self.right:
                self.right = self.right.delete(val)
            return self
        if not self.left:
            return self.right
        if not self.right:
            return self.left
        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.val = min_larger_node.val
        self.right = self.right.delete(min_larger_node.val)
        return self

    def search(self, val: int | str | None) -> bool:
        """
        Search for a value in the BST.
        Time Complexity: O(n)
        Space Complexity: O(h)
        """
        if self.val == val:
            return True
        if val < self.val and self.left:
            return self.left.search(val)
        if val > self.val and self.right:
            return self.right.search(val)
        return False

    def preorder(self) -> list[int | str | None]:
        """
        Pre-order traversal of the BST.
        Time Complexity: O(n)
        Space Complexity: O(h)
        """
        visited: list[int | str | None] = [self.val]
        if self.left:
            visted += self.left.preorder()
        if self.right:
            visited += self.right.preorder()
        return visited

    def postorder(self) -> list[int | str | None]:
        """
        Post-order traversal of the BST.
        Time Complexity: O(n)
        Space Complexity: O(h)
        """
        visited: list[int | str | None] = []
        if self.left:
            visted += self.left.postorder()
        if self.right:
            visited += self.right.postorder()
        visited.append(self.val)
        return visited

    def inorder(self) -> list[int | str | None]:
        """
        In-order traversal of the BST.
        Time Complexity: O(n)
        Space Complexity: O(h)
        """
        visited: list[int | str | None] = []
        if self.left:
            visted += self.left.inorder()
        visited.append(self.val)
        if self.right:
            visited += self.right.inorder()
        return visited

    def get_height(self) -> int:
        """
        Return the height (max depth) of the BST.
        Time Complexity: O(n)
        Space Complexity: O(h)
        """
        left_height = self.left.get_height() if self.left else 0
        right_height = self.right.get_height() if self.right else 0
        return 1 + max(left_height, right_height)
