# DON'T MODIFY THIS FILE

from copy import deepcopy
import pytest

from implementation import TreeImplementation as Tree


@pytest.fixture
def tree_fixture():
    return Tree(5, Tree(3, Tree(2), Tree(4)), Tree(8, Tree(7), Tree(9)))


def test_tree_init():
    tree = Tree(1)
    assert tree.value == 1
    assert tree.left is None
    assert tree.right is None


@pytest.mark.parametrize("value", [5, 2, 8, 4, 7])
def test_tree_insert_existing_value(tree_fixture, value):
    original = deepcopy(tree_fixture)
    tree_fixture.insert(value)
    assert original == tree_fixture


@pytest.mark.parametrize(
    "value,expected", [(4, Tree(5, Tree(4))), (6, Tree(5, right=Tree(6)))]
)
def test_tree_insert_leaf(value, expected):
    tree = Tree(5)
    tree.insert(value)
    assert tree == expected


@pytest.mark.parametrize(
    "tree, value, expected",
    [
        (Tree(5, Tree(3)), 4, Tree(5, Tree(3, right=Tree(4)))),
        (Tree(5, right=Tree(7)), 6, Tree(5, right=Tree(7, Tree(6)))),
    ],
)
def test_tree_insert_multiple_layers(tree, value, expected):
    tree.insert(value)
    assert tree == expected


@pytest.mark.parametrize("value", [5, 2, 8, 4, 7])
def test_tree_contains_existing_value(tree_fixture, value):
    assert tree_fixture.contains(value)


@pytest.mark.parametrize("value", [0, 6, 10])
def test_tree_doesnt_contain_value(tree_fixture, value):
    assert not tree_fixture.contains(value)


@pytest.mark.parametrize(
    "tree, value, expected",
    [(Tree(5, Tree(4)), 4, Tree(5)), (Tree(5, right=Tree(6)), 6, Tree(5))],
)
def test_tree_remove_leaf(tree, value, expected):
    tree.remove(value)
    assert tree == expected


def test_tree_remove_root(tree_fixture):
    tree_fixture.remove(5)
    assert tree_fixture == Tree(7, Tree(3, Tree(2), Tree(4)), Tree(8, right=Tree(9)))


def test_tree_remove_only_element_exception():
    with pytest.raises(ValueError):
        Tree(5).remove(5)


def test_tree_remove_nonexistent_element_exception(tree_fixture):
    with pytest.raises(KeyError):
        tree_fixture.remove(6)


def test_tree_min_value(tree_fixture):
    assert tree_fixture.min_value() == 2


def test_tree_max_value(tree_fixture):
    assert tree_fixture.max_value() == 9


def test_tree_inorder_traversal(tree_fixture):
    assert tree_fixture.inorder_traversal() == [2, 3, 4, 5, 7, 8, 9]
