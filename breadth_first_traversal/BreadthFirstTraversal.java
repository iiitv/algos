import java.util.HashSet;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.Set;

public class BreadthFirstSearch {

    // Array  of lists for Adjacency List Representation
    public static LinkedList<Integer>[] adj;

    //Function to add an edge into the breadthFirstTraversal
    private static void addEdge(int source, int w) {
        adj[source].add(w);
    }

    private static void breadthFirstTraversal(int source, int destination) {
        // false by default in java)
        Set<Integer> visited = new HashSet();
        // Mark the current node as visited
        visited.add(source);
        LinkedList<Integer> queue = new LinkedList<>();
        queue.add(source);
        while (queue.size() != 0) {
            source = queue.poll();
            System.out.println(source);
            Iterator<Integer> i = adj[source].listIterator();
            int flag = 0;
            while (i.hasNext()) {
                int n = i.next();
                if (n == destination) {
                    System.out.println(n);
                    flag = 1;
                    break;
                }
                if (!visited.contains(n)) {
                    visited.add(n);
                    queue.add(n);
                }
            }
            if (flag == 1) {
                break;
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
        System.out.println("Breadth First Traversal starting from source to destination");
        breadthFirstTraversal(1,3);
    }
}
