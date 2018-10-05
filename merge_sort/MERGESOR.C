#include <stdio.h>
#include <conio.h>
#define size 20
void merge(int[],int,int,int);
void merge_sort(int[],int,int);
void quick(int[],int,int);
int partition(int[],int,int);
int n,tc=0,pass=0;

void main()
{int arr[size],i,ch;
 clrscr();
 printf("\nEnter the number of elements in the array: ");
 scanf("%d",&n);
 printf("\nEnter the elements of the array: ");
 for(i=0;i<n;i++)
  scanf("%d", &arr[i]);

 printf("\n\tENTER TYPE OF SORT\n1.Merge Sort\n2.Quick Sort\n3.Exit\nEnter your choice: ");
 scanf("%d",&ch);

 switch(ch)
 {case 1: merge_sort(arr,0,n-1);
	  break;
  case 2: quick(arr,0,n-1);
	  break;
  case 3: exit(0);
 }
 printf("\nThe Total comparison is %d",tc);
 getch();
}

void merge(int arr[], int beg, int mid, int end)
{int i=beg,j=mid+1,index=beg,temp[size],k,count=0,m;
 pass++;
 while((i<=mid)&&(j<=end))
 {if(arr[i]<arr[j])
  {temp[index]=arr[i];
   i++;
  }
  else
  {temp[index]=arr[j];
   j++;
  }
  count++;
  index++;
 }
 if(i>mid)
 {while(j<=end)
  {temp[index]=arr[j];
   j++;
   index++;
  }
 }
 else
 {while(i<=mid)
  {temp[index]=arr[i];
   i++;
   index++;
  }
 }
 tc+=count;
 for(k=beg;k<index;k++)
  arr[k]=temp[k];

 printf("\n\nPass: %d\tCount: %d",pass,count);
 printf("\nThe sorted array is:");
 for(m=0;m<n;m++)
   printf("\t%d", arr[m]);
}

void merge_sort(int arr[], int beg, int end)
{int mid;
 if(beg<end)
 {mid=(beg+end)/2;
  merge_sort(arr,beg,mid);
  merge_sort(arr,mid+1,end);
  merge(arr,beg,mid,end);
 }
}

void quick(int a[],int lb,int ub)
{int p;
 if(lb>=ub)
 {return;
 }

 p=partition(a,lb,ub);
 quick(a,lb,p-1);
 quick(a,p+1,ub);
}

int partition(int a[],int down,int up)
{int i=down,j=up,pivot=a[down],count=0,m;
 int temp;
 pass++;
 while(i<j)
 {
  while(a[i]<pivot && i<=up)
   i++;

  while(pivot<a[j] && j>=down)
   j--;

  if(i<j)
  {temp=a[i];
   a[i]=a[j];
   a[j]=temp;
   count++;
   tc++;
  }
  if(count==0)
  {count=1;
   tc++;
  }

 }
 a[i]=a[j];
 a[j]=pivot;
 printf("\n\nPass: %d\tCount: %d",pass,count);
 printf("\nThe sorted array is:");
 for(m=0;m<n;m++)
  printf("\t%d", a[m]);

 return j;
}

/*OUTPUT
Enter the number of elements in the array: 4

Enter the elements of the array: 1 2 3 4

	ENTER TYPE OF SORT
1.Merge Sort
2.Quick Sort
3.Exit
Enter your choice: 1

Pass: 1 Count: 1
The sorted array is:    1       2       3       4

Pass: 2 Count: 1
The sorted array is:    1       2       3       4

Pass: 3 Count: 2
The sorted array is:    1       2       3       4

The Total comparison is 4

Enter the number of elements in the array: 4

Enter the elements of the array: 4 3 2 1

	ENTER TYPE OF SORT
1.Merge Sort
2.Quick Sort
3.Exit
Enter your choice: 1

Pass: 1 Count: 1
The sorted array is:    3       4       2       1

Pass: 2 Count: 1
The sorted array is:    3       4       1       2

Pass: 3 Count: 2
The sorted array is:    1       2       3       4

The Total comparison is 4

Enter the number of elements in the array: 4

Enter the elements of the array: 4 1 3 2

	ENTER TYPE OF SORT
1.Merge Sort
2.Quick Sort
3.Exit
Enter your choice: 1

Pass: 1 Count: 1
The sorted array is:    1       4       3       2

Pass: 2 Count: 1
The sorted array is:    1       4       2       3

Pass: 3 Count: 3
The sorted array is:    1       2       3       4

The Total comparison is 5

Enter the number of elements in the array: 4

Enter the elements of the array: 1 2 3 4

	ENTER TYPE OF SORT
1.Merge Sort
2.Quick Sort
3.Exit
Enter your choice: 2

Pass: 1 Count: 1
The sorted array is:    1       2       3       4

Pass: 2 Count: 1
The sorted array is:    1       2       3       4

Pass: 3 Count: 1
The sorted array is:    1       2       3       4

The Total comparison is 3

Enter the number of elements in the array: 4

Enter the elements of the array: 4 3 2 1

	ENTER TYPE OF SORT
1.Merge Sort
2.Quick Sort
3.Exit
Enter your choice: 2

Pass: 1 Count: 1
The sorted array is:    1       3       2       4

Pass: 2 Count: 1
The sorted array is:    1       3       2       4

Pass: 3 Count: 1
The sorted array is:    1       2       3       4

The Total comparison is 3

Enter the number of elements in the array: 4

Enter the elements of the array: 3 1 4 2

	ENTER TYPE OF SORT
1.Merge Sort
2.Quick Sort
3.Exit
Enter your choice: 2

Pass: 1 Count: 2                                                                
The sorted array is:    2       1       3       4                               
                                                                                
Pass: 2 Count: 1                                                                
The sorted array is:    1       2       3       4                               
                                                                                
The Total comparison is 3                                                       
