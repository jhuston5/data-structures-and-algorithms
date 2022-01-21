from doctest import FAIL_FAST


try:
    from stack_queue.queue import Queue
    from stack_queue.stack import Stack
    from stack_queue.node import Node

except:
    from queue import Queue
    from stack import Stack
    from node import Node


class AnimalShelter:
    def __init__(self):
        self.queue = Queue()
        self.stack = Stack()
        self.animal = ""
        self.initialized = False

    def enqueue(self, animal):
        node = Node(animal)
        if self.queue.isEmpty() == True:
            self.queue.front = node
            self.queue.rear = node

        else:
            self.queue.rear.next = node
            self.queue.rear = node

    def dequeue(self, pref):
        status = True
        while status == True:
            if pref == self.queue.front.value:
                self.animal = self.queue.front.value

                status = False
            else:
                temp = self.queue.front
                # print(temp.value)
                self.stack.push(self.queue.front)
                self.queue.front = self.queue.front.next
                print(self.queue.front.value)

        while self.stack.top is not None:
            temp = self.queue.front
            self.queue.front = self.stack.pop()
            self.queue.front.next = temp
            print(
                f"New Front: {self.queue.front.value}, new front next: {self.queue.front.next.value}"
            )

        print(f"First matching animal: {self.animal}")
        return self.animal


if __name__ == "__main__":
    test_shelter = AnimalShelter()
    test_shelter.enqueue("cat")

    test_shelter.enqueue("cat")
    test_shelter.enqueue("dog")
    test_shelter.enqueue("cat")
    test_shelter.enqueue("cat")

    test_shelter.dequeue("dog")
    # print(f"Test Pointer: {test_shelter.pointer}")
    # print(f"Final Rear: {test_shelter.queue1.rear.value}")

    # if self.queue1.rear == None and self.queue2.rear == None:
    #     self.queue1.front = node
    #     self.queue1.rear = node
    #     self.pointer = 1
    #     print(f"Pointer: {self.queue1.front.value} {self.queue1.rear.value}")
    # else:
    #     self.initialized = True

    # if self.pointer == 1 and self.initialized == True:
    #     print(f"Q1 Check: {node.value}")

    #     self.queue1.rear.next = self.queue1.rear.value
    #     print(f"Rear.next: {self.queue1.rear.value}")
    #     self.queue1.rear = node
    #     print(f"Rear: {self.queue1.rear.value} Rear.next: {self.queue1.rear.next}")

    # elif self.pointer == 2:
    #     self.queue2.rear.next = node
    #     self.queue2.rear = node
