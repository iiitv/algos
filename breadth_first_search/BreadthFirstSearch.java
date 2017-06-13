import java.util.*;

public class BreadthFirstSearch <T> {

    // HasMap  of lists for Adjacency List Representation
    public HashMap<Integer, ArrayList<T>> adj;

    //Function to add an edge into the breadthFirstTraversal
    private void addEdge(int index, T destination) {
        adj.get(index).add(destination);
    }

    public ArrayList breadthFirstSearch(T index, T destination) {
        // false by default in java)
        ArrayList bfsPath = new ArrayList();
        Set<T> visited = new HashSet();
        // Mark the current node as visited
        visited.add(index);
        ArrayList<T> queue = new ArrayList<> ();
        queue.add(index);
        while (queue.size() != 0) {
            index = queue.remove(0);
            bfsPath.add(index);
            Iterator<T> i = adj.get(index).listIterator();
            // after reach the target node break out the all loop
            int flag = 0;
            while (i.hasNext()) {
                T n = i.next();
                if (n.equals(destination)) {
                    bfsPath.add(n);
                    flag = 1;
                    break;
                }
                if (!visited.contains(n)) {
                    visited.add(n);    // mark as visited.
                    queue.add(n);
                }
                if (flag == 1) {
                    break;
                }
            }
        }
        return bfsPath;
    }
    //init edges
    public void initEdges(int n) {
        adj = new HashMap<Integer, ArrayList<T>>();
        for (int i = 0; i < n; i++) {
            adj.put(i, new ArrayList<> ());
        }
    }

    public static void main(String[] args) {
        BreadthFirstSearch<Integer> obj = new BreadthFirstSearch<>();
        obj.initEdges(4);
        obj.addEdge(0, 1);
        obj.addEdge(0, 3);
        obj.addEdge(1, 2);
        obj.addEdge(2, 1);
        obj.addEdge(2, 3);
        System.out.println("Breadth First Search starting from index to destination");
        ArrayList bfsPath = obj.breadthFirstSearch(1, 3);
        System.out.println(bfsPath);
    }
}
