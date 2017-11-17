class Queue(object):

    def __init__(self):
        self._list = []

    def count(self):
        return len(self._list)

    def is_empty(self):
        return self.count() == 0

    def enqueue(self, item):
        self._list.append(item)

    def dequeue(self):
        try:
            return self._list.pop(0)
        except IndexError:
            raise IndexError('pop from empty stack')


def main():
    queue = Queue()
    n = 100

    print('Empty queue: {0}'.format(queue.is_empty()))

    while queue.count() < 5:
        print('pushing elements: {0}'.format(n))
        queue.enqueue(n)
        n = n + 100

    print('Number of items: {0}'.format(queue.count()))
    print('Empty queue: {0}'.format(queue.is_empty()))

    while True:
        try:
            print('Removing element: {0}'.format(queue.dequeue()))
        except Exception as e:
            print('Exception: {0}'.format(e))
            break

    print('Number of items: {0}'.format(queue.count()))
    print('Empty queue: {0}'.format(queue.is_empty()))


if __name__ == '__main__':
    main()
