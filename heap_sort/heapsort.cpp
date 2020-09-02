/*
 * The below code is for the implementation of Heap sort algorithm in CPP
 *  time comeplexity for sorting will be O(n*logn)
 *  n being the size of array.
 *  Space complexity in the belom implementation of heap sort algorithm is O(1)
 *
 */
#include <bits/stdc++.h>
using namespace std;
// swapping function wihout using third variable
void swap(int array[], int index1, int index2)
{
	array[index1] = array[index1] + array[index2];
	array[index2] = array[index1] - array[index2];
	array[index1] = array[index1] - array[index2];
}
void heapify(int array[], int size, int index)
{
	int largest = index; // considering largest as root
	int left = 2 * index + 1;
	int right = 2 * index + 2;
	// left child is larger then root
	if (left < size && array[left] > array[largest])
		largest = left;
	// right child is larger then root
	if (right < size && array[right] > array[largest])
		largest = right;
	//condition if largest is not root
	if (largest != index)
	{
		swap(array, index, largest);
		heapify(array, size, largest);
	}
}
void heapsort(int array[], int size)
{
	//Create heap from array rearrangement
	for (int i = size / 2 - 1; i >= 0; i--)
		heapify(array, size, i);
	// move current root to end a step for Extract min process
	for (int i = size - 1; i > 0; i--)
	{
		//swap element
		swap(array, 0, i);
		//excecuting heapify to bring all elements in correct position again
		heapify(array, i, 0);
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
	int array[] = {6, 3, 6, 343, 42, 1, 43, 35, 34, 43};
	int size = sizeof(array) / sizeof(array[0]);
	cout << "Unsorted array is :" << endl;
	display(array, size); //display the unsorted array
	heapsort(array, size);
	cout << "sorted array is :" << endl;
	display(array, size); // display the sorted array
						  /*
 *  for given input array
 *
 * output :
 *
 *  Unsorted array is :
 *  6 3 6 343 42 1 43 35 34 43
 *  sorted array is :
 *  1 3 6 6 34 35 42 43 43 343
 *
 */
}
