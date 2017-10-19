#include<iostream>
using namespace std;
int binarySearchIterative(int array[], int start, int end, int find)
{
    while(end >= start)
    {
	int mid = start + (end - start)/2;

	if(array[mid] == find)
	    return mid;

	else if(array[mid] < find)
	    start = mid + 1;

	else
	    end = mid - 1;
    }
    return -1;
}

int binarySearchRecursive(int array[], int start, int end, int find)
{
    if(end >= start)
    {
	int mid = start + (end - start)/2;

	if(array[mid] == find)
	    return mid;

	else if(array[mid] > find)
	    return binarySearchRecursive(array, start, mid - 1, find);
	
	else
	    return binarySearchRecursive(array, mid + 1, end, find);
    }
    return -1;
}

int main()
{
    int array[] = { 1, 2, 3, 4, 5, 6, 11, 23, 25, 66, 88, 99, 113 };
    int end = sizeof(array)/sizeof(array[0]);
    cout<<binarySearchIterative(array,0,end,1)<<'\n'<<binarySearchRecursive(array,0,end,1)<<'\n';
    cout<<binarySearchIterative(array,0,end,0)<<'\n'<<binarySearchRecursive(array,0,end,0)<<'\n';
    return 1;
}

