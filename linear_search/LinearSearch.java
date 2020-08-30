/*
 *  Linear Search algorithm searches for a given number in array
 *  Time complexity is O(n) , n is size of array
 */
public class LinearSearch {

    public static int linearSearch(int[] arr, int searchElement) {
        for(int i = 0; i < arr.length; i++) {
            if(arr[i] == searchElement)
                return i;	// Element found
        }
        return -1;	// Element not found
    }

    public static void main(String[] args) {
        int[] array = new int[100];
        // Initializing array with 1,2,....,100
        for(int i = 1; i <= 100; i++)
            array[i-1] = i;
        // Elements to be searched in the array
        int[] search = {12,55,34,102,78};
        for(int i = 0; i < 5; i++) {
            int index = linearSearch(array, search[i]);
            if(index >= 0)
                System.out.println(search[i] + " found at index " + index);
            else
                System.out.println(search[i] + " not found in the list");
        }
    }
}
