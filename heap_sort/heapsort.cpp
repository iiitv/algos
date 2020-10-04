#include <bits/stdc++.h>
using namespace std;

void swap(int array[], int index1, int index2) //swapping function wihout using third variable
{
	array[index1] = array[index1] + array[index2];
	array[index2] = array[index1] - array[index2];
	array[index1] = array[index1] - array[index2];
}
void heapify(int array[], int size, int index)
{
	int largest = index; //considering largest as root
	int left = 2 * index + 1;
	int right = 2 * index + 2;

	if (left < size && array[left] > array[largest]) //left child is larger then root
		largest = left;

	if (right < size && array[right] > array[largest]) //right child is larger then root
		largest = right;

	if (largest != index) //condition if largest is not root
	{
		swap(array, index, largest);
		heapify(array, size, largest);
	}
}
void heapsort(int array[], int size)
{

	for (int i = size / 2 - 1; i >= 0; i--) //Create heap from array rearrangement
		heapify(array, size, i);

	for (int i = size - 1; i > 0; i--) //move current root to end a step for Extract min process
	{

		swap(array, 0, i); //swap element

		heapify(array, i, 0); //excecuting heapify to bring all elements in correct position again
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
	display(array, size); //display the sorted array
}
