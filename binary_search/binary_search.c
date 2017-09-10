#include <stdio.h>

/*
 * @arr Array pointer
 * @arr_size Size of array
 * @search_element Element to be searched
 */

/* function to perform recursive binary search
 * input parameters:
 * @ar - user-input array.
 * @l - left index of array.
 * @r - right index of array.
 * @ele - element to be searched.
 */
int binary_search_recursive(const int *ar, int l, int r, int ele) {
	if (r >= l) {

		int mid = l + (r - l) / 2;    //calculate mid point of the array

		// If the element is present at the middle itself
		if (ar[mid] == ele) {
			return mid;
		}

		// If element is smaller than mid, then it can only be present
		// in left subarray
		if (ar[mid] > ele) {
			return binary_search_recursive(ar, l, mid - 1, ele);
		}

		// Else the element can only be present in right subarray
		return binary_search_recursive(ar, mid + 1, r, ele);
	}

	// We reach here when element is not present in array
	return -1;
}

//Function to perform iterative binary search
int binary_search(const int *arr, int arr_size, int search_element) {
	int left = 0, right = arr_size - 1;

	while (left <= right) {
		int mid = left + (right - left) / 2;

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
	int arr[] = {1, 5, 35, 112, 258, 324};
	int search_arr[] = {1, 35, 112, 324, 67};
	int i;

	for (i = 0 ; i < 5 ; i++) {

		int pos;
		pos = binary_search(arr, 6, search_arr[i]);
		if (pos >= 0) {
			printf("%d found at index %d.\n", search_arr[i], pos);
		} else {
			printf("%d not found.\n", search_arr[i]);
		}

		pos = binary_search_recursive(arr, 0, 5, search_arr[i]);
		if (pos >= 0) {
			printf("%d found at index %d, recursively\n", search_arr[i], pos);
		} else {
			printf("%d not found.\n", search_arr[i]);
		}
	}

	return 0;
}
