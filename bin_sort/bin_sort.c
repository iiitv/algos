/* Following algorithm sorts the input array in ascending order
 * Time Complexity : O(n)-> Avg case and O(n^2)-> Worst Case
 */
#include <stdio.h>
#include <stdlib.h>

struct bucket {
	int count;
	float* value;
};

int comparator(const float* first, const float* second) {
	float a = *first, b = *second;
	float result = a - b;
	return (0 < result) - (result < 0);
}

void bucket_sort(int array[], int n) {
	struct bucket buckets[3];
	int a, b, c;
	for (a = 0; a < 3; a++) {
		buckets[a].count = 0;
		buckets[a].value = malloc(sizeof(int) * n);
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
	float array[] = {0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434};
	int n = sizeof(array) / sizeof(array[0]);
	int j;
	bucket_sort(array, n);
	for (j = 0; j < n; j++) {
		printf("%f ", array[j]);
	}
	printf("\n");
	return 0;
}
