#include <stdio.h>
#include <math.h>     // for using square root 
#include <stdbool.h>  // to include bool datatype 

void sieveOfEratosthenes(int n){
	bool numbers[n+1];
	int i, sqrt_n = sqrt(n)+1, j;
	
	memset(numbers, true, sizeof(numbers));

	for (i = 2; i < sqrt_n; i++){
		if (numbers[i]){
			for (j = 2*i; j < n+1; j += i){
				numbers[j] = false;
			}
		}
	}

	for (j = 2; j < n; j++){
		if (numbers[j]){
			printf("%d ",j);
		}
	}

}

int main(){
	int n;
	scanf("%d",&n);
	sieveOfEratosthenes(n);
	return 0;
}
