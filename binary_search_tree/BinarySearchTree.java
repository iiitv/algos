import java.util.NoSuchElementException;

class Node {	// Node for Binary Search Tree
    public int data;
    public Node left;
    public Node right;

    public Node(int data) {	// Initializes node with given data and no chlid
        this.data = data;
        this.left = null;
        this.right = null;
    }
}

class BST {
    private Node root;	// Root of Binary Search Tree

    public BST() {	// Initializes empty BST
        root = null;
    }

    public BST(int data) {	// Initializes root of BST
        root = new Node(data);
    }

    public void insert(int data) {
        if (root == null) {
            root = new Node(data);	// Initialize root with the given data
            return;
        }
        Node newNode = new Node(data);	// Create Node for new entry
        Node iterator = root;	// Temp Node for iterating from root to leaf
        Node parent = null;	// To store the future parent of new node
        while (iterator != null) {
            parent = iterator;
            if (data <= iterator.data) {
                iterator = iterator.left;
            }
            else {
                iterator = iterator.right;
            }
        }
        if (data <= parent.data) {
            parent.left = newNode;
        }
        else {
            parent.right = newNode;
        }
    }

    public Node search(int data) {	// Returns the Node if element is found else will throw an Exception
        Node iterator = root;
        while (iterator != null) {
            if (iterator.data == data)
                return iterator;
            else if (data <= iterator.data)
                iterator = iterator.left;
            else
                iterator = iterator.right;
        }
        throw new NoSuchElementException("Element is not found in BST");
    }

    public boolean delete(int data) {	// Finds the parent of the node to be deleted.
        if (root == null) {
            throw new NoSuchElementException("Cannot perform delete operation, BST is empty");
        }
        Node iterator = root;
        Node parent = null;
        while (iterator != null) {
            if (data == iterator.data) {
                return deleteNode(data, parent);
            } else  {
                parent = iterator;
                if (data <= iterator.data)
                    iterator = iterator.left;
                else
                    iterator = iterator.right;
            }
        }
        throw new NoSuchElementException("Delete Unsuccessful! Element was not found in BST");
    }

    private boolean deleteNode(int data, Node parent) {
        Node child = null;
        boolean position = false;	// Indicates position of child wrt to parent, true is left child, false is right child
        if (data <= parent.data) {
            child = parent.left;
            position = true;
        }
        else
            child = parent.right;

        if (child.left == child.right) {	// Condition for leaf node
            child = null;
            if (position)
                parent.left = null;
            else
                parent.right = null;
            return true;
        } else if (child.right == null) {	// Condition for non-leaf with no right sub-tree
            if (position)
                parent.left = child.left;
            else
                parent.right = child.left;
            child.left = null;
            child = null;
            return true;
        } else if (child.left == null) {	// Condition for non-leaf with no left sub-tree
            if (position)
                parent.left = child.right;
            else
                parent.right = child.right;
            child.right = null;
            child = null;
            return true;
        }
        else {	// Conditon when Node has both subtree avaliable
            Node iterator = child.right;
            Node parentOfIterator = null;
            while(iterator.left != null) {	// Finding the leftmost child of right sub-tree
                parentOfIterator = iterator;
                iterator = iterator.left;
            }
            child.data = iterator.data;
            parentOfIterator.left = null;
            iterator = null;
            return true;
        }
    }

    public void printInOrder() {	// Function to call inorder printing using root
        if (root == null)
            throw new NoSuchElementException("Cannot print! BST is empty");
        print(root);
        System.out.println("");
    }

    private void print(Node iterator) {
        if (iterator != null) {
            print(iterator.left);
            System.out.print(iterator.data + " ");
            print(iterator.right);
        }
    }
}

public class BinarySearchTree {
    public static void main(String[] args) {
        // Created an empty tree
        BST tree = new BST();
        // Adding a few test entries
        tree.insert(10);
        tree.insert(9);
        tree.insert(3);
        tree.insert(12);
        tree.insert(14);
        tree.insert(7);
        tree.insert(6);
        tree.insert(11);
        tree.insert(1);
        tree.insert(2);
        // Test printing
        tree.printInOrder();
        // Deleting a valid node
        tree.delete(9);
        // Print again
        tree.printInOrder();
        // Searching an invalid node, same can be tested for delete as both use same logic
        // but with a slight different approach to find the node
        try {
            tree.search(4);
            System.out.println("Node was found successfully.");
        } catch (NoSuchElementException e) {
            System.out.println("Invalid Search");
        }
        try {
            tree.delete(9);
        } catch (NoSuchElementException  e) {
            System.out.println("Cannot delete, Node not present.");
        }
    }
}
