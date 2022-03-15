class Hashtable:
    pass

    def __init__(self, size=10024):
        self.size = size
        self.bucket = size * [None]

    def add(self, key, value):
        index = hash(key)

        pass
        # Add
        # Arguments: key, value
        # Returns: nothing
        # This method should hash the key, and set the key and value pair in the table, handling collisions as needed.
        # Should a given key already exist, replace its value from the value argument given to this method.

    def get(self, key):
        pass
        # get
        # Arguments: key
        # Returns: Value associated with that key in the table

    def contains():
        pass
        # contains
        # Arguments: key
        # Returns: Boolean, indicating if the key exists in the table already.

    def hash(self, key):
        "Cat"

        "aCt"
        sum = 0

        for ch in key:

            sum += ord(ch)

        primed = sum * 97

        index = primed % self.size

        return index

    def keys():
        pass

        # keys
        # Returns: Collection of keys


if __name__ == "__main__":
    new_hash = Hashtable()
    new_hash.hash("Cat")
