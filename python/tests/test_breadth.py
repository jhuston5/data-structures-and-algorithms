from trees.breadth import breadthFirst
from stack_queue.queue import Queue
from trees.binary_tree import BinaryTree
from trees.binary_tree import BinarySearchTree
from trees.node import Node

import pytest


# def test_version():
#     assert __version__ == '0.1.0'


def test_breadth_single_val():
    bt = BinaryTree()
    bt.add("apple")
    expected = breadthFirst(bt)
    assert expected == ["apple"]


def test_breadth_multiple_val():
    apple = Node("apple")
    pear = Node("pear")
    orange = Node("orange")

    bt = BinaryTree(apple)
    apple.left = pear
    apple.right = orange
    expected = breadthFirst(bt)
    assert expected == ["apple", "pear", "orange"]


def test_bst():
    bt = BinarySearchTree()
    bt.add(100)
    bt.add(50)
    bt.add(200)
    bt.add(75)

    expected = breadthFirst(bt)
    assert expected == [100, 50, 200, 75]
