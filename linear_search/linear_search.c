#include <stdio.h>
/*
 *  Algorithm to find a given number in an array
 *  *arr : given array to search in
 *  search_element : Element to be searched
 *  size : size of array
 */
int linear_search(const int *arr, int size, int search_element) {
	int i;
	for (i = 0; i < size; i++) {
		if (arr[i] == search_element)
			return i;				// Element found
	}
	return -1;						// Element not found
}

int main() {
	int array[100], i;

	// Initializing array with 1,2,....,100
	for (i = 1; i <= 100; i++)
		array[i-1] = i;

	// Elements to be searched in the array
	int search[5] = {12, 55, 34, 102, 78};

	for (i = 0; i < 5; i++) {
		int index = linear_search(array, 100, search[i]);

		if (index >= 0)
			printf("%d found at index %d\n", search[i], index);
		else
			printf("%d not found in the list\n", search[i]);
	}
	return 0;
}
