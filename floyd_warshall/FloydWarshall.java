import java.util.*;
import java.lang.*;
import java.io.*;


class FloydWarshall {
    final static int INF = 99999, V = 4;

    void floydWarshall(int graph[][]) {
        int dist[][] = new int[V][V];
        int i, j, k;

        // Initialize the Solution Matrix as Input Graph MAtrix
        for (i = 0; i < V; i++)
            for (j = 0; j < V; j++)
                dist[i][j] = graph[i][j];

        /*  Add all vertices one by one to the set of intermediate
         *  vertices.
         *
         *  Before start of a iteration, we have {0, 1, 2, .. k-1} as intermediate vertices.
         *
         *  After the end of a iteration, k is added to the set of intermediate vertices and the set
         *  becomes {0, 1, 2, .. k} 
         */
        for (k = 0; k < V; k++) {
            // Pick all vertices as source one by one
            for (i = 0; i < V; i++) {
                // Pick all vertices as destination  
                for (j = 0; j < V; j++) {
                    // If vertex k is on the shortest path from i to j, then update the value of dist[i][j]
                    if (dist[i][k] + dist[k][j] < dist[i][j]) {
                        dist[i][j] = dist[i][k] + dist[k][j];
                    }
                }
            }
        }

        // Print the shortest distance matrix
        printSolution(dist);
    }

    void printSolution(int dist[][]) {
        System.out.println("Solution Matrix for shortest path b/w each pair or vertices:");
        for (int i=0; i<V; ++i) {
            for (int j=0; j<V; ++j) {
                if (dist[i][j]==INF)
                    System.out.print("INF ");
                else
                    System.out.print(dist[i][j]+"   ");
            }
            System.out.println();
        }
    }
 
    public static void main (String[] args)
    {
        int graph[][] = { {0,   5,  INF, 10},
                          {INF, 0,   3, INF},
                          {INF, INF, 0,   1},
                          {INF, INF, INF, 0}
                        };
        FloydWarshall f = new FloydWarshall();
 
        // Print the solution
        f.floydWarshall(graph);
    }
}