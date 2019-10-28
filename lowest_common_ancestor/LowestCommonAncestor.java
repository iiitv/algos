/*
    The program determines the lowest common ancestor
    of two nodes in a tree. The class design for tree
    is implemented in the program.
*/

import java.util.HashSet;

//Class design for node of Tree
class Node {
    int value;  //Stores value of the node
    Node left;  //Stores address of left node
    Node right;  //Stores address of right node

    Node(int value) {  //Constructor
        this.value = value;
    }
}

class LowestCommonAncestor {

    //Returns the Lowest Common Ancestor of two nodes node1 and node2
    public static int findLowestCommonAncestor(int node1, int node2, int[] parent) {
        HashSet<Integer> path1 = new HashSet<>();	//Set stores the path from node1 to the root of tree in bottom-up manner

        //Storing the path from node1 to the root of tree	  
        path1.add(node1);
        while(parent[node1]!=0) {
            int parentNode = parent[node1];
            path1.add(parentNode);
            node1 = parent[node1];
        }

        /*   Traverse the path from node2 to the root of the tree in bottom up fashion
             If a node is found which is present in path1 then return
             it as an LCA of node1 and node2
        */
        if(path1.contains(node2)) {
            return node2;
        }
        while(parent[node2]!=0) {
            int parentNode = parent[node2];
            if(path1.contains(parentNode)) {
                return parentNode;
            }
            node2 = parent[node2];
        }
        return -1;
    }

    public static void main(String[] args) {
        //Initializing size of tree
        int size = 10;
        int[] parent = new int[10+1];  //Initializing the parent array
        //Creating root of the tree
        Node root = new Node(1);

        //Building tree
        root.left = new Node(5);
        parent[5] = 1;
		root.right = new Node(7);
        parent[7] = 1;
        root.left.left = new Node(2);
        parent[2] = 5; 
        root.left.right = new Node(3);
        parent[3] = 5;
        root.right.left = new Node(8);
        parent[8] = 7;
        root.right.right = new Node(9);
        parent[9] = 7;
        root.left.left.left = new Node(4);
        parent[4] = 2;
        root.left.left.right = new Node(6);
        parent[6] = 2;
        root.left.right.left = new Node(10);
        parent[10] = 3;

        System.out.println("Lowest Common Ancestor of node 6 and 10 is: "+findLowestCommonAncestor(6,10,parent));
        System.out.println("Lowest Common Ancestor of node 3 and 9 is: "+findLowestCommonAncestor(3,9,parent));
        System.out.println("Lowest Common Ancestor of node 4 and 6 is: "+findLowestCommonAncestor(4,6,parent));
    }
}
