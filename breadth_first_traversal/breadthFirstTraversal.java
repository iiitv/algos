/*
    *Implementation of Breadth First Traversal in Graph
    *Time Complexity => O(v+e) v is no. of vertex and e is no. of edges
    *Space Complexity => O(v)
    *Adjacency List representation is used here    
*/

import java.util.*;
public class breadthFirstTraversal {

    public static void main(String[] args) {
        Graph g=new Graph(7);
        //1 Based indexing 
        g.addEdge(1, 2);
        g.addEdge(1, 6);
        g.addEdge(2, 3);
        g.addEdge(2, 5);
        g.addEdge(6, 3);
        g.addEdge(6, 5);
        g.addEdge(5, 4);
        g.addEdge(3, 4);
        System.out.println("BFS Traversal of the given graph is -");
        g.breadthFirstTraverse(1);
    }
    
}


class Graph
{
    private int V;   // No. of vertices
    private LinkedList<Integer> adj[]; //Adjacency Lists
    // Constructor
    public Graph(int v)
    {
        V = v;
        adj = new LinkedList[v];
        for (int i=0; i<v; ++i)
            adj[i] = new LinkedList();
    }
    // Function to add an edge into the graph

    public void addEdge(int v,int w)
    {
        adj[v].add(w);
    }
    // prints BFS traversal from s

    public void breadthFirstTraverse(int s)
    {
        // Mark all the vertices as not visited(By default
        // set as false)
        boolean visited[] = new boolean[V];
        // Creates a queue for BFS
        LinkedList<Integer> queue = new LinkedList<Integer>();
        // Mark the current node as visited and enqueue it
        visited[s]=true;
        queue.add(s);
        while (queue.size() != 0)
        {
            // Dequeue a vertex from queue and print it
            s = queue.poll();
            System.out.print(s+" ");
            // Get all adjacent vertices of the dequeued vertex s
            // If a adjacent has not been visited, then mark it
            // visited and enqueue it
            Iterator<Integer> i = adj[s].listIterator();
            while (i.hasNext())
            {
                int n = i.next();
                if (!visited[n])
                {
                    visited[n] = true;
                    queue.add(n);
                }
            }
        }
    }
}
