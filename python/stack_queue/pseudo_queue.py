try:
    from stack_queue.stack import Stack

except:
    from stack import Stack


class PseudoQueue:
    # Create a Pseudo Queue class using two stacks to mimic Queue functionality
    pass

    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, value):
        # Handle if there are no initial values in the stack
        if self.stack2.top == None:
            self.stack2.push(value)
            print(f"When no Stack2 val: {self.stack2.top.value}")

        else:
            # Iterate over the second stack to push stored values to the first temporary stack
            status = True
            while status == True:
                if self.stack2.top == None:
                    status = False
                else:
                    temp = self.stack2.pop()
                    self.stack1.push(temp)
                    print(f"Temp: {temp}")
            # Push the new value onto the top of the temporary stack
            self.stack1.push(value)

            # Iterate over first temporary stack, popping and pushing back onto the storage stack
            status = True
            while status == True:
                if self.stack1.top == None:
                    status = False
                else:
                    temp = self.stack1.pop()
                    self.stack2.push(temp)
                    print(f"Temp2: {temp}")

        print(f"Final Stack2 Top: {self.stack2.top.value}")

    def dequeue(self):
        # print(f"Dequeued Value: {self.stack2.pop()}")
        print(f"DQ Stack 2 Top Value: {self.stack2.top.value}")
        return self.stack2.pop()


# if __name__ == "__main__":
#     pseudo = PseudoQueue()
#     pseudo.enqueue("Windrunner")
#     pseudo.enqueue("Lightweaver")
#     pseudo.enqueue("Skybreaker")
#     pseudo.enqueue("Edgedancer")

#     pseudo.dequeue()
#     peek_value = pseudo.stack2.peek()
#     print(peek_value)
