import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Set;

// Generic type BreadthFirstSearch implementation using the queue concept
// Time Complexity: O(V+E) where V is number of vertices in the graph and E is number of edges
public class BreadthFirstSearch<T> {
    // HashMap  of lists for Adjacency List Representation
    public HashMap<T, ArrayList<T>> adj = new HashMap<T, ArrayList<T>>();

    //Function to add an edge
    public void addEdges (T source, T destination) {
        if (adj.containsKey(source)) {
            // update the adj-list
            ArrayList<T> list = adj.get(source);
            list.add(destination);
            adj.put(source, list);
        } else {
            // init the adj-list
            ArrayList<T> list = new ArrayList<>();
            list.add(destination);
            adj.put(source, list);
        }
    }

    // BreadthFirstSearch search function with return path in a list
    public ArrayList<T> breadthFirstSearch (T source, T destination) {
        ArrayList<T> bfsPath = new ArrayList<>();
        // init the set for node visited
        Set<T> visited = new HashSet<>();
        // init list of queue
        ArrayList<T> queue = new ArrayList<>();
        queue.add(source);
        bfsPath.add(source);
        // mark as visited
        visited.add(source);
        int flag = 0;
        while (! queue.isEmpty()) {
            source = queue.get(0);
            queue.remove(0);
            ArrayList<T> temp = new ArrayList<>();
            if (adj.containsKey(source) && adj.get(source).size() > 0) {
                temp.addAll(adj.get(source));
            }
            for (int i = 0; i < temp.size(); i++) {
                if (! visited.contains(temp.get(i))) {
                    bfsPath.add(temp.get(i));
                    if (temp.get(i).equals(destination)) {
                        flag = 1;
                        break;
                    }
                    queue.add(temp.get(i));
                    // mark as visited
                    visited.add(temp.get(i));
                }
            }
            // break the while loop
            if (flag == 1) {
                break;
            }
        }
        // target node not found
        if (flag == 0) {
            return null;
        }
        // return the list
        return bfsPath;
    }

    public static void main (String[] args) {
        BreadthFirstSearch<String> obj = new BreadthFirstSearch<>();
        obj.addEdges("A", "B");
        obj.addEdges("A", "D");
        obj.addEdges("B", "C");
        obj.addEdges("C", "D");
        ArrayList<String> path = new ArrayList<>();
        // find the path form source and destination
        path = obj.breadthFirstSearch("A", "D");
        // print the path
        if (path != null) {
            System.out.println(path);
        } else {
            System.out.println("Path not found");
        }
    }
}
