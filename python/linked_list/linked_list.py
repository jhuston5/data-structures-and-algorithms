# Exception Error Handler
def handle_exceptions(method):
    def wrapper(*args, **kwargs):
        try:
            method(*args, **kwargs)
        except TypeError:
            print(f"You received an error on {method.__name__} method.")

    return wrapper


class Node:
    """
    Create a Node Class
    """

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    """
    Create a Linked List Class
    """

    def __init__(self, head=None, next=None, tail=None):
        # initialization here
        self.head = head
        self.next = next

    # Insert a new Node into the LinkedList
    @handle_exceptions
    def insert(self, value):
        # method body here
        new_node = Node(value)
        if self.head is not None:
            new_node.next = self.head
        self.head = new_node

    # Check if a value exists in the Linked List and return a Boolean
    def includes(self, included_value):
        # Return if the value exists as a Node value in the linked list (Boolean). Utilize a while loop to traverse the LL?
        current = self.head
        while current:
            if current.value == included_value:
                return True
            current = current.next

        return False

    # Find all values in the Linked List and print them in a string
    def to_string(self):
        current = self.head
        output_string = ""
        while current is not None:
            output_string += f"{current.value} -> "
            current = current.next
        else:
            output_string += "NULL"
        return output_string

    # Add a new Node to the end (Tail) of the LinkedList
    def append(self, end_value):
        new_end_node = Node(end_value)
        current = self.head
        while current:
            if current.next == None:
                current.next = new_end_node
                break
            current = current.next

    # Adds a new Node and value right BEFORE the Node specified
    def insert_before(self, old_value, new_value):
        new_node = Node(new_value)
        current = self.head
        # new_next = current.next
        """if current.next == None:
            print(f"Current Value= {current.value}")
            print(f"NewNode.next = {new_node.next}")
            print(f"NewNode= {new_node.value}")
            new_node.next = current.value
            current.next = current.value
            current.value = new_node.value

            print(f"current.value= {current.value}")
        print(f"current.next= {current.next}")
        print(f"newnode.value= {new_node.value}")
        print(f"newnode.next= {new_node.next}")
        print(f"current= {current.value}")"""

        while current.next is not None:
            new_next = current.next
            print(f"New Next.value = {new_next.value}")
            if new_next.value == old_value:
                new_node.next = current.next
                current.next = new_node
                break
            current = current.next

    # Adds a new Node and value right AFTER the Node specified
    def insert_after(self, old_value, new_value):
        new_node = Node(new_value)
        current = self.head
        while current is not None:
            if current.value == old_value:
                new_node.next = current.next
                current.next = new_node
            current = current.next


if __name__ == "__main__":

    test = LinkedList()
    test2 = LinkedList()

    """test.insert("pear")
    test.insert("raspberry")
    test.insert("kiwi")
    test.insert("apple")
    test.append("pineapple")
    test.append("blueberry")
    test.insert_after("kiwi", "peach")
    test.insert_before("pear", "papaya")

    print(test.includes("kiwi"))
    print(test.includes("apricot"))
    # test_output = test.to_string()
    print(f"Head: {test.head.value}")
    print(f"All Nodes: {test.to_string()}")
"""
    test2.insert("apple")
    test2.insert_before("apple", "peach")
    print(f"Head test 2: {test2.head.value}")
    print(f"All Nodes Test 2: {test2.to_string()}")

    # Test error handling
    test.insert()

# print(test_output)


"""
if __name__ == '__main__':
    ll = LinkedList()
    ll.insert(5)
    ll.insert(7)
    ll.insert(6)
    ll.insert(3)
    ll.__str__()"""
