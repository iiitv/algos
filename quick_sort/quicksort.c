#include "stdio.h"

/*
 * @ar_size array size
 * @ar array pointer
 */
void quicksort(int ar_size, int * ar) {
	int piv;
	piv = ar[ar_size-1]; // chose last element as pivot
	int i, temp, c = 0;
	int prevmax, prevind = -1; // stores last number >= pivot

	for (i=0; i<ar_size-1; i++){
		if (ar[i] < piv){
			if ((prevind > -1) && (ar[i] < prevmax)){
				// swap current and previous large element
				// current element is less than prevmax so move it to the left side
				// and prevmax to the right side
				temp = ar[i];
				ar[i] = prevmax;
				ar[prevind] = temp;
				// prevind now has a less than pivot element, no need for it now
				// therefore increment it for the next number
				prevind = prevind + 1;
				prevmax = ar[prevind];
			}
			c++;  // pivot's final location (depends on count of items smaller than pivot)
		}
		else if (prevind < 0) {
			// init first larger than pivot element
			// it may be swapped out later (above block)
			prevmax = ar[i];
			prevind = i;
		}
	}

	if (prevind > -1){ // if some swaps were done
		ar[ar_size-1] = ar[c];
		ar[c] = piv; // swap pivot to its correct position
	}

	if (ar_size > 2){
		if (c != 0)
			quicksort(c, &ar[0]); // recursively quicksort left partition
		if (ar_size-c-1 != 0)
			quicksort(ar_size-c-1, &ar[c+1]); // right partition
	}
}

int main() {
	int ar_size = 4, i;
	int a[4] = {2, 3, 0, 4};
	quicksort(ar_size, a);

	for (i=0; i<ar_size; i++){
		printf("%d\n", a[i]);
	}
	return 0;
}
