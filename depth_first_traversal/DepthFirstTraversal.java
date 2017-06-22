import java.util.HashSet;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.Set;
import java.util.ArrayList;


public class DepthFirstTraversal {

    // ArrayList for Adjacency List Representation
    public static ArrayList<LinkedList<Integer>> adj;

    // Function to add an edge into the DepthFirstTraversal
    private static void addEdge(int v, int w) {
        adj.get(v).add(w);
    }

    // A function used by DFS
    private static void depthFirstTraversal(int v, Set<Integer> visited) {
        // Mark the current node as visited
        visited.add(v);
        System.out.println(v);
        Iterator<Integer> i = adj.get(v).listIterator();
        while (i.hasNext()) {
            int n = i.next();
            if (!visited.contains(n)) {
                depthFirstTraversal(n, visited);
            }
        }
    }

    public static void dfs(int v) {
        // false by default in java)
        Set<Integer> visited = new HashSet<Integer>();
        // Call the recursive helper function to print DFS traversal
        depthFirstTraversal(v, visited);
    }

    public static void initEdges(int n) {
        adj = new ArrayList<LinkedList<Integer>>();
        for (int i = 0; i < n; ++i) {
            adj.add(new LinkedList<Integer>());
        }
    }

    public static void main(String[] args) {
        initEdges(4);
        addEdge(0, 1);
        addEdge(0, 2);
        addEdge(1, 2);
        addEdge(2, 0);
        addEdge(2, 3);
        addEdge(3, 0);
        System.out.println("Depth First Traversal starting from vertex 2");
        dfs(2);
    }
}
