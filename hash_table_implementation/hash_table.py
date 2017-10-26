class HashTable(object):

    def __init__(self, size):
        # Set up size and slots and data
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        # Only use integer keys for ease of use with the Hash Function
        # Get the hash value
        hashvalue = self.hashfunction(key, len(self.slots))

        # If Slot is Empty
        if self.slots[hashvalue] is None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            # If key already exists, replace old value
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data
            # Otherwise, find the next available slot
            else:
                nslt = self.rehash(hashvalue, len(self.slots))

                # Get to the next slot
                while self.slots[nslt] is not None and self.slots[nslt] != key:
                    nslt = self.rehash(nslot, len(self.slots))
                # Set new key, if NONE
                if self.slots[nslt] is None:
                    self.slots[nslt] = key
                    self.data[nslt] = data

                # Otherwise replace old value
                else:
                    self.data[nslt] = data
    @classmethod
    def hashfunction(self, key, size):
        # Remainder Method
        return key % size
    @classmethod
    def rehash(self, oldhash, size):
        # For finding next possible positions
        return (oldhash+1) % size

    def get(self, key):
        # Getting items given a key and seting up vars
        startslot = self.hashfunction(key, len(self.slots))
        data = None
        stop = False
        found = False
        position = startslot
        # Until we discern that its not empty
        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True
        return data

    # Special Methods for use with Python indexing
    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)


def main():

    h = HashTable(5)
    # Put our first key in
    h[1] = 'one'
    h[2] = 'two'
    h[3] = 'three'
    print(h[1])
    print(h[2])
    h[1] = 'new_one'
    h[1]


if __name__ == '__main__':
    main()
