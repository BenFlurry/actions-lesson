from tree import Tree

class TreeImplementation(Tree):
    def insert(self, value: int) -> None:
        """
        Insert a value into the tree. Does nothing if the value is already in
        the tree.
        """
        if value < self.value:
            if self.left is None:
                self.left = TreeImplementation(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = TreeImplementation(value)
            else:
                self.right.insert(value)

    def contains(self, value: int) -> bool:
        """
        Check if the tree contains a value.
        """
        if value == self.value:
            return True
        elif value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(value)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(value)

    def remove(self, value: int) -> None:
        """
        Remove a value from the tree. Raises a KeyError if the value is not
        in the tree, or a ValueError if the removal would result in an empty
        tree.
        """
        no
        pass

    def min_value(self) -> int:
        """
        Return the minimum value in the tree.
        """
        if self.left is None:
            return self.value
        else:
            return self.left.min_value()
        

    def max_value(self) -> int:
        """
        Return the maximum value in the tree.
        """
        if self.right is None:
            return self.value
        else:
            return self.right.min_value()

    def inorder_traversal(self) -> list[int]:
        """
        Return the inorder traversal (left, root, right) of the tree as a list.
        """
        if self.left is None:
            left = []
        else:
            left = self.left.inorder_traversal()

        if self.right is None:
            right = []
        else:
            right = self.right.inorder_traversal()

        return left + [self.value] + right
