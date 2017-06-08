import java.util.Scanner;
import java.util.NoSuchElementException;
import java.util.InputMismatchException;

public class AvlTree {

	public static void main(String[] args) {
		AVL avl = new AVL();
		Scanner inp = new Scanner(System.in);
		while (true) {
			try {
				System.out.println("\nTo insert an element Enter 1");
				System.out.println("To delete an element Enter 2");
				System.out.println("To print AVL tree preorder Enter 3");
				System.out.println("To EXIT Enter 4");
				int a = inp.nextInt();
				switch (a) {
				case 1:
					int in = inp.nextInt();
					avl.insert(in);
					break;
				case 2:
					int d = inp.nextInt();
					avl.del(d);
					break;
				case 3:
					if (avl.isEmpty()) {
						System.out.println("null");
					} else {
						avl.prntIn(avl.root);
						System.out.println(" ");
					}
					break;
				case 4:
					break;
				default:
					System.out.println("Sorry input number is not valid ");
					break;
				}
				if (a == 4) {
					break;
				}
			} catch (InputMismatchException e) {
				System.out.println("Input not valid!!!\nplease Integers numbers only");
				break;
			}

		}
	}
}

class AVL {
	public NodeAVL root = null;

	public void insert(int data) {
		// call these method when you wanna insert an element in the tree;
		if (root == null) {
			root = new NodeAVL(data);
		} else
			root = insert(root, data);
	}

	private NodeAVL insert(NodeAVL node, int data) {
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

	public NodeAVL rotateLR(NodeAVL node) {
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

	public NodeAVL rotateRL(NodeAVL node) {
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

	public NodeAVL rotateLL(NodeAVL node) {
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

	public NodeAVL rotateRR(NodeAVL node) {
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

	public NodeAVL isRotate(NodeAVL node) {
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

	public void del(int data) {
		// we call these method to delete the node if its exist
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
					dta = go(temp);
					root.data = dta;
				}
				if (root.right == null)
					root.hRight = 0;
				else
					root.hRight = Math.max(root.right.hLeft, root.right.hLeft);
				root = isRotate(root);
			}
		} else
			del(root, data);
	}

	private void del(NodeAVL node, int data) {
		// These is the method to delete node if it exist
		// Otherwise it throws an exception
		if (node.right == null && node.left == null) {
			throw new NoSuchElementException("element you wanna delete not exist");
		}
		if (node.right != null && node.right.data == data) {
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
					del.data = go(temp);
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
				del.data = go(temp);
				del.hRight = Math.max(del.right.hLeft, del.right.hRight);
			}
		} else if (node.data > data) {
			del(node.left, data);
			if (node.left == null)
				node.hLeft = 0;
			else
				node.hLeft = Math.max(node.left.hLeft, node.left.hRight) + 1;
		} else if (node.data < data) {
			del(node.right, data);
			if (node.right == null)
				node.hRight = 0;
			else
				node.hRight = Math.max(node.right.hLeft, node.right.hRight) + 1;
		}
		node = isRotate(node);
	}

	public int go(NodeAVL node) {
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
		int data = go(node);
		if (node.left == null)
			node.hLeft = 0;
		else
			node.hLeft = Math.max(node.left.hLeft, node.left.hLeft);
		node = isRotate(node);
		return data;
	}
}

class NodeAVL {
	public int hLeft;
	public int hRight;
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
