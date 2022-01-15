from stack_queue.node import Node


class Stack:
    """
    Create a Stack Class
    """

    def __init__(self, top=None):
        self.top = top

    # adds a new node with that value to the top of the stack with an O(1) Time performance.
    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    # Removes the node from the top of the stack
    def pop(self):
        if self.isEmpty() == True:
            raise Exception("Error - This Stack is Empty")
        temp = self.top
        self.top = self.top.next
        temp.next = None
        return temp.value

    def peek(self):
        if self.top == None:
            raise Exception("Error - This Stack is Empty")
        return self.top.value

    def isEmpty(self):
        if self.top == None:
            return True
        else:
            return False


if __name__ == "__main__":
    stack = Stack()
    stack2 = Stack()
    stack.push("Dalinar")
    stack.push("Shallan")
    stack.push("Jasnah")
    stack.push("Kaladin")
    stack.push("Adolin")
    stack.pop()
    stack.peek()
    stack.isEmpty()
    stack2.isEmpty()
    # stack2.pop()
