/*
*  Following implementation of dijsktra's algorithm prints the minimum distance from given source to destination using adjacency matrix.
*  Time complexity : O(V^2).
*  Space Complexity : O(V).
*/

#include <stdio.h>
#include <limits.h>    // For using INT_MAX
#include <stdbool.h>    // bool datatype
#include <string.h>    // for using memset()

#define INFINITY INT_MAX

// This function will find the minimum distance from the unselected vertices
int minimum_distance(const int min_distances[], const bool shortest_paths[], int vertices) {
    int i;
    int minimum = INFINITY, index;
    for (i = 0; i < vertices; ++i) {
        if (!shortest_paths[i] && min_distances[i] <= minimum) {
            minimum = min_distances[i];
            index = i;
        }
    }
    return index;
}

//    This function returns the minimum distance from given source to destination
int dijkstra(int vertices, int *graph[vertices], int souce, int destination) {
    int i, j;
    int min_distances[vertices];
    bool shortest_paths[vertices];
    memset(shortest_paths, false, vertices);
    for (i = 0; i < vertices; ++i) {
        min_distances[i] = INFINITY;    // Initiallt set all distances to INFINITY
    }
    min_distances[souce] = 0;    // Distance from source to itself is zero
    for (i = 0; i < vertices - 1; ++i) {
        int temp = minimum_distance(min_distances, shortest_paths, vertices);
        shortest_paths[temp] = true;
        for (j = 0; j < vertices; ++j) {
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
    int vertices = 8;
    int **graph;
    memset(graph, 0, vertices * vertices);
    graph[0] = {0, 4, 0, 0, 0, 0, 0, 8};
    graph[1] = {4, 0, 8, 0, 0, 0, 0, 11};
    graph[2] = {0, 8, 0, 7, 0, 4, 0, 0};
    graph[3] = {0, 0, 7, 0, 9, 14, 0, 0};
    graph[4] = {0, 0, 0, 9, 0, 10, 0, 0};
    graph[5] = {0, 0, 4, 14, 10, 0, 2, 0};
    graph[6] = {0, 0, 0, 0, 0, 2, 0, 1};
    graph[7] = {8, 11, 0, 0, 0, 0, 1, 0};
    printf("The minimum distance from %d to %d is %d\n", source, destination, dijkstra(vertices, graph, source, destination));
    return 0;
}
