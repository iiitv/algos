#include<iostream>

using namespace std;

int binary_search_iterative(int array[], int start, int end, int find)
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

int binary_search_recursive(int array[], int start, int end, int find)
{
	if(end >= start)
	{
		int mid = start + (end - start)/2;
		if(array[mid] == find)
			return mid;
		else if(array[mid] > find)
			return binary_search_recursive(array, start, mid - 1, find);
		else
			return binary_search_recursive(array, mid + 1, end, find);
	}
	return -1;
}

int main()
{
	int array[] = { 1, 2, 3, 4, 5, 6, 11, 23, 25, 66, 88, 99, 113 };
	int end = sizeof(array)/sizeof(array[0]);
	cout << binary_search_iterative(array,0,end,1) << '\n' << binary_search_recursive(array,0,end,1) << '\n';
	cout << binary_search_iterative(array,0,end,0) << '\n' << binary_search_recursive(array,0,end,0) << '\n';
	return 0;
}
