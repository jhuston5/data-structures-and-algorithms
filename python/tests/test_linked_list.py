from linked_list.linked_list import LinkedList, Node

import pytest


def test_import():
    assert LinkedList


def test_node_instance():
    node = Node(1, None)
    assert node.next == None
    assert node.value == 1


def test_node_instance_failed():
    node = Node(1, None)
    assert node.next != node
    assert node.value != 2


def test_linked_list():
    node = Node(1, None)
    ll = LinkedList(node)
    assert ll.head == node


def test_linked_list_empty_insert():
    ll = LinkedList()
    assert ll.head == None


# Test to check if insert() function will work with an empty Linked List
def test_insert_to_empty_linked_list():
    # ll.head = apple
    ll = LinkedList()
    ll.insert("apple")
    assert ll.head.value == "apple"


# Test to check if insert() function will work with a Linked List that has a Head stored.
def test_insert_to_linked_list():
    ll = LinkedList()
    node1 = Node("apple")
    ll.head == node1
    node2 = Node("pear")
    node1.next == node2
    ll.insert("banana")
    assert ll.head.value == "banana"


# Test to check if the LinkedList includes() function works when a value is stored in a node
def test_includes_in_linked_list():
    ll = LinkedList()
    node1 = ll.insert("apple")
    ll.head == node1
    node2 = ll.insert("pear")
    test_value = ll.includes("pear")
    assert test_value == True


# Test to check if the includes() function works when a value is NOT stored in a node.
def test_not_includes_in_linked_list():
    ll = LinkedList()
    node1 = ll.insert("apple")
    ll.head == node1
    node2 = ll.insert("banana")
    test_value = ll.includes("pear")
    assert test_value == False


# Test to check if to_string function is printing the LinkedList output correctly
def test_to_string():
    ll = LinkedList()
    node1 = ll.insert("apple")
    ll.head == node1
    node2 = ll.insert("banana")
    test_output = ll.to_string()
    assert test_output == "banana -> apple -> NULL"


# Test to see if to_string will function when passed an empty Linked List
def test_to_string_empty():
    ll = LinkedList()
    test_output = ll.to_string()
    assert test_output == "NULL"


# 6-1 Test to see if one node can be appended to the end of a Linked List
def test_append():
    ll = LinkedList()
    node1 = ll.insert("apple")
    ll.head == node1
    node2 = ll.insert("banana")
    ll.append("peach")
    test_output = ll.to_string()
    assert test_output == "banana -> apple -> peach -> NULL"


# 6-2 Test to see if multiple nodes can be appended to the end of a Linked List
def test_append_multiple():
    ll = LinkedList()
    node1 = ll.insert("apple")
    ll.head == node1
    ll.append("peach")
    ll.append("pineapple")
    expected = ll.to_string()
    assert expected == "apple -> peach -> pineapple -> NULL"


# 6-3 Test if you can insert a node before a node in the middle of a Linked List
def test_insert_mid_before():
    ll = LinkedList()
    node1 = ll.insert("apple")
    ll.head == node1
    ll.insert("kiwi")
    ll.insert("blueberry")
    ll.insert_before("kiwi", "peach")
    expected = ll.to_string()
    assert expected == "blueberry -> peach -> kiwi -> apple -> NULL"


# 6-4 Test if you can insert a node before the first node of a Linked List
def test_insert_beg():
    ll = LinkedList()
    node1 = ll.insert("apple")
    ll.head == node1
    ll.insert_before("apple", "peach")
    expected = ll.to_string()
    assert expected == "peach -> apple -> NULL"


# 6-5 Test if you can insert a node after the middle node of a Linked List
def test_insert_mid_after():
    ll = LinkedList()
    node1 = ll.insert("apple")
    ll.head == node1
    ll.insert("kiwi")
    ll.insert("blueberry")
    ll.insert_after("kiwi", "peach")
    expected = ll.to_string()
    assert expected == "blueberry -> kiwi -> peach -> apple -> NULL"


# 6-6 Test if you can insert a node after the last node of a linked list
def test_insert_last_after():
    ll = LinkedList()
    node1 = ll.insert("apple")
    ll.head == node1
    ll.insert("kiwi")
    ll.insert_after("apple", "peach")
    expected = ll.to_string()
    assert expected == "kiwi -> apple -> peach -> NULL"


# 6-optional Test if you can append to an empty Linked List
def test_append_empty():
    ll = LinkedList()
    node1 = ll.append("apple")
    expected = ll.to_string()
    assert expected == "apple -> NULL"
