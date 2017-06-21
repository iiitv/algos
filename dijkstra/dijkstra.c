/*
 *  Following implementation of dijsktra's algorithm prints the minimum distance from given source to destination using adjacency matrix.
 *  Time complexity : O(V^2).
 *  Space Complexity : O(V).
 */

#include <stdio.h>
#include <limits.h>	// For using INT_MAX
#include <stdbool.h>	// bool datatype
#include <string.h>	// for using memset()

#define VERTICES 8
#define INFINITY INT_MAX

// This function will find the minimum distance from the unselected vertices
int minimum_distance(const int min_distances[], const bool shortest_paths[]) {
	int i;
	int minimum = INFINITY, index;
	for (i = 0; i < VERTICES; ++i) {
		if (!shortest_paths[i] && min_distances[i] <= minimum) {
			minimum = min_distances[i];
			index = i;
		}
	}
	return index;
}

//	This function returns the minimum distance from given source to destination
int dijkstra(const int graph[VERTICES][VERTICES], int souce, int destination) {
	int i, j;
	int min_distances[VERTICES];
	bool shortest_paths[VERTICES];
	memset(shortest_paths, false, VERTICES);
	for (i = 0; i < VERTICES; ++i) {
		min_distances[i] = INFINITY;	// Initiallt set all distances to INFINITY
	}
	min_distances[souce] = 0;	// Distance from source to itself is zero
	for (i = 0; i < VERTICES - 1; ++i) {
		int temp = minimum_distance(min_distances, shortest_paths);
		shortest_paths[temp] = true;
		for (j = 0; j < VERTICES; ++j) {
			if ((!shortest_paths[j]) && (graph[temp][j] != 0) && (min_distances[temp] != INFINITY) && (min_distances[temp] + graph[temp][j]) < min_distances[j]) {
				min_distances[j] = min_distances[temp] + graph[temp][j];
			}
		}
	}
	return min_distances[destination];
}

int main() {
	int source = 0;
	int destination = 4;
	const int graph[VERTICES][VERTICES] = {
		{0, 4, 0, 0, 0, 0, 0, 8},
		{4, 0, 8, 0, 0, 0, 0, 11},
		{0, 8, 0, 7, 0, 4, 0, 0},
		{0, 0, 7, 0, 9, 14, 0, 0},
		{0, 0, 0, 9, 0, 10, 0, 0},
		{0, 0, 4, 14, 10, 0, 2, 0},
		{0, 0, 0, 0, 0, 2, 0, 1},
		{8, 11, 0, 0, 0, 0, 1, 0},
	};
	printf("The minimum distance from %d to %d is %d\n", source, destination, dijkstra(graph, source, destination));
	return 0;
}
