#include <bits/stdc++.h>
using namespace std;
void insertionSort(int array[], int size)
{
	int i = 0, j = 0, tempElement = 0, tempIndex = 0, flag = 0;
	for (i = 1; i < size; i++)
	{
		tempElement = array[i]; // taking an array element into tempElement
		for (j = i - 1; j >= 0; j--)
		{
			if (array[j] > tempElement)
				array[j + 1] = array[j];
			else
				flag = 1; //checking if we got the correct position of tempElement
			break;
		}
		if (flag == 1 || j == -1) //condition checking if we got correct position of tempElement or not
		{
			flag = 0;
			array[j + 1] = tempElement; //putting tempElement to it correct position
		}
	}
}
void display(int array[], int size)
{
	int i = 0;
	for (i = 0; i < size; i++)
		cout << array[i] << " "; //printing array
	cout << endl;
}
int main()
{
	int array[] = {5, 4, 233, 32, 1, 4, 34, 3, 23};
	int size = sizeof(array) / sizeof(array[0]);
	cout << "unsorted array is :" << endl;
	display(array, size);		//display unsorted array
	insertionSort(array, size); //calling insertion sort
	cout << "sorted array is :" << endl;
	display(array, size); //display the sorted array
}
