class Stack(object):
    def __init__(self):
        self._list = []

    def __str__(self):
        return str(self._list)

    def __len__(self):
        return len(self._list)

    def push(self, item):
        self._list.append(item)

    def pop(self):
        try:
            return self._list.pop()
        except IndexError:
            raise IndexError('pop from empty stack')

    def peek(self):
        try:
            return self._list[-1]
        except IndexError:
            raise IndexError('peek into empty stack')


def main():
    st = Stack()

    # Push and print
    for i in range(10):
        st.push(i)
        print(st)
    st.push('Hello World')
    print(st)

    # Get size
    print(len(st))

    # Pop
    print(st.pop())
    print(st)

    # Peek
    print(st.peek())
    print(st)

    # Exceptions
    while len(st):  # Empty the stack
        st.pop()
    try:
        st.peek()
    except Exception as e:
        print('Exception: {0}'.format(e))
    try:
        st.pop()
    except Exception as e:
        print('Exception: {0}'.format(e))


if __name__ == '__main__':
    main()
