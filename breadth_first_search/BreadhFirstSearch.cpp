#include <iostream>
#include <list>
using namespace std;

class Graph {
	int v;
	list<int> *adjlist;
	public :

	Graph(int V) {
		v = V;
		adjlist = new list<int>[V];
	}

	void addEdge (int source, int dest) {
		adjlist[source].push_back(dest);
	}

	void breadthFirstSearch (int source) {
		bool *visited = new bool[v];
		list<int> queue;

		visited[source] = true;
		queue.push_back(source);

		list<int>::iterator itr;
		while (!queue.empty()) {
			source = queue.front();
			queue.pop_front();
			cout<<source<<"->";

			for(itr = adjlist[source].begin(); itr != adjlist[source].end(); itr++) {
				if(!visited[*itr]) {
					visited[*itr] = true;
					queue.push_back(*itr);
				}
			}
		}
	}
} ;

int main () {
	Graph G(4);
	G.addEdge(0, 1);
	G.addEdge(0, 2);
	G.addEdge(1, 2);
	G.addEdge(2, 0);
	G.addEdge(2, 3);
	G.addEdge(3, 3);

	cout<<"BFS starting from vertex 2 is "<<endl;
	G.breadthFirstSearch(2);
	return 0;
}
