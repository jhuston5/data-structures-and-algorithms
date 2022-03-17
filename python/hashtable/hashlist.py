class HashList:
    def __init__(self, key, data):
        # key of the entry
        self.key = key
        # data to be stored
        self.value = data
        # reference to new entry
        self.next = None

    def __str__(self):
        return str(self.key) + ", " + self.value
