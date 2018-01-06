package main

import (
	"fmt"
	"math"
)

// Prims finds a minimum spanning tree of given graph, starting at [0] and
// using Prim's algorithm.
func Prims(graph [][]int) []int {
	length := len(graph)
	// Stores the parent of each vertex
	parents := make([]int, length)
	// Stores key value of each vertex
	keys := make([]int, length)
	// true if already included in MST. Otherwise, false.
	visited := make([]bool, length)
	for i := 0; i < length; i++ {
		keys[i] = math.MaxInt32
	}

	// Make the first node the root one (no parent)
	keys[0] = 0
	parents[0] = -1

	for i := 1; i < length; i++ {
		// Find the minimum key
		u := minKey(keys, visited)
		visited[u] = true

		// Update the neighbours
		for j := 0; j < length; j++ {
			if graph[u][j] != 0 && !visited[j] && graph[u][j] < keys[j] {
				parents[j] = u
				keys[j] = graph[u][j]
			}
		}
	}
	return parents
}

func minKey(keys []int, visited []bool) int {
	min := math.MaxInt32
	minID := -1
	length := len(keys)
	for i := 0; i < length; i++ {
		if !visited[i] && keys[i] < min {
			min = keys[i]
			minID = i
		}
	}
	return minID
}

func main() {
	graph := [][]int{
		{0, 2, 0, 6, 0},
		{2, 0, 3, 8, 5},
		{0, 3, 0, 0, 7},
		{6, 8, 0, 0, 9},
		{0, 5, 7, 9, 0},
	}
	// Get parents of all the nodes
	parents := Prims(graph)

	// Print the Minimum Spanning Tree
	fmt.Println("Edge\tWeight")
	for i := 1; i < len(graph); i++ {
		fmt.Printf("%d - %d\t%d\n", parents[i], i, graph[i][parents[i]])
	}
}
