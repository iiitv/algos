package project1;
//A Java program for Bellman-Ford's single source shortest path
//algorithm.
import java.util.*;
import java.lang.*;
import java.io.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
class Reader {
 static BufferedReader reader;
 static StringTokenizer tokenizer;

 /** call this method to initialize reader for InputStream */
 static void init(InputStream input) {
     reader = new BufferedReader(
                  new InputStreamReader(input) );
     tokenizer = new StringTokenizer("");
 }

 /** get next word */
 static String next() throws IOException {
     while ( ! tokenizer.hasMoreTokens() ) {
         //TODO add check for eof if necessary
         tokenizer = new StringTokenizer(
                reader.readLine() );
     }
     return tokenizer.nextToken();
 }

 static int nextInt() throws IOException {
     return Integer.parseInt( next() );
 }
 static Long nextLong() throws IOException {
     return  Long.parseLong( next() );
 }
 static double nextDouble() throws IOException {
     return Double.parseDouble( next() );
 }
}
//A class to represent a connected, directed and weighted graph
class Graph
{
 // A class to represent a weighted edge in graph
 class Edge {
     int src, dest, weight;
     Edge() {
         src = dest = weight = 0;
     }
 };

 int V, E;
 Edge edge[];

 // Creates a graph with V vertices and E edges
 Graph(int v, int e)
 {
     V = v;
     E = e;
     edge = new Edge[e];
     for (int i=0; i<e; ++i)
         edge[i] = new Edge();
 }

 // The main function that finds shortest distances from src
 // to all other vertices using Bellman-Ford algorithm.  The
 // function also detects negative weight cycle
 void BellmanFord(Graph graph,int src)
 {
     int V = graph.V, E = graph.E;
     int dist[] = new int[V];

     // Step 1: Initialize distances from src to all other
     // vertices as INFINITE
     for (int i=0; i<V; ++i)
         dist[i] = Integer.MAX_VALUE;
     dist[src] = 0;

     // Step 2: Relax all edges |V| - 1 times. A simple
     // shortest path from src to any other vertex can
     // have at-most |V| - 1 edges
     for (int i=1; i<V; ++i)
     {
         for (int j=0; j<E; ++j)
         {
             int u = graph.edge[j].src;
             int v = graph.edge[j].dest;
             int weight = graph.edge[j].weight;
             if (dist[u]!=Integer.MAX_VALUE &&
                 dist[u]+weight<dist[v])
                 dist[v]=dist[u]+weight;
         }
     }

     // Step 3: check for negative-weight cycles.  The above
     // step guarantees shortest distances if graph doesn't
     // contain negative weight cycle. If we get a shorter
     //  path, then there is a cycle.
     for (int j=0; j<E; ++j)
     {
         int u = graph.edge[j].src;
         int v = graph.edge[j].dest;
         int weight = graph.edge[j].weight;
         if (dist[u] != Integer.MAX_VALUE &&
             dist[u]+weight < dist[v])
           System.out.println("Graph contains negative weight cycle");
     }
     printArr(dist, V);
 }

 // A utility function used to print the solution
 void printArr(int dist[], int V)
 {
     System.out.println("Vertex   Distance from Source");
     for (int i=0; i<V; ++i)
         System.out.println(i+"\t\t"+dist[i]);
 }

}
//

public class bellmanford {
	public static void main(String[] args) throws Exception
	 {
	     int V;  // Number of vertices in graph
	     int E;  // Number of edges in graph
	     Reader.init(System.in);
	     E=Reader.nextInt();
	     V=Reader.nextInt();
	     Graph graph = new Graph(V, E);
	     for(int i=0;i<E;i++){
	       graph.edge[i].src=Reader.nextInt();
	       graph.edge[i].dest=Reader.nextInt();
	       graph.edge[i].weight=Reader.nextInt();
	     }
	     graph.BellmanFord(graph, 0);
	 }
}
