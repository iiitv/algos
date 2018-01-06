#include<stdio.h>
#include<conio.h>
#include<math.h>

void Nqueen(int,int);
int place(int,int);
int x[10],sol;

void main()
{int n;
 clrscr();
 printf("\nEnter the number of queens: ");
 scanf("%d",&n);
 printf("\nThe solution for the %d Queen problem is:\n",n);
 Nqueen(1,n);
 printf("\nThe total number of solutions is %d",sol);
 getch();
}

void Nqueen(int k,int n)
{int i,j;
 for(i=1;i<=n;i++)
 {if(place(k,i)==1)
  {x[k]=i;
   if(k==n)
   {for(j=1;j<=n;j++)
     printf("%d\t",x[j]);

    printf("\n");
    sol++;
   }
   else Nqueen(k+1,n);
  }
 }
}

int place(int k,int i)
{int j;
 for(j=1;j<=k-1;j++)
 {if((x[j]==i) || (abs(x[j]-i)==abs(j-k)))
   return 0;
 }
 return 1;
}

/*OUTPUT

Enter the number of queens: 4

The solution for the 4 Queen problem is:
2       4       1       3
3       1       4       2

The total number of solutions is 2


Enter the number of queens: 8

The solution for the 8 Queen problem is:
7       4       2       8       6       1       3       5
7       5       3       1       6       8       2       4
8       2       4       1       7       5       3       6
8       2       5       3       1       7       4       6
8       3       1       6       2       5       7       4
8       4       1       3       6       2       7       5

The total number of solutions is 92
*/
