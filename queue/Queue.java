import java.util.NoSuchElementException;

/**
 * Implements https://docs.oracle.com/javase/8/docs/api/java/util/Queue.html
 */
public class Queue<T> {

    private int total;
    // Linked Lists used to store the data
    private Node first, last;

    private class Node {

        private T data;
        private Node next;

        public Node(T data) {
            this.data = data;
        }
    }

    /**
     * Inserts the specified element into this queue if it is possible to do so immediately without
     * violating capacity restrictions, returning true upon success and throwing an
     * IllegalStateException if no space is currently available.
     *
     * @param element the element to add
     * @return true upon success, throwing an IllegalStateException if no space is currently
     * available.
     */
    public boolean add(T element) {
        Node newNode = new Node(element);

        Node current = last;
        last = newNode;

        if (total == 0) {
            first = last;
        } else {
            current.next = last;
        }
        total++;

        return true;
    }

    /**
     * Inserts the specified element into this queue if it is possible to do so immediately without
     * violating capacity restrictions.
     *
     * @param element the element to add
     * @return true if the element was added to this queue, else false
     */
    public boolean offer(T element) {
        try {
            return add(element);
        } catch (Exception ex) {
            //failed to add, return false
            return false;
        }
    }

    /**
     * Retrieves and removes the head of this queue.
     * This method differs from poll only in that it throws an exception if this queue is empty.
     *
     * @return the head of this queue.
     * @throws NoSuchElementException if this queue is empty
     */
    public T remove() throws NoSuchElementException {
        if (total == 0) {
            throw new NoSuchElementException();
        }
        T element = first.data;
        first = first.next;
        total--;
        if (total == 0) {
            last = null;
        }
        return element;
    }

    /**
     * Retrieves and removes the head of this queue, or returns null if this queue is empty.
     * This method differs from peek only in that it throws an exception if this queue is empty.
     *
     * @return the head of this queue, or returns null if this queue is empty.
     */
    public T poll() {
        try {
            return remove();
        } catch (Exception ex) {
            //failed to remove, return null
            return null;
        }
    }

    /**
     * Retrieves, but does not remove, the head of this queue.
     *
     * @return the head of this queue
     * @throws NoSuchElementException if this queue is empty
     */
    public T element() throws NoSuchElementException {
        if (total == 0) {
            throw new NoSuchElementException();
        }
        return first.data;
    }

    /**
     * Retrieves, but does not remove, the head of this queue, or returns null if this queue is empty.
     *
     * @return the head of this queue, or returns null if this queue is empty.
     */
    public T peek() {
        return total == 0 ? null : first.data;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        Node tmp = first;
        while (tmp != null) {
            sb.append(tmp.data).append(", ");
            tmp = tmp.next;
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        Queue<Integer> queue = new Queue<>();
        for (int i = 1; i <= 10; i++) { // Creates a dummy queue which contains integers from 1-10
            queue.add(i);
        }

        System.out.println("Queue :");

        while (queue.peek() != null) {
            System.out.println(queue.poll());
        }
    }
}
