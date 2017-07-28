#include <stdio.h>
#include <stdlib.h>

int largestSumContiguousSubArray(int arr[], int size) {
	int max_till = 0;
	int max_int = 0;
	for (int i = 0; i < size; i++) {
		max_int = max_int + arr[i];
		max_int = max(max_int, arr[i]);
		max_till = max(max_till, max_int);
	}
	return max_till;
}

int max(int first, int second) {
	if (first < second)	{
		return second;
	} else {
		return first;
	}
}

int main() {
	int array[] = {-2, 1, -3, 4, -1, 2, 1, -5, 4, 5};
	int size = sizeof(array) / sizeof(array[0]);
	printf("%d\n", largestSumContiguousSubArray(array, size));
}
