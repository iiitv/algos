#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int maxsum(int arr[], int arrlen)
{
	int sum=0,i,j,k,max=-32767;
	for(i=1;i<=arrlen;i++) //identifies size of subarray
	{
		for(j=0;j<=arrlen-i;j++) //identifies position at which subarray starts
		{
			for(k=j;k<(i+j);k++)	//adds the elements in the subarray		
			{
				if(k<=arrlen)
					sum+=arr[k]; 
			}
			if(sum>max) {max=sum;}
			sum=0;
		}
	}
	return max;
}
int main(int argc, char* argv[]) //taking the array as command line argument
{
	int i,m, j=0, pos=0;
	int a[1000];
	char val[16];
	char* n=argv[1];
	int k=strlen(argv[1]);

	for(i=0;i<6;i++)
	{
		val[i]=' ';
	}
	//separate numbers by space
	for(i=0;i<k;i++)
	{
		if(n[i]!=' ')
    	{
			while(n[i]!=' ' && i<k)
			{
				val[j]=n[i];
				j++;
				i++;
			}
			if(val[0]=='-')
			{
				a[pos]=-atoi(val+1); pos++;
			}
			else 
			{ 
				a[pos]=atoi(val); pos++;
			}
			for(m=0;m<7;m++)
			{
				val[m]=' ';
			}
			j=0;
	  	}
	}
	printf("%d",maxsum(a,pos));
	return 0;
}
