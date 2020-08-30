/*
 *  Following implementation of Stack uses LinkedList
 *  The last element of LinkedList is considered as the Top of Stack
 *  T defines the type of Stack we wish to create
 */

import java.util.LinkedList;
import java.util.NoSuchElementException;

public class Stack<T> {
    private LinkedList<T> stack;

    public Stack() {   // Constructor to create empty Stack
        stack = new LinkedList<>();
    }

    public void push(T data) { // Add element to Top of Stack
        stack.addLast(data);
    }

    public T pop() throws NoSuchElementException {    // Remove element from top of Stack
        return stack.removeLast();
    }

    public static void main(String[] args) {
        Stack<Integer> obj = new Stack<>();
        System.out.println("Putting element in the stack.");
        for (int i = 1; i <= 10; i++) {
            obj.push(i);
            System.out.println("Pushed "+i);
        }
        System.out.println("\nPoping elements out of stack.");
        while(true) { // Remove the elements till stack is empty,
            try {
                Integer curr_element = obj.pop();
                System.out.println("Popped " + curr_element);
            }
            catch(NoSuchElementException nsee) {
                System.out.println("Stack is empty now.");
                break;
            }
        }
    }
}
