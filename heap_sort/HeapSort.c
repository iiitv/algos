/*
 * C program to Implement Heap sort.
 * Time complexity: Average = O( n log( n ) ), worst case complexity = O( n log( n ) ).
 * Space complexity: O(1).
 */

#include<stdio.h>
#include <stdlib.h>

//i is the root of subtree, a is an array, HEAPSIZE is size of heap
void  max_heapify(int a[], int i, int HEAPSIZE) {
    int largest;
    int l = (2 * i) + 1;  // left child
    int r = (2 * i) + 2;  // Right child
    // Check if left child is larger than root.
    if ((l <= HEAPSIZE) && (a[l] > a[i]))
         largest = l;
    else
         largest = i;
    // Check if right child is larger than root.
    if ((r <= HEAPSIZE) && (a[r] > a[largest]))
         largest = r ;
    // If root is not the largest.
    if (largest != i) {
         int tmp = a[i];
         a[i] = a[largest];
         a[largest] = tmp;
         max_heapify(a, largest, HEAPSIZE);
    }
}

// a is the array.
void heap_sort(int a[], int HEAPSIZE) {
    int i;
    // Building max heap.
    for (i = HEAPSIZE/2; i >= 0; i--) {
         max_heapify(a, i, HEAPSIZE);
    }
    // One by one extract an element from heap
    for (i = HEAPSIZE; i > 0; i--) {
        int tmp = a[i];
        a[i] = a[0];
        a[0] = tmp;
        HEAPSIZE--;
        // Again build max heap with the reduced array.
        max_heapify(a, 0, HEAPSIZE);
    }
}

int main() {
    int i, r, SIZE = 8;
    // Unsorted data
    int a[] = {10000, -999, 240, 1111111, 3, 2, 452, -65};
    // Calling heap_sort function
    heap_sort(a, SIZE-1);
    printf("After Sorting:\t");

    for (i = 0; i < SIZE; i++)
        printf("%d ", a[i]);

    return 0;
}
