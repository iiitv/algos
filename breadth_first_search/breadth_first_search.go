package main

import "fmt"

type Graph struct {
	adj map[string][]string
}

func NewGraph() *Graph {
	return &Graph{
		adj: make(map[string][]string),
	}
}

func (gr *Graph) AddEdges(source string, destination string) *Graph {
	if _, ok := gr.adj[source]; ok {
		gr.adj[source] = append(gr.adj[source], destination)
		if _, ok := gr.adj[destination]; !ok {
			gr.adj[destination] = []string{}
		}
	} else {
		gr.adj[source] = []string{destination}
	}
	return gr
}

func BreadthFirstSearch(graph *Graph, source string, destination string) []string {
	bfsPath := []string{source}
	queue := []string{source}
	visited := []string{source}
	flag := 0

	for len(queue) != 0 {
		source = queue[0]
		queue = queue[1:]
		temp := []string{}

		if contains(keys(graph.adj), source) && len(graph.adj[source]) > 0 {
			for _, node := range graph.adj[source] {
				temp = append(temp, node)
			}
		}

		for _, el := range temp {
			if !contains(visited, el) {
				bfsPath = append(bfsPath, el)
				if el == destination {
					flag = 1
					break
				}
				queue = append(queue, el)
				visited = append(visited, el)
			}
		}
		if flag == 1 {
			break
		}
	}
	if flag == 0 {
		return nil
	}

	return bfsPath
}

func keys(coll map[string][]string) []string {
	result := make([]string, len(coll))

	for key := range coll {
		result = append(result, key)
	}

	return result
}

func contains(list []string, item string) bool {
	for _, value := range list {
		if value == item {
			return true
		}
	}
	return false
}

func main() {
	graph := NewGraph()

	graph.AddEdges("A", "B")
	graph.AddEdges("A", "D")
	graph.AddEdges("B", "C")
	graph.AddEdges("C", "D")

	result := BreadthFirstSearch(graph, "A", "D")

	fmt.Printf("Result is `%s`", result)
}
