class Node(object):
    # Node for Binary search Tree and set the Node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# insert data in tree


def insert(node, data):
    if node is None:
        # create a new node
        node = Node(data)
        return node
    else:
        # go to the left child
        if data <= node.data:
            node.left = insert(node.left, data)
        # got to the right child
        else:
            node.right = insert(node.right, data)
    return node

# seraching data


def search(node, data):
    # if data not present
    if node is None:
        return None
    # go to the left if data is lesser from root
    if data < node.data:
        node = search(node.left, data)
    # go to the right if data is greater from root
    elif data > node.data:
        node = search(node.right, data)
    # data found
    elif data == node.data:
        return node
    return node

# find the minimum


def minright(node):
    if node.left is None:
        return node
    else:
        node = minright(node.left)
    return node

# delete a node


def delete(root, data):
    if root is None:
        return root
    if data < root.data:
        root.left = delete(root.left, data)
    elif data > root.data:
        root.right = delete(root.right, data)
    # data node is found
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        # if left or right child is Not None find the the minimum node in right child
        temp = minright(root.right)
        root.data = temp.data
        # recursive delete the minimum node in right child
        root.right = delete(root.right, temp.data)
    return root

# print inorder


def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

# print preorder


def preorder(root):
    if root is not None:
        print(root.data)
        preorder(root.left)
        preorder(root.right)

# print postorder


def postorder(root):
    if root is not None:
        preorder(root.left)
        preorder(root.right)
        print(root.data)

# check the method


def main():
    root = None
    root = insert(root, 5)
    root = insert(root, 11)
    root = insert(root, 3)
    root = insert(root, 1)
    root = insert(root, 50)
    root = insert(root, 45)
    root = insert(root, 30)
    root = insert(root, 35)
    print("****** InOrder ******")
    inorder(root)
    print("****** PreOrder ******")
    preorder(root)
    print("****** PostOrder ******")
    postorder(root)
    print("***** search Node ******")
    temp = search(root, 28)
    if temp is not None:
        print("node search==> ", temp.data)
    else:
        print("node is not present")
    print("***** delete Node ******")
    root = delete(root, 11)
    inorder(root)


if __name__ == '__main__':
    main()
