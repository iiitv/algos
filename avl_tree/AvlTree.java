import java.util.NoSuchElementException;
import java.util.Random;

public class AvlTree {

    public static void main(String[] args) {
        AVL avl = new AVL();
        Random rand = new Random();
        int inp = 10;
        System.out.println(avl.isEmpty());
        for (int i = 0; i < inp; i++) {
            avl.root = avl.insert(avl.root, rand.nextInt(100));
        }
        avl.prntIn(avl.root);
        System.out.println(" ");
        System.out.println(avl.isEmpty());
        avl.delNode(avl.root,avl.root.data);
        avl.prntIn(avl.root);
        System.out.println(" ");
        try {
            avl.delNode(avl.root,1111);
        } catch(NoSuchElementException e) {
            System.out.println("Cannot delete element");
        }
    }
}

class AVL {
    public NodeAVL root;

    public AVL(){
        root = null;
    }

    public NodeAVL insert(NodeAVL node, int data) {
        // These method takes care of rotation needed after insertion
        if (node == null) {
            node = new NodeAVL(data);
            return node;
        } else {
            if (node.data > data) {
                node.left = insert(node.left, data);
                if (node.left == null)
                    node.hLeft = 0;
                else
                    node.hLeft = Math.max(node.left.hLeft, node.left.hRight) + 1;
            } else {
                node.right = insert(node.right, data);
                if (node.right == null)
                    node.hRight = 0;
                else
                    node.hRight = Math.max(node.right.hLeft, node.right.hRight) + 1;
            }
            node = isRotate(node);
        }
        return node;
    }

    private NodeAVL rotateLR(NodeAVL node) {
        NodeAVL sec = node.left;
        NodeAVL temp = sec.right;
        node.left = temp;
        sec.right = temp.left;
        temp.left = sec;
        node.left = temp.right;
        temp.right = node;
        if (node.left == null)
            node.hLeft = 0;
        else
            node.hLeft = Math.max(node.left.hLeft, node.left.hRight) + 1;
        if (sec.right == null)
            sec.hRight = 0;
        else
            sec.hRight = Math.max(sec.right.hLeft, sec.right.hRight) + 1;
        temp.hLeft = Math.max(sec.hLeft, sec.hRight) + 1;
        temp.hRight = Math.max(node.hLeft, node.hRight) + 1;
        return temp;
    }

    private NodeAVL rotateRL(NodeAVL node) {
        NodeAVL sec = node.right;
        NodeAVL temp = sec.left;
        node.right = temp;
        sec.left = temp.right;
        temp.right = sec;
        node.right = temp.left;
        temp.left = node;
        if (node.right == null)
            node.hRight = 0;
        else
            node.hRight = Math.max(node.right.hLeft, node.right.hRight) + 1;
        if (sec.left == null)
            sec.hLeft = 0;
        else
            sec.hLeft = Math.max(sec.left.hLeft, sec.left.hRight) + 1;
        temp.hRight = Math.max(sec.hLeft, sec.hRight) + 1;
        temp.hLeft = Math.max(node.hLeft, node.hRight) + 1;
        return temp;
    }

    private NodeAVL rotateLL(NodeAVL node) {
        NodeAVL temp = node.left;
        node.left = temp.right;
        temp.right = node;
        if (node.left == null)
            node.hLeft = 0;
        else
            node.hLeft = Math.max(node.left.hRight, node.left.hLeft) + 1;
        temp.hRight = Math.max(node.hRight, node.hLeft) + 1;
        return temp;
    }

    private NodeAVL rotateRR(NodeAVL node) {
        NodeAVL temp = node.right;
        node.right = temp.left;
        temp.left = node;
        if (node.right == null)
            node.hRight = 0;
        else
            node.hRight = Math.max(node.right.hRight, node.right.hLeft) + 1;
        temp.hLeft = Math.max(node.hRight, node.hLeft) + 1;
        return temp;
    }

