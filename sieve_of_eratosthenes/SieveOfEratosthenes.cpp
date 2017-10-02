//Sieve of Eratosthenes
using namespace std;
#include<iostream>
#include<cmath>
#include<vector>
int main()
{

		int b;
		scanf("%d",&b);
		vector<bool> sieve(b+1,true);
		for(int p=2; p<=sqrt(b); p++)
		{
			if(sieve[p]==true)
			{
				for(int i=p*2; i<=b; i+=p)
					sieve[i]=false;
			}
		}
		for(int r=2;r<=b;r++)
		{
			if(sieve[r]==true)
				{
					printf("%d",r);
					printf("\n");
				}
		}
}
