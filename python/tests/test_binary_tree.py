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


def test_bt_single_root():
    bt = BinaryTree("apple")
    assert bt.root == "apple"


# Pre Order Test
def test_bt_pre_order():

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
def test_bt_in_order():

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
def test_bt_post_order():

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


# Add Method Test
def test_add():
    bt = BinarySearchTree()
    bt.add(100)
    bt.add(50)
    bt.add(200)
    bt.add(75)

    expected = 75
    assert bt.root.left.right.value == expected


# Contain Method Test
def test_bt_():

    #           apple
    #       /           \
    #   pear          orange
    bt = BinarySearchTree()
    bt.add(100)
    bt.add(50)
    bt.add(200)
    bt.add(75)

    expected = True
    assert expected == bt.contains(100)


# For a Binary Search Tree, can successfully add a left child and right child properly to a node
def test_add_left_child():
    bt = BinarySearchTree()
    bt.add(100)
    bt.add(50)
    bt.add(200)
    bt.add(25)

    expected = 25
    assert bt.root.left.left.value == expected


def test_add_right_child():
    bt = BinarySearchTree()
    bt.add(100)
    bt.add(50)
    bt.add(200)
    bt.add(250)

    expected = 250
    assert bt.root.right.right.value == expected
