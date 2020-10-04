#include <bits/stdc++.h>
using namespace std;
void insertionSort(int array[], int size)
{
	int i = 0, tempElement = 0, j = 0;
	for (i = 1; i < size; i++)
	{
		tempElement = array[i]; //Choosing element whose correct index to be found.
		j = i - 1;
		while (j >= 0 && array[j] > tempElement)
		{
			array[j + 1] = array[j]; //Shifting element one position right side untill we get correct position
			j = j - 1;
		}
		array[j + 1] = tempElement; // got the correct position for tempElement
	}
}
void display(int array[], int size)
{
	int i = 0;
	for (i = 0; i < size; i++)
		cout << array[i] << " ";
	cout << endl;
}
int main()
{
	int size;
	cout<<"Enter the size of the array :"<<endl;
	cin>>size; //size of the array
	int array[size];
	cout<<"Enter array elements"<<endl;
	for(int i=0;i<size;i++)
	cin>>array[i]; //taking input
	cout << "unsorted array is :" << endl;
	display(array, size); //display unsorted array
	insertionSort(array, size);
	cout << "sorted array is :" << endl;
	display(array, size); //display the sorted array
}
