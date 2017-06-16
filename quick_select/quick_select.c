#include <stdio.h>

/*
 * partition function
 * ar        : array on which partitioning has to be done
 * left      : left index of the partitioning subarray
 * right     : right index of the partitioning subarray
 * pivot_idx : pivot index from which partition has to done
 * store_idx : index of the last element of the left subarray
 * return    : the index of the last element of the left subarray
 */
int partition(int *ar, int left, int right, int pivot_idx) {
	int pivot_value = ar[pivot_idx];
	int temp = ar[right];
	ar[right] = ar[pivot_idx];
	ar[pivot_idx] = temp;

	int store_idx = left;
	while (left < right) {
		if (ar[left] < pivot_value) {
			temp = ar[store_idx];
			ar[store_idx] = ar[left];
			ar[left] = temp;
			store_idx++;
		}
		left++;
	}
	temp = ar[right];
	ar[right] = ar[store_idx];
	ar[store_idx] = temp;
	return store_idx;
}

/*
 * Quick Select function
 * left        : left index of the subarray
 * right       : right index of the subarray
 * pos         : position to find the element using quick sort
 * pivot_index : pivot index
 * return      : the value of element at pos place in the sorted array
 */
int quick_select(int *ar, int left, int right, int pos) {
	int pivot_index;
	if (left == right)
		return ar[left];
	pivot_index = right - 1;
	pivot_index = partition(ar, left, right, pivot_index);
	if (pos == pivot_index) {
		return ar[pivot_index];
	} else if (pos < pivot_index) {
		return quick_select(ar, left, pivot_index - 1, pos);
	} else {
		return quick_select(ar, pivot_index + 1, right, pos);
	}
}

int main() {
	int ar[] = {10, 5, 1, 6, 7, 3, 2, 4, 8, 9};
	printf("%d\n", quick_select(ar, 0, 9, 3));
	return 0;
}
