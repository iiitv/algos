
// Applying Dijkstra Algorithm to find minimum distance

#include <bits/stdc++.h>
using namespace std;
#define Vertices 9 //Number of nodes in a graph
#define INF 1000   //Defining Ininity value of this graph

int minimumDistance(int distFromSrc[], int vistedNodes[])
{
    int minimumDistance = INF;
    int minimumIndex;
    for (int i = 0; i < Vertices; i++)
    {
        if (!vistedNodes[i] && minimumDistance >= distFromSrc[i]) //Finding the node with minimum distance which is not visted
        {
            minimumDistance = distFromSrc[i];
            minimumIndex = i;
        }
    }
    return minimumIndex; // Returning the minimum node
}

void printDistancesformSrc(int distFromSrc[], int src)
{
    cout << "Distances from " << src + 1 << " to all points are: -" << endl;
    for (int i = 0; i < Vertices; i++) 
    {
        cout <<"Node "<< i + 1 << " " << distFromSrc[i] << endl;// Printing the minimum distance from the source to all points
    }
}

void dijkstra(int graph[Vertices][Vertices], int src)
{
    int vistedNodes[Vertices] = {0}; //Initializing the visted nodes array to zero
                                    //No node is visted till now.
    int distFromSrc[Vertices]; // This array will store the minimum distance from the source
    
    for (int i = 0; i < Vertices; i++)
    {
        distFromSrc[i] = INF;
    }
    distFromSrc[src] = 0;

    int currentNode;

    for (int i = 0; i + 1 < Vertices; i++)
    {
        currentNode = minimumDistance(distFromSrc, vistedNodes);
        vistedNodes[currentNode] = 1;

        for (int j = 0; j < Vertices; j++)
        {
            if (!vistedNodes[j] && graph[currentNode][j] && distFromSrc[currentNode] != INF && distFromSrc[currentNode] + graph[currentNode][j] < distFromSrc[j])
            {
                distFromSrc[j] = distFromSrc[currentNode] + graph[currentNode][j];
            }
        }
    }

    printDistancesformSrc(distFromSrc, src);
}

int main()
{
    int startPoint = 0;
    //Creating a graph
    int graph[Vertices][Vertices] = {
        {0, 33, 2, 0, 0, 0, 0, 0, 0},
        {3, 0, 4, 30, 8, 0, 5, 0, 0},
        {2, 4, 0, 0, 20, 0, 0, 6, 0},
        {0, 7, 6, 0, 9, 1, 3, 0, 7},
        {0, 8, 5, 9, 0, 2, 0, 3, 0},
        {0, 0, 0, 1, 2, 0, 0, 0, 7},
        {0, 5, 0, 3, 0, 0, 0, 0, 6},
        {0, 0, 0, 7, 0, 7, 6, 0, 0},
        {0, 0, 0, 7, 0, 7, 6, 0, 0}};

    dijkstra(graph, startPoint);

    return 0;
}
