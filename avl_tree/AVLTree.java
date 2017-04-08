import java.util.*;


class AVLNode {
    public AVLNode right;
    public AVLNode left;
    public int data;
    public int height;
    AVLNode(int num) {
        data = num;
        left = null;
        right = null;
        height = 1; 
    }
    
    public void setLeft(AVLNode temp) {
        left = temp;
    }
    
    public void setRight(AVLNode temp) {
        right = temp;
    }
}

class AVL{
    private AVLNode root;
    public AVL() {
        root = null;
    }
    
    public int height(AVLNode root) {
        if(root == null)
            return 0; 
        return root.height; 
    }

    public boolean isEmpty() {
        return root == null;
    }
    
    public int getBalance(AVLNode root) {
        if(root == null)
            return 0;
        return height(root.left) - height(root.right); 
    }

    public void insert(int data) {
        root = insert(root, data);
    }
    
    private AVLNode rightRotate(AVLNode root) {
        AVLNode y = root.left;  
        AVLNode temp = y.right;
        y.right = root;
        root.left = temp;
        root.height= 1 + Math.max(height(root.left), height(root.right));    
        y.height = 1 + Math.max(height(y.left), height(y.right));   
        return y;
    } 
      
    private AVLNode leftRotate(AVLNode root) {
        AVLNode y = root.right;  
        AVLNode temp = y.left;
        y.left = root;
        root.right = temp;
        root.height= 1 + Math.max(height(root.left), height(root.right));    
        y.height = 1 + Math.max(height(y.left), height(y.right));   
        return y;
    } 
    
    private AVLNode insert(AVLNode root, int data) {
        if (root == null) {
            root = new AVLNode(data);
        }
        else{   
              if (data < root.data) { 
              root.left = insert(root.left, data);
            }
              else if(data > root.data) {
                root.right = insert(root.right, data);
            } 
              else
                return root;
        }
        root.height = 1 + Math.max(height(root.right), height(root.left));  
        int balance = height(root.left) - height(root.right); 
            
        if(balance > 1 && getBalance(root.left) >= 0)  //left-left case
            return rightRotate(root);
        
        else if(balance < -1 && getBalance(root.right) < 0)  //right-right case 
            return leftRotate(root);
        
        else if(balance > 1 && getBalance(root.right) < 0) {   //left-right case
            root.left = leftRotate(root.left);   
            return rightRotate(root);
        }
        
        else if(balance < -1 && getBalance(root.left) >= 0) {  //right-left case 
            root.right = rightRotate(root.right);
            return leftRotate(root);   
        } 
        return root;
    }
    
    public boolean search(int val) { 
        return search(root, val);
    }
    
    private boolean search(AVLNode root, int val) {
        boolean found = false;
        while ((root != null) && !found) {
            int rval = root.data;
            if (val < rval)
                root = root.left;
            else if (val > rval)
                root = root.right;
            else{
                found = true;
                break;
            }
            found = search(root, val);
        }
        return found;
    }
     
    public void inorder() {
        inorder(root);
    }
     
    private void inorder(AVLNode root) {
        if (root != null) {
            inorder(root.left);
            System.out.print(root.data + " ");
            inorder(root.right);
        }
    }
    public void delete(int k) {
        if (isEmpty())
            System.out.println("Tree Empty");
        else if (!search(k))
            System.out.println("Sorry " + k + " is not present");
        else{
            root = delete(root, k);
            System.out.println(k + " deleted from the tree");
        }
    }
    private AVLNode delete(AVLNode root, int k) {
        AVLNode p;
        AVLNode n;
        if (root.data == k) {
            AVLNode left; 
            AVLNode right;
            left = root.left;
            right = root.right;
            if (left == null && right == null)
                return null;
            else if (left == null)
                return right;
            else if (right == null)
                return left;
            else{
                p = right;
                while (p.left != null) {
                    p = p.left;
                }
                root.data = p.data; 
                root.right= delete(right, p.data);
            }
        }
        else if (k < root.data) {
            n = delete(root.left, k);
            root.setLeft(n);
        }
        else{
            n = delete(root.right, k);
            root.setRight(n);             
        }
            
        if(root == null)
            return root;
            root.height = 1 + Math.max(height(root.right), height(root.left));   
            int balance = height(root.left) - height(root.right); 
            
        if(balance > 1 && getBalance(root.left) >= 0)  //left-left case
            return rightRotate(root);
        
        else if(balance < -1 && getBalance(root.right) < 0)  //right-right case 
            return leftRotate(root);
        
        else if(balance > 1 && getBalance(root.right) < 0) {   //left-right case
            root.left = leftRotate(root.left);   
            return rightRotate(root);
        }
        else if(balance < -1 && getBalance(root.left) >= 0) {  //right-left case 
            root.right = rightRotate(root.right);
            return leftRotate(root);   
        } 
        return root;
    }
}

public class AvlTree{
    public static void main(String[] args) {
        AVL s = new AVL();        
        s.insert(10);
        s.insert(14);
        s.insert(5);
        s.insert(15);
        s.insert(16);
        s.insert(2);
        s.insert(1);
        s.insert(7);
        s.inorder();    // Printing in inorder
        System.out.println(s.search(7));    // Searching 7 
        s.delete(1);    // Deleting 1
        System.out.println(s.search(1));    // Searching 1
        s.inorder();    // Printing in inorder, again 
    }
}