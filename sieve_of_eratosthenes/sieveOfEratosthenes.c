#include <stdio.h>
#include <string.h>
#include <math.h>     // for using square root 
#include <stdbool.h>  // to include bool datatype 

void sieveOfEratosthenes(int n){
	bool primes[n+1];
	int i, sqrt_n = sqrt(n)+1, j;
	
	memset(primes, true, sizeof(primes));
	primes[0] = false;
	primes[1] = false;

	for (i = 2; i < sqrt_n; i++){
		if (primes[i]){
			for (j = 2*i; j < n+1; j += i){
				primes[j] = false;
			}
		}
	}

	for (j = 2; j < n; j++){
		if (primes[j]){
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
