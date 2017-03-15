#include <stdio.h>

/*
 * @arr Array pointer
 * @arr_size Size of array
 * @search_element Element to be searched
 */
int binary_search(const int *arr, int arr_size, int search_element) {
	int left = 0, right = arr_size - 1;

	while (left <= right) {
		int mid = (left + right) / 2;

		if (arr[mid] == search_element)	// Element found
			return mid;
		if (arr[mid] < search_element)	// Look in right half
			left = mid + 1;
		else				// Look in left half
			right = mid - 1;
	}

	return -1;				// Element not found
}

int main() {
	int arr[] = {1, 5, 35, 112, 258, 324},
		search_arr[] = {1, 35, 112, 324, 67},
		pos, i;

	for (i = 0 ; i < 5 ; i ++) {
		pos = binary_search(arr, 6, search_arr[i]);

		if (pos >= 0)
			printf("%d found at index %d.\n", search_arr[i], pos);
		else
			printf("%d not found.\n", search_arr[i]);
	}

	return 0;
}
