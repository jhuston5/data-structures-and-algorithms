from hashtable.hashtable import Hashtable
from trees.binary_tree import BinaryTree
from trees.node import Node
from tree_intersection.tree_intersection import tree_intersection


def test_intersection():
    a = Node("150")
    b = Node("100")
    c = Node("250")

    bt1 = BinaryTree(a)
    a.left = b
    a.right = c

    d = Node("42")
    e = Node("100")
    f = Node("600")

    bt2 = BinaryTree(d)
    d.left = e
    d.right = f

    expected = tree_intersection(bt1, bt2)
    actual = ["100"]
    assert actual == expected
