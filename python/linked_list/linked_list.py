"""def handle_exceptions(method):
    def wrapper(*args, kwargs):
        try:
            method
        except TypeError as error:
            print(f'You received a {method.__name__} {error}')
"""

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

    def __init__(self, head=None, next=None):
        # initialization here
        self.head = head
        self.next = next
        pass

# Insert a new Node into the LinkedList
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
        output_string = ''
        while current is not None:
            output_string += f'{current.value} -> '
            current = current.next
        else:
            output_string += 'NULL'
        return output_string


if __name__ == "__main__":

    test = LinkedList()

    test.insert('pear')
    test.insert('raspberry')
    test.insert('kiwi')
    test.insert('apple')
    print(test.includes('kiwi'))
    print(test.includes('apricot'))
    # test_output = test.to_string()
    print(f'Head: {test.head.value}')
    print(f'All Nodes: {test.to_string()}')


# print(test_output)



"""
if __name__ == '__main__':
    ll = LinkedList()
    ll.insert(5)
    ll.insert(7)
    ll.insert(6)
    ll.insert(3)
    ll.__str__()"""

