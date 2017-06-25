/*
 *  Following Algorithm sorts the given array in worst case time complexity O(n*log(n))
 *  and space complexity O(n), n being size of array.
 */

#include <stdio.h>

void merge(int *arr, int left, int mid, int right) {
	int i, j, k;
	int n_left = mid - left + 1;
	int n_right = right - mid;
	int left_arr[n_left];
	int right_arr[n_right];
	for (i = 0; i < n_left; i++)
		left_arr[i] = arr[left + i];
	for (j = 0; j < n_right; j++)
		right_arr[j] = arr[mid + 1 + j];
	i = 0;
	j = 0;
	k = left;
	while (i < n_left && j < n_right) {
		if (left_arr[i] <= right_arr[j]) {
			arr[k] = left_arr[i];
			i++;
		} else {
			arr[k] = right_arr[j];
			j++;
		}
		k++;
	}
	while (i < n_left) {
		arr[k] = left_arr[i];
		i++;
		k++;
	}
	while (j < n_right) {
		arr[k] = right_arr[j];
		j++;
		k++;
	}
}

void merge_sort(int *arr, int left, int right) {
	if (left < right) {
		int mid = (left + right) / 2;
		merge_sort(arr, left, mid);
		merge_sort(arr, mid + 1, right);
		merge(arr, left, mid, right);
	}
}

int main() {
	int i;
	int arr[] = {7, 10, 14, 1, 2, 6, 17, 0};
	int size = sizeof(arr) / sizeof(arr[0]);
	merge_sort(arr, 0, size - 1);
	for (i = 0; i < size; i++) {
		printf("%d ", arr[i]);
	}
	return 0;
}
