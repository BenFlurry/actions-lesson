from tree import Tree


class TreeImplementation(Tree):
    def insert(self, value: int) -> None:
        """
        Insert a value into the tree. Does nothing if the value is already in
        the tree.
        """
        if self.root is None:
            self.root = self.value(value)
        else:
            if value < self.root.value:
                if self.root.left is None:
                    self.root.left = self.value(value)
                else:
                    self.root.left.insert(value)
            elif value > self.root.value:
                if self.root.right is None:
                    self.root.right = self.value(value)
                else:
                    self.root.right.insert(value)
            else:
                self.root.value = value

    def contains(self, value: int) -> bool:
        """
        Check if the tree contains a value.
        """
        if value == None:
            return False
        else:
            if value == self.root.value:
                return True
            elif value < self.root.value:
                if self.root.left is None:
                    return False
                else:
                    return self.root.left.contains(value)
            elif value > self.root.value:
                if self.root.right is None:
                    return False
                else:
                    return self.root.right.contains(value)
            else:
                return False

    def remove(self, value: int) -> None:
        """
        Remove a value from the tree. Raises a KeyError if the value is not
        in the tree, or a ValueError if the removal would result in an empty
        tree.
        """
        pass

    def min_value(self) -> int:
        """
        Return the minimum value in the tree.
        """
        return 0

    def max_value(self) -> int:
        """
        Return the maximum value in the tree.
        """
        return 0

    def inorder_traversal(self) -> list[int]:
        """
        Return the inorder traversal (left, root, right) of the tree as a list.
        """
        return []
