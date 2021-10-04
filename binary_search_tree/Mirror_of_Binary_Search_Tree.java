package Binarytree;


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

class BST_mirror{
    Node root;
    BST_mirror()
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
    Node mirror()
    {
        return mirrorify(root);
    }
    Node mirrorify(Node node)
    {
        if(node == null)
            return null;
        // now in each step we have to create a new node and replace left right elem of old root node with new node's right left
        Node mirror_temp = new Node(node.data);
        mirror_temp.left = mirrorify(node.right);
        mirror_temp.right = mirrorify(node.left);
        return mirror_temp;
    }
}

public class mirror_Tree {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        BST_mirror obj = new BST_mirror();

        obj.addNode(9);
        obj.addNode(6);
        obj.addNode(8);
        obj.addNode(7);
        obj.addNode(13);
        obj.addNode(17);
        obj.addNode(19);
        System.out.println("Inorder of original Tree");
        obj.inorder(obj.root);

        System.out.println();
        System.out.println("Inorder of original Tree");
        Node mirror_node;
        mirror_node = obj.mirror();
        obj.inorder(mirror_node);

    }
}
