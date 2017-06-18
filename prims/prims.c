#include <stdio.h>
#include <string.h>
#include <limits.h>

#define SIZE 5

// This function finds the minimal spanning tree by Prim's Algorithm
void prims(int G[SIZE][SIZE], int *parent) {
	int select[SIZE], i, j, k;
	int v1 = 0, v2 = 0;
	for (i = 0; i < SIZE; ++i) {  // Initialize the selected vertices list
		select[i] = 0;
	}
	select[0] = 1;
	for (k = 1; k < SIZE; ++k) {
		int min_dist = INT_MAX;
		for (i = 0; i < SIZE; ++i) {  // Select an edge such that one vertex is selected and other is not and the edge
			for (j = 0; j < SIZE; ++j) {  // has the least weight.
				if (G[i][j] && ((select[i] && !select[j]) || (!select[i] && select[j]))) {
					if (G[i][j] < min_dist) {  //obtained edge with minimum wt
						min_dist = G[i][j];
						v1 = i;
						parent[j] = v1;
						v2 = j;  //picking up those vertices
					}
				}
			}
		}
		select[v1] = select[v2] = 1;
	}
}

int main() {
	int G[SIZE][SIZE] = {
		{0, 2, 0, 6, 0},
		{2, 0, 3, 8, 5},
		{0, 3, 0, 0, 7},
		{6, 8, 0, 0, 9},
		{0, 5, 7, 9, 0}};
	int i, j;
	int parent[SIZE];
	memset(parent, 0, SIZE);
	printf("Edge\tWeight\n");
	prims(G,parent);
	for (i = 1; i < SIZE; ++i) {
		printf("%d - %d\t%d \n", parent[i], i, G[i][parent[i]]);
	}
	return 0;
}
