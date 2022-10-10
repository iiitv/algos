#include <stdio.h>
#include <stdlib.h>
int find(int a, int parent[]) // recursive function to find parent of a
{
	if (parent[a] == a) // if root itself is a parent
		return a;
	else
		return find(parent[a], parent); // to find the parent of the parent
}

void unionn(int a, int b, int parent[], int rank[]) // function to do unionn of a and b
{
	int a1 = find(a, parent); // to find parent of a
	int b1 = find(b, parent); // to find parent of b
	if (a1 == b1)			  // if both have same parent that is both are in same set
	{
		printf("both the elements are in same set\n");
		return;
	}
	if (rank[a1] > rank[b1]) // if height of parent of a is greater than height of parent of b
	{
		parent[b1] = a1;
	}
	else if (rank[a1] < rank[b1]) // if height of parent of b is greater than height of parent of a
	{
		parent[a1] = b1;
	}
	else // if height of both parent is same
	{
		parent[a1] = b1;
		rank[b1]++;
	}
}
int main()
{
	int n = 10;
	int parent[n];
	int rank[n];

	for (int i = 0; i < 10; i++)
		parent[i] = i; // in starting the node is itself the parent
	for (int i = 0; i < 10; i++)
		rank[i] = 1; // by default the rank of all nodes is 1

	unionn(3, 8, parent, rank); // 3 is friend of 8
	unionn(3, 6, parent, rank); // 3 is friend of 6
	printf("the parent of 8 is %d\n", find(8, parent));

	unionn(1, 9, parent, rank); // 1 is friend of 9
	unionn(2, 8, parent, rank); // 2 is friend of 8
	unionn(5, 8, parent, rank); // 5 is friend of 8

	unionn(2, 9, parent, rank); // 2 is friend of 9
	printf("the parent of 2 is %d\n", find(2, parent));
	printf("the parent of 8 is%d\n", find(8, parent));

	if (find(5, parent) == find(7, parent)) // to check whether 5 is friend of 7 or not
		printf("5 is a friend of 7\n");
	else
		printf("5 is not a friend of 7\n");
	if (find(3, parent) == find(1, parent)) // to check whether 3 is friend of 1 or not
		printf("3 is a friend of 1\n");
	else
		printf("3 is not a friend of 1\n");

	return 0;
}
