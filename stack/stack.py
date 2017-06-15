class Stack(object):

    def __init__(self):
        self._list = []

    def push(self, item):
        self._list.append(item)

    def pop(self):
        try:
            return self._list.pop()
        except IndexError:
            raise IndexError('pop from empty stack')


def main():
    st = Stack()
    # Push and print
    for i in range(10):
        st.push(i)
        print("Pushed ", i)
    st.push('Hello World')

    # Pop
    print(st.pop())

    # Exceptions
    while True:  # Empty the stack
        try:
            st.pop()
        except Exception as e:
            print('Exception: {0}'.format(e))
            break


if __name__ == '__main__':
    main()
