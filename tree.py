# DON'T MODIFY THIS FILE

from abc import ABC, abstractmethod
from typing import Optional


class Tree(ABC):
    def __init__(
        self, value: int, left: Optional["Tree"] = None, right: Optional["Tree"] = None
    ) -> None:
        """
        Create a leaf node with the given value.
        """
        self.value = value
        self.left = left
        self.right = right

    @abstractmethod
    def insert(self, value: int) -> None:
        """
        Insert a value into the tree. Does nothing if the value is already in
        the tree.
        """
        pass

    @abstractmethod
    def contains(self, value: int) -> bool:
        """
        Check if the tree contains a value.
        """
        pass

    @abstractmethod
    def remove(self, value: int) -> None:
        """
        Remove a value from the tree. Raises a KeyError if the value is not
        in the tree, or a ValueError if the removal would result in an empty
        tree.
        """
        pass

    @abstractmethod
    def min_value(self) -> int:
        """
        Return the minimum value in the tree.
        """
        pass

    @abstractmethod
    def max_value(self) -> int:
        """
        Return the maximum value in the tree.
        """
        pass

    @abstractmethod
    def inorder_traversal(self) -> list[int]:
        """
        Return the inorder traversal (left, root, right) of the tree as a list.
        """
        pass

    def __eq__(self, other: object) -> bool:
        """
        Check if two trees are equal.
        """
        if not isinstance(other, Tree):
            return NotImplemented

        return (
            self.value == other.value
            and self.left == other.left
            and self.right == other.right
        )
