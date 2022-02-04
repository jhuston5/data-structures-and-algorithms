try:
    from trees.node import Node
    from stack_queue.queue import Queue
    from trees.binary_tree import BinaryTree


except:
    from node import Node
    from binary_tree import BinaryTree


def breadthFirst(bt):
    breadth = Queue()
    breadth.enqueue(bt.root)
    tree_breadth = []

    while breadth.isEmpty() is False:
        front = breadth.dequeue()

        tree_breadth.append(front.value)

        if front.left is not None:
            breadth.enqueue(front.left)

        if front.right is not None:
            breadth.enqueue(front.right)

    return tree_breadth
