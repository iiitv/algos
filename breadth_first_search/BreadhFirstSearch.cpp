// Program to print Breadth First Traversal of a Graph
// Time Complexity : O( no_of_vertices + no_of_edges)
// Space Complexity : O( no_of_vertices + no_of_edges)

#include <iostream>
#include <list>

using namespace std;

class Graph {
	int v;
	list<int> *adjlist;
	public :

	// Constructor Function
	Graph(int v) {
		this->v = v;
		adjlist = new list<int>[v];
	}

	// Function to add edge from source node to dest node
	void addEdge (int source, int dest) {
		adjlist[source].push_back(dest);
	}

	// Function to print Breadth First Traversal of graph starting from source node
	void breadthFirstSearch (int source) {
		bool *visited = new bool[v];
		list<int> node_queue;

		visited[source] = true;
		node_queue.push_back(source);

		list<int>::iterator itr;
		while (!node_queue.empty()) {
			source = node_queue.front();
			node_queue.pop_front();
			cout << source << "->";

			for(itr = adjlist[source].begin(); itr != adjlist[source].end(); ++itr) {
				if(!visited[*itr]) {
					visited[*itr] = true;
					node_queue.push_back(*itr);
				}
			}
		}
	}
};

int main () {
	Graph testGraph(4);
	testGraph.addEdge(0, 1);
	testGraph.addEdge(0, 2);
	testGraph.addEdge(1, 2);
	testGraph.addEdge(2, 0);
	testGraph.addEdge(2, 3);
	testGraph.addEdge(3, 3);

	cout << "BFS starting from vertex 2 is " << endl;
	testGraph.breadthFirstSearch(2);
	return 0;
}
