/* Following algorithm sorts the input array in ascending order
 *  Time complexity is O(n+k)
 *  Auxiliary space is O(n+k)
 *  n is number of elements and k is the range of input
 *  max is the maximum element in array
 */

#include <stdio.h>
#include <string.h>

void counting_sort(int arr[], int n, int max) {
	// Function to sort input array arr.
	int i;
	int count[max + 1];  // Array to store count's of elements.
	memset(count, 0, sizeof(count));
	int temp[n];
	for (i = 0; i < n; ++i)  // Count the occurences of contents of array.
		count[arr[i]]++;
	for (i = 1; i <= max; ++i)
		count[i] += count[i-1];
	for (i = 0; i < n; ++i) {  // Sort the array according to occurences of elements.
		temp[count[arr[i]] - 1] = arr[i];
		count[arr[i]]--;
	}
	for (i = 0; i < n; ++i)  // Copy the sorted array back to original array.
		arr[i] = temp[i];
}

int main() {
	int i;
	int max = 10;  // max is the maximum number in the array
	int arr[] = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1};
	int n = sizeof(arr) / sizeof(arr[0]);
	counting_sort(arr, n, max);
	for (i = 0; i < n; ++i)
		printf("%d ", arr[i]);
	return 0;
}
