#include "stdio.h"


void quicksort(int ar_size, int *  ar) {
	int piv;
	piv = ar[ar_size-1];
	int i, temp, c=0;
	int prevmax, prevind=-1;

	for (i=0; i<ar_size-1; i++){
		if (ar[i] < piv){
			if ((prevind>-1) && (ar[i] < prevmax)){
				temp = ar[i];
				ar[i] = prevmax;
				ar[ prevind ] = temp;
				prevind = prevind+1;
				prevmax = ar[prevind];
			}
			c++;
		}
		else if (prevind<0) {
			prevmax = ar[i];
			prevind = i;
		}
	}

	if (prevind>-1){
		ar[ar_size-1] = ar[c];
		ar[c] = piv;
	}

	if (ar_size>2){
		if (c!=0)
			quicksort(c, &ar[0]);
		if (ar_size-c-1 != 0)
			quicksort(ar_size-c-1, &ar[c+1]);
	}
}

int main(){
	int ar_size = 4, i;
	int a[4];
	a[0] = 2; a[1] = 3; a[2] = 0; a[3] = 4;
	quicksort(ar_size, a);

	for (i=0; i<ar_size; i++){
		printf("%d\n", a[i]);
	}
	return 0;
}
