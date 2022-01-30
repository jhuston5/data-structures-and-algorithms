from audioop import add


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

        # if root is not None:
        #     tree_val.append(root)
        #     tree_val = tree_val + self.pre_order(root.left)
        #     tree_val = tree_val + self.pre_order(root.right)
        # return tree_val

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


class BinarySearchTree(BinaryTree):
    # def __init__(self, root=None):
    #     self.root = root

    def add(self, value):
        def walk(root, value):
            print(root.value)
            if not root.left:
                root.left = Node(value)
            else:
                walk(root.left, value)
            if not root.right:
                root.right = Node(value)
            else:
                walk(root.right, value)

        walk(self.root, value)

    # Had help from Bionca here
    def contains(self, node, value):
        if node:
            if node.value == value:
                return True
            if node.value > value:
                return self.contains(node.left, value)
            if node.value < value:
                return self.contains(node.right, value)
        else:
            return False

    # def add(self, root, value):
    #     # Check if the value is greater than the root
    #     # If the root is None,
    #     if root is None:
    #         root = Node(value)
    #         return root
    #     else:
    #         if root.value == value:
    #             return root
    #         elif root.value < value:
    #             root.right = add(root.right, value)
    #         else:
    #             root.left = add(root.left, value)
    #     return root


# Notes
