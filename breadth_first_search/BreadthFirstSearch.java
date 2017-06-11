import java.util.*;

public class BreadthFirstSearch <T> {

    // HasMap  of lists for Adjacency List Representation
    public HashMap<Integer, ArrayList<T>> adj;

    //Function to add an edge into the breadthFirstTraversal
    private void addEdge(int source, T destination) {
        adj.get (source).add (destination);
    }

    public ArrayList breadthFirstSearch(T source, T destination) {
        // false by default in java)
        ArrayList arrayList = new ArrayList();
        Set<T> visited = new HashSet();
        // Mark the current node as visited
        visited.add(source);
        ArrayList<T> queue = new ArrayList<> ();
        queue.add(source);
        while (queue.size() != 0) {
            source = queue.remove(0);
            arrayList.add(source);
            Iterator<T> i = adj.get(source).listIterator();
            int flag = 0;
            while (i.hasNext()) {
                T n = i.next();
                if (n == destination) {
                    arrayList.add(n);
                    flag = 1;
                    break;
                }
                if (!visited.contains(n)) {
                    visited.add(n);    // mark as visited.
                    queue.add(n);
                }
            }
            if (flag == 1) {
                break;
            }
        }
        return arrayList;
    }
    //init edges
    public void initEdges(int n) {
        adj = new HashMap<Integer, ArrayList<T>>();
        for (int i = 0; i < n; i++) {
            adj.put (i, new ArrayList<> ());
        }
    }

    public static void main(String[] args) {

        BreadthFirstSearch<Integer> obj = new BreadthFirstSearch<> ();
        obj.initEdges(4);
        obj.addEdge(0, 1);
        obj.addEdge(0, 3);
        obj.addEdge(1, 2);
        obj.addEdge(2, 1);
        obj.addEdge(2, 3);
        System.out.println("Breadth First Search starting from source to destination");
        ArrayList arrayList = obj.breadthFirstSearch(1,3);
        System.out.println(arrayList);
    }
}
