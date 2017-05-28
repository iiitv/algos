import java.util.HashSet;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.Set;

public class BreadthFirstSearch {

    // Array  of lists for Adjacency List Representation
    public static LinkedList<Integer>[] adj;

    //Function to add an edge into the breadthFirstTraversal
    private static void addEdge(int v, int w) {
        adj[v].add(w);
    }

    private static void breadthFirstTraversal(int v) {
        // false by default in java)
        Set<Integer> visited = new HashSet();
        // Mark the current node as visited
        visited.add(v);
        LinkedList<Integer> queue = new LinkedList<>();
        queue.add(v);
        while (queue.size() != 0) {
            v = queue.poll();
            System.out.println(v);
            Iterator<Integer> i = adj[v].listIterator();
            while (i.hasNext()) {
                int n = i.next();
                if (!visited.contains(n)) {
                    visited.add(n);
                    queue.add(n);
                }
            }
        }
    }

    public static void initEdges(int n) {
        adj = new LinkedList[n];
        for (int i = 0; i < n; ++i) {
            adj[i] = new LinkedList();
        }
    }

    public static void main(String[] args) {
        initEdges(4);
        addEdge(0, 1);
        addEdge(0, 3);
        addEdge(1, 2);
        addEdge(2, 1);
        addEdge(2, 3);
        addEdge(3, 3);
        System.out.println("Breadth First Traversal starting from vertex 0");
        breadthFirstTraversal(0);
    }
}

