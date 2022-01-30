from trees.binary_tree import BinarySearchTree
from trees.binary_tree import BinaryTree
from trees.node import Node

import pytest


# def test_version():
#     assert __version__ == '0.1.0'


def test_new_node():
    node = Node(11)
    actual = node.value
    expected = 11
    assert actual == expected


def test_new_node_bad():
    node = Node(11)
    actual = node.value
    expected = 12
    assert actual != expected


def test_bt_empty():
    bt = BinaryTree()
    assert bt


def test_bt_empty_root_none():
    bt = BinaryTree()
    assert bt.root == None


# Pre Order Test
def test_bt_left_right():

    #           apple
    #       /           \
    #   pear          orange

    apple = Node("apple")
    pear = Node("pear")
    orange = Node("orange")

    bt = BinaryTree(apple)
    apple.left = pear
    apple.right = orange

    assert apple.left == bt.root.left
    assert apple.right == orange
    order_list = bt.pre_order()
    assert order_list == ["apple", "pear", "orange"]


# In Order Test
def test_bt_left_root_right():

    #           apple
    #       /           \
    #   pear          orange

    apple = Node("apple")
    pear = Node("pear")
    orange = Node("orange")

    bt = BinaryTree(apple)
    apple.left = pear
    apple.right = orange

    assert apple.left == bt.root.left
    assert apple.right == orange
    order_list = bt.in_order()
    assert order_list == ["pear", "apple", "orange"]


# Post Order Test
def test_bt_left_right_root():

    #           apple
    #       /           \
    #   pear          orange

    apple = Node("apple")
    pear = Node("pear")
    orange = Node("orange")

    bt = BinaryTree(apple)
    apple.left = pear
    apple.right = orange

    assert apple.left == bt.root.left
    assert apple.right == orange
    order_list = bt.post_order()
    assert order_list == ["pear", "orange", "apple"]


# Add method
def test_add():
    mid = Node(100)
    l = Node(50)
    r = Node(200)

    bt = BinaryTree(mid)
    mid.left = l
    mid.right = r

    bst = BinarySearchTree(bt)
    bst.add(25)
    expected = 25
    assert bst.root.left == expected


# Contain Method
def test_bt_left_right_root():

    #           apple
    #       /           \
    #   pear          orange

    apple = Node("apple")
    pear = Node("pear")
    orange = Node("orange")

    bt = BinaryTree(apple)
    bst = BinarySearchTree(bt)
    apple.left = pear
    apple.right = orange

    expected = True
    assert expected == bst.contains(bst.root, "apple")
