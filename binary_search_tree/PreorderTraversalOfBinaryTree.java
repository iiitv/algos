/*
 * Java Program to traverse a binary tree using PreOrder traversal. 
 * In PreOrder the node value is printed first, followed by visit
 * to left and right subtree. 
 * input:
 *     A
 *    / \
 *   B   E
 *  / \   \
 * C   D   F
 * 
 * output: A B C D E F 
 */

public class Main {

  public static void main(String[] args) throws Exception {

    // construct the binary tree given in question
    BinaryTree bt = new BinaryTree();
    BinaryTree.TreeNode root = new BinaryTree.TreeNode("A");
    bt.root = root;
    bt.root.left = new BinaryTree.TreeNode("B");
    bt.root.left.left = new BinaryTree.TreeNode("C");

    bt.root.left.right = new BinaryTree.TreeNode("D");
    bt.root.right = new BinaryTree.TreeNode("E");
    bt.root.right.right = new BinaryTree.TreeNode("F");

    // visitng nodes in preOrder traversal
    System.out.println("printing nodes of a binary tree in preOrder using recursion");
    bt.preOrder();

  }

}

class BinaryTree {
  static class TreeNode {
    String data;
    TreeNode left, right;

    TreeNode(String value) {
      this.data = value;
      left = right = null;
    }

    boolean isLeaf() {
      return left == null ? right == null : false;
    }

  }

  // root of binary tree
  TreeNode root;

  /**
   * Java method to print tree nodes in PreOrder traversal
   */
  public void preOrder() {
    preOrder(root);
  }

  /**
   * traverse the binary tree in PreOrder
   * @param node - starting node, root
   */
  private void preOrder(TreeNode node) {
    if (node == null) {
      return;
    }
    System.out.printf("%s ", node.data);
    preOrder(node.left);
    preOrder(node.right);
  }

}
