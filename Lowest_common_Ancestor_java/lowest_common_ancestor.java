//code begins here
 public class Main {
	public static class TreeNode
	{
		int value;
		TreeNode left;
		TreeNode right;
		TreeNode(int value)
		{
			this.value=value;
		}
	}
 
	 public static TreeNode lowest_Common_Ancestor(TreeNode root, TreeNode node1, TreeNode node2) {
	     
         if(root==null)
            return null;
            
        if(root.value==node1.value || root.value==node2.value)
        {
            return root;
        }
        TreeNode left_node=lowest_Common_Ancestor(root.left,node1,node2);
        TreeNode right_node=lowest_Common_Ancestor(root.right,node1,node2);
        //from our root left and right we found this node1 and node2 which means root is the lowest ancestor hence return root
        if(left_node!=null && right_node!=null)
           return root;
           else
           {
               //here we are checking if nodes left is not null and we found node1 and node2 in the left subtree of node  therefore we will return nodes left otherwise right
               if(left_node!=null)
                   return left_node;
               else
                   return right_node;
           }
        
    }
	public static void main(String[] args)
	{
	    TreeNode root =new TreeNode(3);
		TreeNode node1=new TreeNode(5);
		TreeNode node2=new TreeNode(1);
		TreeNode node3=new TreeNode(6);
		TreeNode node4=new TreeNode(2);
		TreeNode node5=new TreeNode(0);
		TreeNode node6=new TreeNode(8);
		TreeNode node7=new TreeNode(7);
		TreeNode node8=new TreeNode(4);
		TreeNode node9=new TreeNode(0);
        TreeNode node10=new TreeNode(0);
        TreeNode node11=new TreeNode(0);
        TreeNode node12=new TreeNode(0);
		/*
             3
            /  \
           5    1
          / \  / \
         6  2  0  8
           / \
          7   4

*/ // below we are making this binary tree
		root.left=node1;
		root.right=node2;
 
		node1.left=node3;
		node1.right=node4;
		
		node2.left=node5;
		node2.right=node6;
        
        node3.left=null;
		node3.right=null;
 
		node3.left=node7;
		node3.right=node8;
		
		node5.left=null;
		node5.right=null;
		
		node6.left=null;
		node6.right=null;
		
		node7.left=null;
		node7.right=null;
		
		node8.left=null;
		node8.right=null;
		
		node9.left=null;
		node9.right=null;
	
		System.out.println("Lowest common ancestor for node 5 and 1 ");
		System.out.println(lowest_Common_Ancestor(root,node1,node8).value);
	}
}
