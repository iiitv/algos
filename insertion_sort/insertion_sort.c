/*
 *  arr - array to be sorted
 *  arr_size - size of array
 */
#include <stdio.h>

void insertion_sort(int *arr, int arr_size) {
	int i, j;
	for (i = 1; i < arr_size; i++) {
		int key = arr[i];
		j = i - 1;
		/* Move elements of arr[0...i-1], that are
			greater than key, to one position ahead
			of their current position */
		while (j >= 0 && arr[j] > key) {
			arr[j+1] = arr[j];
			j--;
		}
		arr[j+1] = key;
	}
}

int main() {
	int arr[] = {12, 11, 13, 5, 6};
	int arr_size = sizeof(arr) / sizeof(arr[0]);
	int i;

	insertion_sort(arr, arr_size);

	for (i = 0; i < arr_size; i++) {   // Printing the sorted array
		printf("%d ", arr[i]);
	}
	printf("\n");
	return 0;
}
