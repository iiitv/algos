package Binarytree;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

class Node{
    int data;
    Node left;
    Node right;
    Node(int element)
    {
        this.data = element;
        this.left = this.right = null;
    }
}

class BST{
    Node root;
    BST()
    {
        root = null;
    }
    void addNode(int element)
    {
        root = add(root,element);
    }
    Node add(Node node, int element)
    {
        if(node == null)
            return new Node(element);
        if(element<=node.data)
            node.left = add(node.left,element);
        else
        if(element>node.data)
            node.right = add(node.right,element);

        return node;
    }

    void inorder(Node root)
    {
        if(root == null)
            return;
        inorder(root.left);
        System.out.print(root.data+" ");
        inorder(root.right);
    }
        
        ArrayList<Integer> leftView(Node node)
        {
            ArrayList<Integer> al = new ArrayList<>();

            Queue<Node> q = new LinkedList<>();
            q.add(node);
            while(!q.isEmpty())
            {
                int n = q.size();
                for(int i=1;i<=n;i++)
                {
                    Node temp = q.poll();
                    if(i==1) {
                        al.add(temp.data);
                    }
                    if(temp.left!=null)
                        q.add(temp.left);
                    if(temp.right!=null)
                        q.add(temp.right);

                }
            }
            return al;
        }
}

public class Left_View {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        BST obj = new BST();

        obj.addNode(9);
        obj.addNode(6);
        obj.addNode(5);
        obj.addNode(8);
        obj.addNode(7);
        obj.addNode(13);
        obj.addNode(17);
        obj.addNode(19);
        System.out.println("Inorder of entered Tree is: ");
        obj.inorder(obj.root);
        ArrayList<Integer> al = new ArrayList<>();
        al = obj.leftView(obj.root);
        System.out.println("\nLeft View of this tree is: "+al);
    }
}
