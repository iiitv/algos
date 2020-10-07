#include <bits/stdc++.h>
using namespace std;
#define INF 100000

struct Edge
{
    int src, dest, weight;
};

struct Graph
{
    int Vertices, Edges;
    Edge *edge;
};
struct Graph *createGraph(int Vertices, int Edges)
{
    struct Graph *graph = new Graph;
    graph->Edges = Edges;
    graph->Vertices = Vertices;
    graph->edge = new Edge[Edges];
    return graph;
};

// To print the minimum distances from the src
void printArray(int distanceFromSrc[], int Vertices, int Source)
{
    cout << "Minimum Distance from the node " << (Source + 1) << " is: -" << endl;
    for (int i = 0; i < Vertices; i++)
    {
        cout << "Node " << (i + 1) << " " << distanceFromSrc[i] << endl;
    }
}

void bellmanFordAlgo(struct Graph *graph, int src)
{
    int V = graph->Vertices;
    int E = graph->Edges;

    int distanceFromSrc[V];
    for (int i = 0; i < V; i++)
    {
        distanceFromSrc[i] = INF;
    }

    distanceFromSrc[src] = 0;

    for (int i = 0; i < V - 1; i++)
    {

        for (int j = 0; j < E; j++)
        {
            int currentEdgeSrc = graph->edge[j].src;
            int currentEdgeDest = graph->edge[j].dest;
            int currentEdgeWeight = graph->edge[j].weight;

            if (distanceFromSrc[currentEdgeSrc] != INF && (distanceFromSrc[currentEdgeSrc] + currentEdgeWeight) < distanceFromSrc[currentEdgeDest])
            {
                distanceFromSrc[currentEdgeDest] = distanceFromSrc[currentEdgeSrc] + currentEdgeWeight; // Relaxing
            }
        }
    }
    // Checking for a negative weight cycle
    for (int j = 0; j < E; j++)
    {
        int currentEdgeSrc = graph->edge[j].src;
        int currentEdgeDest = graph->edge[j].dest;
        int currentEdgeWeight = graph->edge[j].weight;
        if (distanceFromSrc[currentEdgeSrc] != INF && distanceFromSrc[currentEdgeSrc] + currentEdgeWeight < distanceFromSrc[currentEdgeDest])
        {
            cout << "Graph has negative weight cycle, Failed" << endl;
            return;
        }
    }

    printArray(distanceFromSrc, V, src);
}

int main()
{
    int Vertices = 7;
    int Edges = 10;

    struct Graph *graph = createGraph(Vertices, Edges);
    int src = 0;
    // Creating the graph
    graph->edge[0].src = 0;
    graph->edge[0].dest = 1;
    graph->edge[0].weight = 6;

    graph->edge[1].src = 0;
    graph->edge[1].dest = 2;
    graph->edge[1].weight = 5;

    graph->edge[2].src = 0;
    graph->edge[2].dest = 3;
    graph->edge[2].weight = 5;

    graph->edge[3].src = 3;
    graph->edge[3].dest = 2;
    graph->edge[3].weight = -2;

    graph->edge[4].src = 2;
    graph->edge[4].dest = 1;
    graph->edge[4].weight = -2;

    graph->edge[5].src = 1;
    graph->edge[5].dest = 4;
    graph->edge[5].weight = -1;

    graph->edge[6].src = 2;
    graph->edge[6].dest = 4;
    graph->edge[6].weight = 1;

    graph->edge[7].src = 3;
    graph->edge[7].dest = 5;
    graph->edge[7].weight = -1;

    graph->edge[8].src = 5;
    graph->edge[8].dest = 6;
    graph->edge[8].weight = 3;

    graph->edge[9].src = 4;
    graph->edge[9].dest = 6;
    graph->edge[9].weight = 3;

    bellmanFordAlgo(graph, src);
}