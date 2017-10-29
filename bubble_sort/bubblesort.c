#include <stdio.h>
void print_array(int arr[],int size)
{   
    printf("{");
    for(int i=0;i<size;i++)
    {
        printf(" %d",arr[i]);
        if(i < (size - 1))
                      printf(",");
        }
         printf("}\n");
}
int bubble_sort(int arr[],int size);

int main()
{
    int n;
    printf("How many elements ?\n");
    scanf("%d",&n);
    int array[n];
    for(int i=0;i<n;i++){
    printf("Element #%d\n",i);
    scanf("%d",&array[i]);
    }
    printf("Unsorted Array: ");
    print_array(array,n);
    int steps = bubble_sort(array,n);
    printf("Sorted Array: ");
    print_array(array,n);
    printf("Completed in %d steps.\n",steps);
    return 0;
}
int bubble_sort(int arr[],int size)
{
    int steps = 0;
    for(int i=0;i<size;i++)
    {
        for(int j=0;j<(size-i);j++)
        {
            if(arr[j] > arr[j+1])
            {
                int tmp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = tmp;
            }
            steps++;
        }
    }
    return steps;
}

