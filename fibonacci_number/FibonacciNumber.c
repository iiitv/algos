#include <stdio.h>

long long int FibonacciNumber(long long int n)
{
	//Because first fibonacci number is 0 and second fibonacci number is 1.
	if (n == 1 || n == 2)
	{
		return (n - 1);
	}
	else
	{
		//store last fibonacci number
		long long int a = 1;
		//store second last fibonacci number
		long long int b = 0;
		//store current fibonacci number
		long long int nth_Fib;
		for (long long int i = 3; i <= n; i++)
		{
			nth_Fib = a + b;
			b = a;
			a = nth_Fib;
		}
		return nth_Fib;
	}
}

int main()
{
	long long int n;
	printf("Enter a Number : ");
	scanf("%lli", &n);
	if (n < 1)
	{
		printf("Number must be greater than 0");
	}
	else
	{
		long long int nth_Fib = FibonacciNumber(n);
		printf("Fibonacci Number is %lli", nth_Fib);
	}
	return 0;
}
