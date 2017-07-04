class Node(object):
    def __init__(self, data=None, next_=None):
        # Initialises Node
        self.data = data
        self.next = next_

    def __str__(self):
        return str(self.data) if self.next is None \
            else '{0} -> {1}'.format(self.data, self.next)


class LinkedList(object):
    def __init__(self):
        # Initialises Linked List.
        self.head = None
        self.size = 0

    def __str__(self):
        return str(self.head)

    def __len__(self):
        return self.size

    def add_front(self, data):
        # Inserts element at first position.
        self.add(data, 0)

    def add_last(self, data):
        # Inserts element at last position.
        self.add(data, self.size)

    def add(self, data, index):
        # Inserts data at index.
        if index < 0 or index > self.size:
            raise IndexError('Index Out of Bound')
        temp = self.head
        if index is 0:
            n = Node(data)
            n.next = self.head
            self.head = n
        else:
            for _ in range(index - 1):
                temp = temp.next
            n = Node(data)
            n.next = temp.next
            temp.next = n
        self.size += 1
        return n

    def remove_front(self):
        # Deletes First Element
        self.remove(0)

    def remove_last(self):
        # Deletes Last Element
        self.remove(self.size - 1)

    def remove(self, index):
        # Deletes Element present at index
        if self.is_empty():
            raise IndexError('List is empty')
        if index < 0 or index >= self.size:
            raise IndexError('Index out of bound')
        if index is 0:
            removed = self.head.data
            self.head = self.head.next
        else:
            temp = self.head
            if temp.next is None:
                removed = temp.data
                self.head = None
            else:
                for _ in range(index - 1):
                    temp = temp.next
                removed = temp.next.data
                temp.next = temp.next.next
        self.size -= 1
        return removed

    def remove_by_value(self, value):
        # Search and removes the value from Linked List.
        self.remove(self.find_first(value))

    def search(self, inp):
        # Search for inp in Linked List and return it's index
        head = self.head
        for i in range(self.size):
            if head.data is inp:
                return i
            else:
                head = head.next
        raise ValueError('Value not found')

    def find_first(self, inp):
        # Finds First occurence of data in Linked List
        return self.search(inp)

    def find_last(self, inp):
        # Finds Last occurence of data in Linked List
        new_list = self.clone()
        new_list.reverse()
        return self.size - new_list.search(inp) - 1

    def set(self, data, index):
        # Sets the data to index and replaces previously existing data.
        if index >= self.size:
            self.add(data, index)
        else:
            head = self.head
            for i in range(self.size):
                if i is index:
                    head.data = data
                head = head.next

    def clear(self):
        # Removes all elements from Linked List
        self.head = None
        self.size = 0

    def is_empty(self):
        # Checks if Linked List is Empty.
        return self.size is 0

    def clone(self):
        # Clones the Linked List
        new_list = LinkedList()
        temp = self.head
        while temp.next:
            new_list.add_last(temp.data)
            temp = temp.next
        new_list.add_last(temp.data)
        return new_list

    def reverse(self):
        # Function to reverse Linked List
        prev = None
        current = self.head
        while current is not None:
            next_ = current.next
            current.next = prev
            prev = current
            current = next_
        self.head = prev


def main():
    l_list = LinkedList()

    l_list.add_last(5)
    print(str(l_list))
    print('Size:', len(l_list))

    l_list.add_last(15)
    print(str(l_list))
    print('Size:', len(l_list))

    # Add Element at Front
    l_list.add_front(10)
    print(str(l_list))
    print('Size:', len(l_list))

    # Add Element at Front
    l_list.add_front(11)
    print(str(l_list))
    print('Size:', len(l_list))

    # Add Element at Last
    l_list.add_last(6)
    print(str(l_list))
    print('Size:', len(l_list))

    # Add Element at Front
    l_list.add_front(5)
    print(str(l_list))
    print('Size:', len(l_list))

    # Finding Fist Occurance in Linked List
    try:
        print('First Element found at index:', l_list.find_first(5))
    except ValueError:
        print('Value not Found')

    # Finding Last Occurance in Linked List
    try:
        print('Last Element found at index:', l_list.find_last(5))
    except ValueError:
        print('Value not Found')

    # Remove by Value
    l_list.remove_by_value(5)
    print(str(l_list))
    print('Size:', len(l_list))

    # Reversing Linked List
    l_list.reverse()
    print('Reversed:', str(l_list))

    # Add Element at Index
    try:
        l_list.add(25, -1)
    except IndexError:
        print('Invalid Index')
    print(str(l_list))
    print('Size:', len(l_list))

    # Add Element at Index
    try:
        l_list.set(25, 2)
    except IndexError:
        print('Invalid Index')
    print(str(l_list))
    print('Size:', len(l_list))

    # Cloning Linked List
    print('Cloned :', str(l_list.clone()))

    # Removes Element from Front
    l_list.remove_front()
    print(str(l_list))
    print('Size:', len(l_list))

    # Removes Element from End
    l_list.remove_last()
    print(str(l_list))
    print('Size:', len(l_list))

    # Removes Element from Index
    try:
        l_list.remove(3)
    except IndexError:
        print('Value not found')
    print(str(l_list))
    print('Size:', len(l_list))

    # Search for Element with data as arguement
    try:
        print('Element found at index :', l_list.search(25))
    except ValueError:
        print('Value Not Found')

    try:
        print('Element found at index', l_list.search(10))
    except ValueError:
        print('Value Not Found')

    # Clearing the Linked List
    l_list.clear()
    print(str(l_list))
    print('Size:', len(l_list))


if __name__ == "__main__":
    main()
