/*
*  Following implementation of Stack uses LinkedList
*  The last element of LinkedList is considered as the Top of Stack
*  T defines the type of Stack we wish to create
*/

import java.util.LinkedList;
import java.util.NoSuchElementException;

class Stack<T> {
    private int size;
    private LinkedList<T> stack;
        
    public Stack() {   // Constructor to create empty Stack
        stack = new LinkedList<> ();
        size = 0;
    }

    public void push(T data) { // Add element to Top of Stack
        stack.addLast(data);
        size++;
    }
        
    public T pop() {    // Remove element from top of Stack
        if (size == 0) {
            throw new NoSuchElementException("Cannot Pop, Stack is empty");
        }
        size--;
        return stack.removeLast();
    }
       
    public T peek() {   // Get the element at the Top of Stack
        if (size == 0) {
            throw new NoSuchElementException("No element left to Peek");
        }
        size--;
        return stack.getLast();
    }
        
    public int getSize() {  // Get size of Stack
        return size;
    }
        
    public void displayStack() {    // Display Stack
        if (size == 0) {
            throw new NoSuchElementException("No element in Stack to Display");
        }
        for (int i = size-1; i >= 0; i--) {
                System.out.print(stack.get(i) + " ");
        }
        System.out.println();
    }    
}

class StackTest {    // Tester Class to check the working of Stack
    public static void main(String[] args) {
        Stack<Integer> obj = new Stack<Integer>();
        // Adding elements for testing
        for (int i = 1; i <= 10; i++) {
            obj.push(i);
        }
        // Displaying the Stack (Top first basis)
        System.out.print("Stack is: ");
        obj.displayStack();
        // Getting size
        System.out.println("Size of stack is:" + obj.getSize());
        // Pop element
        obj.pop();
        System.out.print("Stack is: ");
        obj.displayStack();
        // Peeking
        System.out.println("Top element is:" + obj.peek());
        // Checking of Exceptions
        while(obj.getSize() != 0) { // Empty the stack
            obj.pop();
        }
        try {
        obj.peek(); // Checking for peek() same can be done for pop()
        } catch (NoSuchElementException exp) {
            System.out.println("Stack is empty.");
        }
    }
}
