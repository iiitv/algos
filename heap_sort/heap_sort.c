/*
 * C program to Implement Heap sort.
 * Time complexity: Average = O( n log( n ) ), worst case complexity = O( n log( n ) ).
 * Space complexity: O(1).
 */

#include <stdio.h>

// root = index root of the subtree, a is an array, heapsize = size of heap
void  max_heapify(int a[], int root, int heapsize) {
	int largest = root;
	int l = (2 * root) + 1;  // left child
	int r = (2 * root) + 2;  // Right child
	// Check if left child is larger than root.
	if ((l < heapsize) && (a[l] > a[root])) {
		largest = l;
	}
	// Check if right child is larger than largest.
	if ((r < heapsize) && (a[r] > a[largest])) {
		largest = r ;
	}
	// If root is not the largest.
	if (largest != root) {
		int tmp = a[root];
		a[root] = a[largest];
		a[largest] = tmp;
		max_heapify(a, largest, heapsize);
	}
}

// a is the array.
void heap_sort(int a[], int heapsize) {
	int i;
	// Building max heap.
	for (i = (heapsize / 2) - 1; i >= 0; i--) {
		max_heapify(a, i, heapsize);
	}
	// One by one extract an element from heap
	for (i = heapsize - 1; i > 0; i--) {
		int tmp = a[i];
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
	int a[] = {10000, -999, 240, 1111111, 3, 2, 452, -65};
	int size = sizeof(a) / sizeof(a[0]);
	// Calling heap_sort function
	heap_sort(a, size);
	printf("After Sorting:\t");

	for (i = 0; i < size; i++) {
		printf("%d ", a[i]);
	}

	return 0;
}