    private NodeAVL isRotate(NodeAVL node) {
        // This Method see if there is nessesity for rotation and if
        // there is need, it'll do suitable rotation
        if (node.hRight - node.hLeft >= 2) {
            if (node.right.hRight - node.right.hLeft >= 1)
                node = rotateRR(node);
            else if (node.right.hRight - node.right.hLeft <= -1)
                node = rotateRL(node);
        } else if (node.hRight - node.hLeft <= -2) {
            if (node.left.hRight - node.left.hLeft <= -1)
                node = rotateLL(node);
            else if (node.left.hRight - node.left.hLeft >= 1)
                node = rotateLR(node);
        }
        return node;
    }

    public boolean isEmpty() {
        return root == null;
    }

    public void prntIn(NodeAVL node) {
        if (node == null)
            return;
        else if (node.left == null && node.right == null)
            System.out.print(node.data + " ");
        else {
            prntIn(node.left);
            System.out.print(node.data + " ");
            prntIn(node.right);
        }
    }

    public void delNode(NodeAVL node, int data) {
        // These is the method to delete node if it exist
        // Otherwise it throws an exception
        NodeAVL root = node;
        if (root == null) {
            throw new NoSuchElementException("AVL Tree is Empty!!!");
        }
        if (root.data == data) {
            NodeAVL temp = root.right;
            if (root.left == null && root.right == null)
                root = null;
            else if (root.left == null)
                root = root.right;
            else if (temp == null)
                root = root.left;
            else {
                int dta = 0;
                if (root.right.left == null) {
                    root.right.left = root.left;
                    root = root.right;
                } else {
                    dta = transverseLeftmost(temp);
                    root.data = dta;
                }
                if (root.right == null)
                    root.hRight = 0;
                else
                    root.hRight = Math.max(root.right.hLeft, root.right.hLeft);
                root = isRotate(root);
            }
        }
        else if (node.right == null && node.left == null) {
            throw new NoSuchElementException("element you wanna delete not exist");
        }
        else if (node.right != null && node.right.data == data) {
            NodeAVL del = node.right;
            if (del.right == null && del.left == null)
                node.right = null;
            else if (del.left == null)
                node.right = del.right;
            else if (del.right == null)
                node.right = del.left;
            else {
                NodeAVL temp = del.right;
                if (temp.left == null)
                    node.right = node.right.right;
                else
                    del.data = transverseLeftmost(temp);
                del.hRight = Math.max(del.right.hLeft, del.right.hRight);
            }
        } else if (node.left != null && node.left.data == data) {
            NodeAVL del = node.left;
            if (del.right == null && del.left == null)
                node.left = null;
            else if (del.left == null)
                node.left = del.right;
            else if (del.right == null)
                node.left = del.left;
            else {
                NodeAVL temp = del.right;
                if (temp.left == null)
                    node.left = node.left.right;
                del.data = transverseLeftmost(temp);
                del.hRight = Math.max(del.right.hLeft, del.right.hRight);
            }
        } else if (node.data > data) {
            delNode(node.left, data);
            if (node.left == null)
                node.hLeft = 0;
            else
                node.hLeft = Math.max(node.left.hLeft, node.left.hRight) + 1;
        } else if (node.data < data) {
            delNode(node.right, data);
            if (node.right == null)
                node.hRight = 0;
            else
                node.hRight = Math.max(node.right.hLeft, node.right.hRight) + 1;
        }
        node = isRotate(node);
    }

    private int transverseLeftmost(NodeAVL node) {
        // These method is special method which comes
        // in play when we have to delete a node
        // which have both childeren.
        if (node.left.left == null) {
            int data;
            if (node.left != null)
                data = node.left.data;
            else
                data = node.data;
            node.left = null;
            return data;
        }
        node = node.left;
        int data = transverseLeftmost(node);
        if (node.left == null)
            node.hLeft = 0;
        else
            node.hLeft = Math.max(node.left.hLeft, node.left.hLeft);
        node = isRotate(node);
        return data;
    }
}

class NodeAVL {
    protected int hLeft;
    protected int hRight;
    public int data;
    public NodeAVL left;
    public NodeAVL right;

    public NodeAVL(int data) {
        hLeft = 0;
        hRight = 0;
        this.data = data;
        left = null;
        right = null;
    }
}
