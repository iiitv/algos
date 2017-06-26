/*
 * Following is the code for Linked List
 * T defines the type of Linked List to be created
 */

import java.util.NoSuchElementException;

// Class to create a Node that contains data and pointer to next Node
class Node<T> {
    public T data;     // Data of type T
    public Node<T> next;     // Pointer to next Node

    // Constructor to create a Node
    public Node(T input) {
        this.data = input;
        this.next = null;
    }
}

// Class containing methods to be performed on Linked List
class LinkedList<T> {

    private Node<T> head;     // Pointer to first node of the Linked List
    private int sizeOfList = 0;     // Size of the Linked List

    // Constructor to create an empty Linked List
    public LinkedList() {
        head = null;
    }

    // Method to add an element to the start of the Linked List
    public void addFront(T input) {
        Node<T> newNode = new Node<T>(input);
        newNode.next = head;
        head = newNode;
        sizeOfList++;
    }

    // Method to add an element to the end of the Linked List
    public void addLast(T input) {
        if (head == null) {
            Node<T> newNode = new Node<T>(input);
            head = newNode;
            sizeOfList = 1;
        }
        else {
            Node<T> temp = head;
            while (temp.next != null)
                temp = temp.next;
            Node<T> newNode = new Node<T>(input);
            temp.next = newNode;
            sizeOfList++;
        }
    }

    // Method to add an element at a given index
    public void add(T input, int index) {
        if (index < 0 || index > sizeOfList)
            throw new IndexOutOfBoundsException("Invalid Index");
        Node<T> temp = head;
        if (index == 0)
            addFront(input);
        else {
            for (int i = 0; i < index-1; i++)
                temp = temp.next;
            Node<T> newNode = new Node<T>(input);
            newNode.next = temp.next;
            temp.next = newNode;
            sizeOfList++;
        }
    }

    // Method to remove the front element from the Linked List
    public T removeFront() {
        if (isEmpty())
            throw new NoSuchElementException();
        T removedElement = head.data;
        head = head.next;
        sizeOfList--;
        return removedElement;
    }

    // Method to remove the last element from the Linked List
    public T removeLast() {
        if (isEmpty())
            throw new NoSuchElementException();
        T removedElement;
        if (head.next == null) {
            removedElement = head.data;
            head = null;
        }
        else {
            Node<T> temp = head;
            while (temp.next.next != null)
                temp = temp.next;
            removedElement = temp.next.data;
            temp.next = null;
        }
        sizeOfList--;
        return removedElement;
    }

    // Method to remove element at specific index from the Linked List
    public T remove(int index) {
        if (isEmpty())
            throw new NoSuchElementException();
        if (index < 0 || index > sizeOfList)
            throw new IndexOutOfBoundsException("Invalid Index");
        if (index > 0) {
            Node<T> temp = head;
            for (int i = 0; i < index-1; i++)
                temp = temp.next;
            T removedElement = temp.next.data;
            temp.next = temp.next.next;
            sizeOfList--;
            return removedElement;
        }
        return removeFront();
    }

    // Method to search a element in the Linked List returns its index i
    public int search(T input) {
        Node<T> temp = head;
        for (int i = 0; i < sizeOfList; i++) {
            if (temp.data == input)
                return i;
            else
                temp = temp.next;
        }
        return -1;     // Will return -1 if not found
    }

    // Method to display the Linked List
    public void display() {
        Node<T> temp = head;
        if (temp != null) {
            System.out.print("[");
            while (temp != null) {
                System.out.print(temp.data+", ");
                temp = temp.next;
            }
            System.out.print("\b\b]\n");
        }
    }

    // Method to display the size of Linked List
    public int size() {
        return sizeOfList;
    }

    // Method to check whether the Linked List is empty
    public boolean isEmpty() {
        return sizeOfList == 0;
    }

    public static void main(String[] args) {

        LinkedList<Integer> list = new LinkedList<Integer>();     // Creating an empty Linked List

        // Adding element to the list
        list.addFront(3);
        list.display();

        // Adding elements at the end
        list.addLast(5);
        list.addLast(6);
        list.display();

        // Adding elements to front
        list.addFront(2);
        list.addFront(1);
        list.display();

        // Adding element at a given index (Adding 4 at index 3)
        list.add(4, 3);
        list.display();

        // Removing First Element
        list.removeFront();
        list.display();

        // Removing Last Element
        list.removeLast();
        list.display();

        // Removing an element from a index
        list.remove(2);
        list.display();

        // Searching for an element in the Linked List
        int found = list.search(5);
        if (found >= 0)
            System.out.println("Element found at index: " + list.search(5));
        else
            System.out.println("Element not found");

        // Checking size of list and whether it is empty
        if (list.isEmpty())
            System.out.println("List is empty");
        else
            System.out.println("List is not empty, Size of list: " + list.size());

        // Emptying the LinkedList
        while (!list.isEmpty())
            list.removeLast();

        // Testing Exceptions thrown
        try {
            list.removeLast();
        } catch (NoSuchElementException e) {
            System.out.println("List Empty");
        }
    }
}

