/*
 * C program to Implement Heap sort.
 * Time complexity: Average = O( n log( n ) ), worst case complexity = O( n log( n ) ).
 * Space complexity: O(1).
 */

#include<stdio.h>
#include <stdlib.h>

void  max_heapify(int a[], int i, int heapsize) {
    int tmp, largest;
    int l = (2 * i) + 1;  // left child
    int r = (2 * i) + 2;  // Right child
    // Check if left child is larger than root.
    if ((l <= heapsize) && (a[l] > a[i]))
         largest = l;

    else
         largest = i;
    // Check if right child is larger than root.
    if ((r <= heapsize) && (a[r] > a[largest]))
         largest = r ;
    // If root is not the largest.
    if (largest != i) {
         tmp = a[i];
         a[i] = a[largest];
         a[largest] = tmp;
         max_heapify(a, largest, heapsize);
    }

}

void heap_sort(int a[], int heapsize) {
    int i, tmp;
    // Building max heap.
    for (i = heapsize/2; i >= 0; i--) {
         max_heapify(a, i, heapsize);
    }
    // One by one extract an element from heap
    for (i = heapsize; i > 0; i--) {
        tmp = a[i];
        a[i] = a[0];
        a[0] = tmp;
        heapsize--;
        // Again build max heap with the reduced array.
        max_heapify(a, 0, heapsize);
    }
}

int main() {
    int i, r;
    // Unsorted data
    int a[8] = { 10000, -999, 240, 1111111, 3, 2, 452, -65 };
    // Calling heap_sort function
    heap_sort(a, 7);
    printf("After Sorting:\t");

    for (i = 0; i < 8; i++)
        printf("%d ", a[i]);
    return 0;
}
