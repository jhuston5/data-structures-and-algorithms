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
        # Handle exception where a LinkedList is empty when appending
        new_end_node = Node(end_value)
        if self.head is None:
            self.head = new_end_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_end_node

    # Had help from Bionca finalizing
    # Adds a new Node and value right BEFORE the Node specified
    def insert_before(self, old_value, new_value):
        # Logic to handle the old value being the head
        if self.head.value == old_value:
            new_node = Node(new_value)
            new_node.next = self.head
            self.head = new_node
            # current = self.head
        # new_next = current.next
        else:
            current = self.head
            while current.next != None:
                if current.next.value == old_value:
                    temp = current.next
                    current.next = Node(new_value, temp)
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

    def num_from_end(self, k):
        current = self.head

        length = 0
        while current is not None:
            current = current.next
            length += 1

        if k > length:
            return "Error - input value is greater than the length of the Linked List"
        elif k < 0:
            return "Error - input value is less than 0"

        current = self.head
        for i in range(1, (length - k)):
            current = current.next
        return current

    def ll_zip(self, ll1, ll2):
        ll = LinkedList()
        ll1_curr = ll1.head
        ll2_curr = ll2.head
        # {head: blueberry, next: pineapple}
        # print(f"ll2 Curr : {ll2_curr.value}, {ll2_curr.next.value}")
        while ll1_curr != None or ll2_curr != None:
            if ll1_curr != None and ll2_curr != None:
                # Append the current values
                ll.append(ll1_curr.value)
                ll.append(ll2_curr.value)
                ll1_curr = ll1_curr.next
                ll2_curr = ll2_curr.next
                print(f"ll2 Curr : {ll2_curr}")
            # Conditions in case we reach the
            elif ll1_curr == None:
                ll.append(ll2_curr.value)
                ll2_curr = ll2_curr.next
            elif ll2_curr == None:
                ll.append(ll1_curr.value)
                ll1_curr = ll1_curr.next
        print(ll.to_string())
        return ll


if __name__ == "__main__":

    test = LinkedList()
    test2 = LinkedList()
    test3 = LinkedList()
    test.insert("pomegranate")
    test.insert("pear")
    test.insert("raspberry")
    test.insert("kiwi")
    test.insert("dragonfruit")

    test2.insert("apple")
    test2.insert("pineapple")
    test2.insert("blueberry")

    expected = test3.ll_zip(test2, test)
    print(f"test3: {expected.to_string()}")
"""    test.insert("pear")
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
""" test2.insert("apple")
    test2.insert_before("apple", "peach")
    print(f"Head test 2: {test2.head.value}")
    print(f"All Nodes Test 2: {test2.to_string()}")
"""
# Test error handling
# """test.insert()"""

# print(test_output)


"""
if __name__ == '__main__':
    ll = LinkedList()
    ll.insert(5)
    ll.insert(7)
    ll.insert(6)
    ll.insert(3)
    ll.__str__()"""
