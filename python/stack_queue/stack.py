from stack_queue.node import Node


# from stack_queue.node import Node


class Stack:
    def __init__(self, top=None):
        self.top = top

    # adds a new node with that value to the top of the stack with an O(1) Time performance.
    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node
        pass

    # Removes the node from the top of the stack
    def pop():
        pass
        # Should raise exception when called on empty stack
        # Returns: the value from node from the top of the stack

    def peek():
        pass
        # Returns: Value of the node located at the top of the stack
        # Should raise exception when called on empty stack

    def isEmpty():
        pass
        # Returns: Boolean indicating whether or not the stack is empty.


if __name__ == "__main__":
    stack = Stack()
    stack.push("Kaladin")
    # print_stack = LinkedList.to_string(stack)
