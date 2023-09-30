//Code to print nth Fibonacci Number
#include <iostream>
using namespace std;

long long int FibonacciNumber(long long int n)
{
	//Because first fibonacci number is 0 and second fibonacci number is 1.
	if (n == 1|| n==2)
	{
		return 1;
	}
	else
    {
        return FibonacciNumber(n-1)+FibonacciNumber(n-2);
    }
}

int main()
{
	long long int n;
	cout<<"Write the number of the Fibonacci number required :";
	cin>>n;
	if (n < 1)
	{
		cout<<"Number must be greater than 0";
	}
	else
	{
		long long int nth_Fib = FibonacciNumber(n);
		cout<<"Fibonacci Number is "<<nth_Fib ;
	}
	return 0;
}
