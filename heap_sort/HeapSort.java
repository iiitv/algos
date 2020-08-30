/*
 *  Following is the implementation of HeapSort algorithm.
 *  It will sort the input array with time complexity O(N*logN)
 *  N being the size of array.
 *  Space complexity is O(1).
 */

public class HeapSort {

    public static void maxHeapify(int[] arr, int size, int parent) {  // Build max-heap of subtree of parent index
        int left = 2 * parent;
        int right = left + 1;
        int largest = parent;  // Initially considering parent as largest
        if (left < size && arr[left] > arr[largest])  // Left child is greater than parent
            largest = left;
        if (right < size && arr[right] > arr[largest]) // Right child is greater than parent
            largest = right;
        if (largest != parent) {  // If parent is largest then subtree is max-heap
            int temp = arr[parent];
            arr[parent] = arr[largest];  // Swap largest child with parent
            arr[largest] = temp;
            maxHeapify(arr, size, largest);  // Convert upper subtree to max-heap
        }
    }

    public static void heapSort(int[] arr) {
        for (int i = arr.length / 2 - 1; i >= 0; --i)
            maxHeapify(arr, arr.length, i);  // Create max-heap

        for (int i = arr.length - 1; i >= 0; --i) {
            int temp = arr[0];  // Swap first and last element
            arr[0] = arr[i];
            arr[i] = temp;
            maxHeapify(arr, i, 0);  // Create Max-Heap on reduced array
        }
    }

    public static void main(String[] args) {
        int[] arr = new int[] {10, 4, 3, 13, 1, 123};  // Creating Test array

        heapSort(arr);  // Sort the array
        for (int element : arr)  // Printing sorted array
            System.out.print(element + " ");
    }
}
