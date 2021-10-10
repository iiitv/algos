package Binarytree;

import java.util.*;

class Nodes{
    int data;
    Nodes left;
    Nodes right;
    Nodes(int element)
    {
        this.data = element;
        this.left = this.right = null;
    }
}

class BST_REV{
    Nodes root;
    BST_REV()
    {
        root = null;
    }
    void addNode(int element)
    {
        root = add(root,element);
    }
    Nodes add(Nodes node, int element)
    {
        if(node == null)
            return new Nodes(element);
        if(element<=node.data)
            node.left = add(node.left,element);
        else
        if(element>node.data)
            node.right = add(node.right,element);

        return node;
    }

    ArrayList<Integer> revLevelOrder()
    {
        return revLevelOrder(root);
    }
    ArrayList<Integer> levelOrder()
    {
        return levelOrder(root);
    }
    ArrayList <Integer> levelOrder(Nodes node)
    {
        ArrayList<Integer> al = new ArrayList<>();
        Queue<Nodes> q = new LinkedList<>();
        q.add(node);
        while(!q.isEmpty()) {
            Nodes temp = q.remove();
            al.add(temp.data);
            if(temp.left!=null)
                q.add(temp.left);
            if(temp.right!=null)
                q.add(temp.right);
        }
        return al;
    }
    ArrayList <Integer> revLevelOrder(Nodes node)
    {
        ArrayList<Integer> al = new ArrayList<>();
        Queue<Nodes> q = new LinkedList<>();
        q.add(node);
        while(!q.isEmpty()) {
            Nodes temp = q.remove();
            al.add(temp.data);
            if(temp.right!=null)
                q.add(temp.right);
            if(temp.left!=null)
                q.add(temp.left);
        }
        Collections.reverse(al);
        return al;
    }

}

public class revLevelOrder {
    public static void main(String[] args) {
    BST_REV obj = new BST_REV();
    obj.addNode(9);
    obj.addNode(6);
    obj.addNode(13);
    obj.addNode(5);
    obj.addNode(7);
    obj.addNode(11);
        System.out.println("Level order Traversal of the entered tree is: "+obj.levelOrder());
        System.out.println("Reverse Level order of the tree is: "+obj.revLevelOrder());
    }
}
