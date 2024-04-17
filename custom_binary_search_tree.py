# Implement a BST. It should include these methods:
class BST():
    def __init__():
        pass

    def insert(self, int) -> None:
        """inserts a number into the tree"""

        pass

    def search(self, int) -> bool:
        """returns whether or not a value is in the tree"""
        pass

    def in_order_traversal(self) -> list[int]:
        """returns a list of all the values in sorted order"""
        pass

    def find_min(self) -> int:
        """returns the smallest number in the tree(you cannot turn the tree into a list then return an element from the list, you must do it by traversing the tree)"""
        pass

    def find_max(self) -> int:
        """returns the largest number in the tree(you cannot turn the tree into a list then return an element from the list, you must do it by traversing the tree)"""
        pass

    def height(self) -> int:
        """returns the depth of the tree(how far is the furthest node from the root node?)"""
        pass

    def count_leaves(self) -> int:
        """returns the number of leaf nodes in the tree(leaf nodes are nodes without any children)"""
        pass

    def serialize(self) -> str:
        """turn the BST into a string"""
        pass

    def deserialize(self, tree: str) -> None:
        """deserialize a serialized BST(take a string version of a BST and make an empty BST filled with those values). The new tree should match the tree that was serialized."""
        pass
