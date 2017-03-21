#include<stdio.h>
int main()
{

   int t,c[10000],p,cnt=0;
   scanf("%d",&t);
   while(t--)
   {
   	int n =0,k=0,i=0,amt=0;
   	scanf("%d%d",&n,&k);

    int a[n],b[n];
   	for(i=0;i<n;i++)
   	{
      scanf("%d%d",&a[i],&b[i]);
  	}

  	for(i=0;i<n;i++)
   	{
      if(a[i]>k)
      {
      	amt +=(a[i]-k)*b[i];
        k=0;
      }
      else
      {
      	k -=a[i];

      }

  	}
  	 c[t]=amt;
  	 cnt++;



   }

for(p=cnt-1;p>=0;p--)
   	{
      printf("%d\n",c[p]);
  	}
}
