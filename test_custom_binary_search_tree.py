import pytest

from custom_binary_search_tree import BST


@pytest.fixture
def tree() -> BST:
    tree = BST()
    tree.insert(2)
    tree.insert(3)
    tree.insert(9)
    tree.insert(6)
    return tree


def test_insert():
    """inserts a number into the tree"""
    tree = BST()
    assert tree.search(4) == False
    tree.insert(4)
    assert tree.search(4)
    assert tree.root is not None, "root not none"
    assert tree.root.value == 4, "root should = 4"


def test_search(tree: BST):
    """returns whether or not a value is in the tree"""
    assert tree.root is not None, "root should not be none after insertion"
    assert tree.root.value == 2, "root value should be the first inserted node"
    assert tree.search(4) == False
    assert tree.search(2) == True
    assert tree.search(3) == True
    assert tree.search(9) == True
    assert tree.search(6) == True
    assert tree.search(0) == False


def test_in_order_traversal(tree: BST):
    """returns a list of all the values in sorted order"""
    expected = [2, 3, 6, 9]
    actual = tree.in_order_traversal()
    assert expected == actual
 
 
def test_find_min(tree: BST):
    """returns the smallest number in the tree(you cannot turn the tree into a list then return an element from the list, you must do it by traversing the tree)"""
    expected = 2
    actual = tree.find_min()
    assert expected == actual
 

def test_find_max(tree: BST):
    """returns the largest number in the tree(you cannot turn the tree into a list then return an element from the list, you must do it by traversing the tree)"""
    expected = 9
    actual = tree.find_max()
    assert expected == actual


def test_height(tree: BST):
    """returns the depth of the tree(how far is the furthest node from the root node?)"""
    pass


def test_count_leaves(tree: BST):
    """returns the number of leaf nodes in the tree(leaf nodes are nodes without any children)"""
    pass


def test_serialize(tree: BST):
    """turn the BST into a string"""
    pass


def test_deserialize(tree: BST):
    """deserialize a serialized BST(take a string version of a BST and make an empty BST filled with those values). The new tree should match the tree that was serialized."""
    pass
