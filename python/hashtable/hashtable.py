try:
    from hashlist import HashList
except:
    from hashtable.hashlist import HashList


class Hashtable:
    pass

    def __init__(self, size=20):
        self.size = size
        self.bucket = size * [None]

    def add(self, key, value):
        index = self.hash(key)
        if self.bucket[index] is None:
            self.bucket[index] = HashList(key, value)
            # print(self.bucket[index])
        else:
            head = self.bucket[index]
            while head is not None:
                if head.key == key:
                    head.value = value
                    break
                elif head.next is None:
                    head.next = HashList(key, value)
                    break
                head = head.next
        # print(self.bucket[index])
        # print(index)
        # print(self.bucket)
        # Add
        # Arguments: key, value
        # Returns: nothing
        # This method should hash the key, and set the key and value pair in the table, handling collisions as needed.
        # Should a given key already exist, replace its value from the value argument given to this method.

    def get(self, key):
        location = self.hash(key)
        head = self.bucket[location]
        # print(f"Get: {location}")
        # print(f"Get: {head}")
        while head is not None:
            if head.key == key:
                # print(head.value)
                return head.value
            head = head.next
        return None
        # get
        # Arguments: key
        # Returns: Value associated with that key in the table

    def contains(self, key):
        index = self.hash(key)
        if self.bucket[index] is None:
            return False
        elif self.get(key) is not None:
            return True

        # contains
        # Arguments: key
        # Returns: Boolean, indicating if the key exists in the table already.

    def hash(self, key):
        sum = 0

        for ch in key:
            sum += ord(ch)

        primed = sum * 97
        index = primed % self.size
        return index

    def keys(self):
        key_list = []
        for i in self.bucket:
            if i is not None:
                head = i
                key_list.append(head.key)
                head = head.next
        key_list.sort()
        # print(key_list)
        return key_list

        # keys
        # Returns: Collection of keys


if __name__ == "__main__":
    new_hash = Hashtable()
    new_hash.add("Cat", "calico")
    new_hash.add("Dog", "dachsund")
    new_hash.add("Shark", "mako")
    new_hash.hash("Shark")
    new_hash.hash("Shark")
    new_hash.keys()
    new_hash.get("Shark")
    print(new_hash.contains("Shark"))
