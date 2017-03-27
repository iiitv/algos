
package Test;

class NodeB{
	
	int data;
	NodeB left;
	NodeB right;
	public NodeB(int data){
		
		this.data=data;
		left=null;
		right=null;
	}
	public void setLeft(NodeB lft){
		left = lft;
	}
	public void setRight(NodeB rgt){
		right=rgt;
	}
	
	public NodeB getLeft(){
		return left;
	}
	public NodeB getRight(){
		return right;
	}
	public int getData(){
	
		return data;
	}
	
}
public class BST{
     NodeB root;
     NodeB max;
 /*  public BST(){
     	root=null;
     	}*/
     public boolean isEmpty(){
     	return root==null;
     }

	public void insert(int data){
		root=insert(root,data);
	}
	
	private NodeB insert(NodeB node,int data){
		if(node==null){
			node =new NodeB(data);
			
			if(max==null)
				max=node;
			else if(max.data<data)
				max=node;
			}
		else{
			if(node.data>=data){
				node.left=insert(node.left,data);
			}
			else{
				node.right=insert(node.right,data);
				}
		}
		
		return node;

	}
	public NodeB search(int ser){
	
		NodeB value=search(root,ser);
		return value;
	}
	private NodeB search(NodeB node, int ser){
		
		NodeB check=null;
		if(node==null){
			check=null;
			return check;
			}
		else if(node.data==ser){
		
			check= node;
			return check;
			}
		else if(node.data>ser){
			node=node.left;
			return search(node,ser);
			}
		else if(node.data<ser){
			node=node.right;
			return search(node,ser);
		}
		
	return check;
	}
	public void prntIn(NodeB node){
		if(node==null)
			return;
		else if(node.left==null&&node.right==null)
			System.out.print(node.data+" ");
		
		else{
			prntIn(node.left);
			System.out.print(node.data+" ");
			prntIn(node.right);
		}
		
	}
	public void del(int del ){
            NodeB temp=root;
            if(root.data==del){
                temp=temp.right;
                while(temp.left!=null)
                    temp=temp.left;
                temp.left=root.left;
                root=root.right;
            }
            else{
                while(temp!=null){
                    if(temp.data>del){
                        if(temp.left==null)
                            break;
                        else if(temp.left.data==del){
                             if(temp.left.left==null){
                                 temp.left=temp.left.right;
                             }
                             else if(temp.left.right==null){
                                 temp.left=temp.left.left;
                             }
                             else{
                                 NodeB t=temp.left.right;
                                 while(t.left!=null)
                                     t=t.left;
                                 t.left=temp.left.left;
                                 temp.left=temp.left.right;
                             }
                        }
                        else
                            temp=temp.left;
                        
                    }
                    else{
                         if(temp.data<del){
                        if(temp.right==null)
                            break;
                        else if(temp.right.data==del){
                             if(temp.right.left==null){
                                 temp.right=temp.right.right;
                             }
                             else if(temp.right.right==null){
                                 temp.right=temp.right.left;
                             }
                             else{
                                 NodeB t=temp.right.right;
                                 while(t.left!=null)
                                     t=t.left;
                                 t.left=temp.right.left;
                                 temp.right=temp.right.right;
                             }
                        }
                        else
                            temp=temp.right;
                        }
                    }
            }
            
		
			
	}
    }
}

