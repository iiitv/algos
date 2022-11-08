/* this code returns n-th fibonacci term calculated by recursion */
/* fibonacci series considered here is 0,1,1,2,3,5,8....... */
#include<stdio.h>

int fibo(int n){
	if(n < 1)
		return -1;
	if(n == 1)
		return 0;
	if(n == 2)
		return 1;
	else
		return fibo(n-1) + fibo(n-2);
}
int main(){
	int n, n_th_term;
	scanf("%d",&n);
	n_th_term = fibo(n);
	if(n_th_term == -1){
		printf("Invalid input:(\n");
		return -1;
	}
	printf("Required fibonacci term is = %d\n",fibo(n));
	return 0;
}
