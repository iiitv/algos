#include <stdio.h>
#include <stdlib.h>

struct bucket {
	int count;
	int* value;
};

int comparator(const void*first, const void* second) {
	int a = *((int*)first), b = *((int*)second);
	if (a == b) {
		return 0;
	}
	else if (a < b) {
		return -1;
	}
	else {
		return 1;
	}
}

void bucketSort(int array[], int n) {
	struct bucket buckets[3];
	int a, b, c;
	for (a = 0; a < 3; a++) {
		buckets[a].count = 0;
		buckets[a].value = (int*)malloc(sizeof(int) * n);
	}
	for (a = 0; a < n; a++) {
		if (array[a] < 0) {
			buckets[0].value[buckets[0].count++] = array[a];
		}
		else if (array[a] > 10) {
			buckets[2].value[buckets[2].count++] = array[a];
		}
		else {
			buckets[1].value[buckets[1].count++] = array[a];
		}
	}
	for (c = 0, a = 0; a < 3; a++) {
		qsort(buckets[a].value, buckets[a].count, sizeof(int), &comparator);
		for (b = 0; b < buckets[a].count; b++) {
			array[c + b] = buckets[a].value[b];
		}
		c += buckets[a].count;
		free(buckets[a].value);
	}
}

int main() {
	int array[12] = {-5, -9, 1000, 1, -10, 0, 2, 3, 5, 4, 1234, 7};
	int n = sizeof(array) / sizeof(array[0]);
	int j;
	bucketSort(array, n);
	for (j = 0; j < n; j++)
		printf("%d ", array[j]);
	return 0;
}
