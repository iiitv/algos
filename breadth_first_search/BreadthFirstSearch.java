import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Set;

//Generic type BreadthFirstSearch implementation
public class BreadthFirstSearch<T> {
    // HasMap  of lists for Adjacency List Representation
    public HashMap<T, ArrayList<T>> adj = new HashMap<T, ArrayList<T>> ();
    //Function to add an edge
    public void addEdges (T source, T destination) {
        if (adj.containsKey (source)) {
            // update the adj-list
            ArrayList<T> list = (ArrayList<T>) adj.get (source);
            list.add (destination);
            adj.put (source, list);
        } else {
            // init the adj-list
            ArrayList<T> list = new ArrayList<> ();
            list.add (destination);
            adj.put (source, list);
        }
    }
    
    // BreadthFirstSearch search function with return path in a list
    public ArrayList<T> breadthFirstSearch (T source, T destination) {
        ArrayList<T> bfsPath = new ArrayList<> ();
        // Mark the current node as visited
        Set<T> visited = new HashSet<> ();
        //using the queue concept
        ArrayList<T> queue = new ArrayList<>();
        queue.add (source);
        bfsPath.add (source);
        visited.add (source);
        int flag = 0;
        while (!queue.isEmpty()) {
            source = queue.get (0);
            queue.remove (0);
            ArrayList<T> temp = new ArrayList<>();
            if (adj.containsKey(source) && adj.get(source).size() > 0) {
                temp.addAll (adj.get (source));
            }
            for (int i = 0; i < temp.size(); i++) {
                if (!visited.contains(temp.get(i))) {
                    bfsPath.add(temp.get(i));
                    if (temp.get(i) == destination){
                        flag = 1;
                        break;
                    }
                    queue.add(temp.get(i));
                    visited.add(temp.get(i));
                }
            }
            if (flag == 1) {
                break;
            }
        }
        if (flag == 0) {
            return null;
        }
        //return the list
        return bfsPath;
    }

    public static void main (String[] args) {
        BreadthFirstSearch<String> obj = new BreadthFirstSearch<> ();
        obj.addEdges ("A", "B");
        obj.addEdges ("A", "D");
        obj.addEdges ("B", "C");
        obj.addEdges ("C", "D");
        ArrayList<String> path = new ArrayList<> ();
        // find the path form source and destination
        path = obj.breadthFirstSearch ("A", "E");
        if (path != null) {
            System.out.println (path);
        }else {
            System.out.println("Path not found");
        }
    }
}
