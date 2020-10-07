
// A Java program to check if a given Euler_Path_And_Cycle is Eulerian graph or not
//
import java.util.*;

public class Euler_Path_And_Cycle {
    // int n=10;
    public ArrayList<ArrayList<Integer>> adj;// array list of array list to represent undirected graph

    public void make(int n)// function to set the size of arraylist
    {
        adj = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adj.add(new ArrayList<>());
        }
    }

    public void dfs(int u, int vis[])// a recursive depth first search
    {
        vis[u] = 1;// visit the node
        for (int i : adj.get(u)) {
            if (vis[i] == 0)// if not visited
            {
                dfs(i, vis);// explore it
            }
        }
    }

    public int isConnected(int u, int vis[], int n)// to check whether the graph is connected or not
    {
        int i = 0;
        for (; i < n; i++)
            if (adj.get(i).size() != 0)// if node has no edges
                break;
        if (i == n)// if all the nodes are disconnected
            return 1;
        for (int j = 0; j < n; j++)
            vis[j] = 0;
        dfs(0, vis);
        for (int j = 0; j < n; j++)
            if (vis[i] == 0 && adj.get(i).size() > 0)// to check if the graph is not conncted
                return 0;
        return 1;// if graph is connected
    }

    public int isPath(int u, int vis[], int n)// to check whether euler path exist or not
    {
        int odd = 0;
        if (isConnected(u, vis, n) == 0)// to check connected or not
        {

            return 0;
        }
        for (int i = 0; i < n; i++) {
            if (adj.get(i).size() % 2 != 0)// to count the total number of nodes with odd degrees
                odd++;
        }

        if (odd > 2)// if graph is not eulerian
            return 0;
        if (odd == 2)// if graph has euler path
            return 1;
        return 2;// if graph has euler cylce
    }

    public static void main(String args[]) {
        int n;
        n = 5;
        Euler_Path_And_Cycle eg1 = new Euler_Path_And_Cycle();
        Euler_Path_And_Cycle eg2 = new Euler_Path_And_Cycle();

        eg1.make(10);
        int vis1[] = new int[10];// visited array

        eg1.adj.get(0).add(1);
        eg1.adj.get(1).add(2);
        eg1.adj.get(6).add(8);
        eg1.adj.get(8).add(6);
        eg1.adj.get(5).add(0);
        eg1.adj.get(0).add(5);
        eg1.adj.get(1).add(0);
        eg1.adj.get(0).add(1);

        if (eg1.isPath(0, vis1, n) == 0)
            System.out.println("Graph is not euler");
        else if (eg1.isPath(0, vis1, n) == 1)
            System.out.println("Graph has eular path");
        else
            System.out.println("Graph has eular cycle");

        eg2.make(12);

        eg2.adj.get(2).add(1);
        eg2.adj.get(1).add(2);
        eg2.adj.get(0).add(3);
        eg2.adj.get(3).add(0);
        eg2.adj.get(4).add(0);
        eg2.adj.get(0).add(4);

        int vis2[] = new int[12];// visited array

        if (eg2.isPath(0, vis2, n) == 0)
            System.out.println("Graph is not euler");
        else if (eg2.isPath(0, vis2, n) == 1)
            System.out.println("Graph has eular path");
        else
            System.out.println("Graph has eular cycle");

    }

}
