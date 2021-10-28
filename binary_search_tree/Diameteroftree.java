

class Node {
    int data;
    Node left;
    Node right;
    Node(int data) {
        this.data = data;
        left = null;
        right = null;
    }
}

class Tree{
    Node root;
    Tree()
    {
        root=null;
    }
    void add(int element)
    {
        root = addNode(root,element);
    }
    Node addNode(Node node,int element)
    {
            if(node == null)
                return new Node(element);
            if(element<node.data)
                node.left = addNode(node.left,element);
            else
                if(element> node.data)
                    node.right = addNode(node.right,element);

            return node;
    }
    int height (Node root)
    {
        if(root==null)
            return 0;
        return Math.max(height(root.left),height(root.right))+1;
    }
    int diameter()
    {
        return diameter(root);
    }
    int diameter(Node root)
    {
        // base case if tree is empty
        if (root == null)
            return 0;

        // get the height of left and right sub-trees
        int lheight = height(root.left);
        int rheight = height(root.right);

        // get the diameter of left and right sub-trees
        int ldiameter = diameter(root.left);
        int rdiameter = diameter(root.right);

        /* Return max of following three
          1) Diameter of left subtree
          2) Diameter of right subtree
          3) Height of left subtree + height of right subtree + 1
         */
        // This return statement deals with 3 cases that which among the
        //current diameter, left diameter, right diameter is greatest
        // current diameter = left height + right height +1
        return Math.max(lheight + rheight + 1,
                Math.max(ldiameter, rdiameter));
    }
}
public class Diameteroftree {
    public static void main(String[] args) {

        Tree obj = new Tree();
        obj.add(4);
        obj.add(3);
        obj.add(2);
        obj.add(9);
        obj.add(6);
        obj.add(1);
        obj.add(12);
        obj.add(13);

        System.out.println(obj.diameter());

    }
}
