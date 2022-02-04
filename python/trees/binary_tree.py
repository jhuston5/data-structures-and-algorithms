try:
    from trees.node import Node

except:
    from node import Node


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def pre_order(self):
        # root > left > right
        tree_val = []

        def walk(root):
            if root is None:
                return
            tree_val.append(root.value)
            walk(root.left)
            walk(root.right)

        walk(self.root)
        return tree_val

    def in_order(self):
        # left > root > right
        tree_val = []

        def walk(root):
            if root is None:
                return
            walk(root.left)
            tree_val.append(root.value)
            walk(root.right)

        walk(self.root)
        return tree_val

    def post_order(self):
        # left > right > root
        tree_val = []

        def walk(root):
            if root is None:
                return
            walk(root.left)
            walk(root.right)
            tree_val.append(root.value)

        walk(self.root)
        return tree_val

    def add(self, value):
        node = Node(value)

        if self.is_empty():
            self.root = node

    def max_val(self):
        maximum = 0

        def walk(root):
            nonlocal maximum
            print(maximum)
            if root is None:
                return
            maximum = max(root.value, maximum)
            walk(root.left)
            walk(root.right)

        walk(self.root)
        return maximum

    def is_empty(self):
        try:
            self.root.value
            return False
        except:
            return True


class BinarySearchTree(BinaryTree):
    def add(self, value):
        def walk(root):
            if self.root is None:
                self.root = Node(value)
                return

            if value > root.value:
                if root.right is None:
                    root.right = Node(value)
                else:
                    walk(root.right)
            if value < root.value:
                if root.left is None:
                    root.left = Node(value)
                else:
                    walk(root.left)

        walk(self.root)

    def contains(self, value):
        def walk(root):
            if root is None:
                return False

            if root.value == value:
                return True

            elif root.value < value:
                return walk(root.right)

            elif root.value > value:
                return walk(root.left)

            else:
                return False

        return walk(self.root)
