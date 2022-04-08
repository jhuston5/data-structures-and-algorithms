try:
    from stack_queue.node import Node

except:
    from node import Node


class Queue:
    """
    Create a Queue Class
    """

    def __init__(self, rear=None, front=None):
        self.front = front
        self.rear = rear

    # adds a new node with that value to the back of the queue with an O(1) Time performance.
    def enqueue(self, value):
        node = Node(value)
        if self.isEmpty() == True:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    # Removes the node from the front of the queue
    def dequeue(self):
        temp = self.front
        self.front = self.front.next
        temp.next = None
        return temp.value

    def peek(self):
        if self.front == None:
            raise Exception("Error - This is an Empty Queue")
        return self.front.value

    def isEmpty(self):
        if self.front == None:
            return True
        else:
            return False


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue("Wax")
    queue.enqueue("Wayne")
    queue.enqueue("Sanderson")
    queue.dequeue()
    queue.peek()
