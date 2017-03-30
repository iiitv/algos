#include <stdio.h>
#include <stdlib.h>

int largestSumContinousSubArray(int arr[], int size) {
	int max_till = 0;
	int max_int = 0;
	for (int i = 0; i < size; i++) {
		max_int = max_int + arr[i];
		if(max_till < max_int) {
			max_till = max_int;
		}
		if (max_int < 0) {
			max_int = 0;
		}
	}
	return max_till;
}

int main() {
	int array[10];
	for (int k = 0; k < 10; k++) {
		array[k] = rand() % 10;
	}
	printf("%d", largestSumContinousSubArray(array, 10));
}
