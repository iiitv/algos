/*
    The program determines whether a bidirected graph contains an Euler Cycle or Euler Path
    There are some conditions which are needed to be met for a graph to be eulerian.

    Conditions for graph to have an Eulerian Cycle:
        1) All the Vertices with a non-zero degree must be connected.
        2) All verices have an even degree.

    Conditions for graph to have an Eulerian Path:
        1) All the Vertices with a non-zero degree must be connected.
        2) Two vertices should have odd degree and rest of them should have even degree.
*/

import java.util.HashSet;
import java.util.HashMap;

class Graph {
    int size;
    HashMap<Integer,HashSet<Integer>> adjacencyList = new HashMap<>();

    Graph(int size) {    //Constructor
        this.size = size;
        makeAdjacencyList(size);
    }

    public void makeAdjacencyList(int size) {    //Building the initial adjacency list
        for(int i=1;i<=size;i++) {
            adjacencyList.put(i,new HashSet<Integer>());
        }
    }

    public void makeEdge(int u,int v) {    //Connecting node u and v with a bidirected edge
        HashSet<Integer> set1 = adjacencyList.get(u);
        set1.add(v);
        adjacencyList.put(u,set1);
        HashSet<Integer> set2 = adjacencyList.get(v);
        set2.add(u);
        adjacencyList.put(v,set2);
    }

    public void depthFirstSearch(int node, int[] visited) {    //Depth First Search in the Graph
        visited[node] = 1;
        HashSet<Integer> set = adjacencyList.get(node);
        for(int element : set) {
            if(visited[element] == 0) {
                depthFirstSearch(element,visited);
            }
        }
    }

    //Checking whether all the nodes with a positive degree are connected
    public boolean graphIsConnected() {
        int[] visited = new int[size+1];
        int source = 0;
        for(int i=1;i<=size;i++) {
            if(adjacencyList.get(i).size() > 0) {
                source = i;
                break;
            }
        }
        if(source == 0) {    //Return true if there is no edges in the graph
            return true;
        }
        depthFirstSearch(source,visited);
        for(int i=1;i<=size;i++) {
            if(adjacencyList.get(i).size()>0 && visited[i]==0) {
                return false;
            }
        }
        return true;
    }

    public void testForEulerianPathAndCycle() {
        if(!graphIsConnected()) {    //If all the nodes with a positive degree are not connected then graph is not eulerian
            System.out.println("Graph is not Eulerian");
            return;
        }
        int oddDegrees = 0;
        for(int i=1;i<=size;i++) {    //Checking number of nodes with odd degrees in the graph
            if(adjacencyList.get(i).size()%2 != 0) {
                oddDegrees++;
            }
        }
        if(oddDegrees>2) {
            System.out.println("Graph is not Eulerian");
            return;
        }
        if(oddDegrees == 0) {
            System.out.println("Graph has an Eulerian Cycle");
            return;
        }
        System.out.println("Graph has an Eulerian Path");
    }
}

class EulerCycleAndPath {
    public static void main(String[] args) {
        //Building bidirected graph
        Graph graph = new Graph(5);
        graph.makeEdge(1,2);
        graph.makeEdge(2,3);
        graph.makeEdge(3,1);
        graph.makeEdge(2,5);
        graph.makeEdge(5,4);
        graph.makeEdge(4,2);

        //Testing for a graph to have an Eulerian Path or Eulerian Cycle
        graph.testForEulerianPathAndCycle();
    }
}
