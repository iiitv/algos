/*
    The Program evaluates the Next Greater Element in an array
    The algorithm has O(N) Time Complexity and O(N) Space Complexity
    It uses Stack to compute the next greater element of every element in an array
*/

import java.util.Stack;

class NextGreaterElement {

    //Computes the next greater element of every element in the array
    public void nextGreaterElement(int[] elements) {
        Stack<Integer> stack = new Stack<>();

        int n = elements.length; //stores the Size of the array

        //Iterating the array for computing NGE for every element
        for(int i=0;i<n;i++) {
            int element = elements[i];
            if(!stack.isEmpty()) {
                int topElement = stack.pop();
                while(topElement < element) { //Continue popping every small elements in the stack until a greater element is found
                    System.out.println("Element: "+topElement+"|| Next Greater Element: "+element);
                    if(stack.isEmpty()) {
                        break;
                    }
                    topElement = stack.pop();
                }
                if(topElement > element) {  //If the element popped from the stack was greater than push it back into the stack
                    stack.push(topElement);
                }
            }
            stack.push(element);  //After processing, push the element of the list into the stack
        }

        //For the rest elements in the stack, there was no NGE, Hence we pop those elements with NGE value as -1
        while(!stack.isEmpty()) {
            int topElement = stack.pop();
            System.out.println("Element: "+topElement+" || Next Greater Element: -1");
        }
    }

    public static void main(String[] args) {
        int[] elements = {5,3,13,2,9,10,17,13,20};
        NextGreaterElement nge = new NextGreaterElement();
        nge.nextGreaterElement(elements);
    }
}
