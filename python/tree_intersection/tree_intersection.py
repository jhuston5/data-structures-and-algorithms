from hashtable.hashtable import Hashtable
from trees.binary_tree import BinaryTree
from trees.node import Node


def tree_intersection(tree1, tree2):
    intersection_list = []
    hashed_values = Hashtable()
    t1 = BinaryTree.pre_order(tree1)
    for i in t1:
        hashed_values.add(i, "0")

    t2 = BinaryTree.pre_order(tree2)
    for i in t2:
        if hashed_values.contains(i):
            intersection_list.append(i)

    print(intersection_list)
    return intersection_list


if __name__ == "__main__":
    a = Node(150)
    b = Node(100)
    c = Node(250)

    bt1 = BinaryTree(a)
    a.left = b
    a.right = c

    d = Node(42)
    e = Node(100)
    f = Node(600)

    bt2 = BinaryTree(d)
    d.left = e
    d.right = f

    tree_intersection(bt1, bt2)
