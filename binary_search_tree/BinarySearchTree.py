class bst_node:#Node for Binary search Tree
    def __init__(self,data):#set the Node
        self.data = data
        self.left = None
        self.right = None

class bst:#bst class for implement method
    def insert(node,data):#insert data in tree
        if node is None:
            node = bst_node(data)#create a new node
            return node
        else:
            if data <= node.data:#go to the left child
                node.left = bst.insert(node.left,data)
            else:#got to the right child
                node.right = bst.insert(node.right,data)
        return node

    def search(node,data):#seraching data
        if node is None:#if data not present
            return None
        if data < node.data:#go to the left if data is lesser from root
            node = bst.search(node.left,data)
        elif data > node.data:#go to the right if data is greater from root
            node = bst.search(node.right,data)
        elif data == node.data:# data found
            return node
        return node

    def min_right(node):#geeting the minimum
        if node.left is None:#found minimum
            return node
        else:#go to the left
            node = bst.min_right(node.left)
        return node

    def delete(root,data):#delete a node
        if root is None:
            return root
        if data < root.data:#go to the left
            root.left = bst.delete(root.left,data)
        elif data > root.data:#goto right
            root.right = bst.delete(root.right,data)
        else:#data node node is found
            if root.left is None:#left child is None
                temp = root.right
                root = None
                return temp
            elif root.right is None:#right child is None
                temp = root.left
                root = None
                return temp
            #if left or right child is Not None
            temp = bst.min_right(root.right)#find the the minimum node in right child
            root.data = temp.data#delete the data
            root.right = bst.delete(root.right,temp.data)#recursive delete the minimum node in right child
        return root

    def inOrder(root):#print inorder
        if root is not None:
            bst.inOrder(root.left)
            print(root.data)
            bst.inOrder(root.right)

    def preOrder(root):#print preorder
        if root is not None:
            print(root.data)
            bst.preOrder(root.left)
            bst.preOrder(root.right)

   def postOrder(root):#print postorder
        if root is not None:
            bst.preOrder(root.left)
            bst.preOrder(root.right)
            print(root.data)

def main():#check the method
    root = None
    root = bst.insert(root,5)
    root = bst.insert(root,11)
    root = bst.insert(root,3)
    root = bst.insert(root,1)
    root = bst.insert(root,6)
    print("****** InOrder ******")
    bst.inOrder(root)
    print("****** PreOrder ******")
    bst.preOrder(root)
    print("****** PostOrder ******")
    bst.postOrder(root)
    print("***** search Node ******")
    temo = bst.search(root,28)
    if temo is not None:
        print("node search==> ",temo.data )
    else:
        print("node is not present")
    print("***** delete Node ******")
    root = bst.delete(root,11)
    bst.inOrder(root)

if __name__ == '__main__':
    main()
