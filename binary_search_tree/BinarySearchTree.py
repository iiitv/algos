class Node():

    # the actual data which is stored in the node
    __data = None
    # left child of the node
    __left = None
    # right child of the node
    __right = None

    def __init__(self, data=None, left=None, right=None):
        # here self.data, self.left, self.right are not variables
        # these are setters which are defined below
        self.data = data
        self.left = left
        self.right = right

    # adding @property makes this a getter and can be accessed by ObjectName.data
    @property
    def data(self):
        return self.__data

    # we need setter for "data" since its a private variable
    @data.setter
    def data(self, value):
        # Use of setters is to validate data or perform some action before assiging the data
        # we only want our data to be a number/int
        if isinstance(value, int):
            self.__data = value
        else:
            self.__data = None
            print("Invalid data: {} only integers(int) are accepted.".format(value))

    # now we will repeat the same for "left" and "right" variables too
    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, value):
        # since left is not just any variable but a node itself
        if (isinstance(value, Node)) or (value is None):
            self.__left = value
        else:
            print("Invalid left node, should be an instance of class 'Node'.")

    # repeat the same for right node
    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, value):
        # since left is not just any variable but a node itself
        if (isinstance(value, Node)) or (value is None):
            self.__right = value
        else:
            print("Invalid right node, should be an instance of class 'Node'.")

    def insert(self, value):
        # no duplicate data
        if self.data == value:
            print("Value: {} already exists.".format(value))
            return False
        elif self.data > value:
            # if there is a left child insert data there
            if self.left:
                return self.left.insert(value)
            # else create a new node
            else:
                self.left = Node(value)
                return True
        # repeating same steps for the right child
        else:
            if self.right:
                return self.right.insert(value)
            else:
                self.right = Node(value)
                return True

    def find(self, value):
        if self.data == value:
            print("Value: {} FOUND!".format(value))
            return True
        elif self.data > value:
            if self.left:
                return self.left.find(value)
            else:
                print("Value: {} NOT FOUND!".format(value))
                return False
        else:
            if self.right:
                return self.right.find(value)
            else:
                print("Value: {} NOT FOUND!".format(value))
                return False

    def preorder(self):
        if self:
            print(str(self.data))
            if self.left:
                self.left.preorder()
            if self.right:
                self.right.preorder()

    def postorder(self):
        if self:
            if self.right:
                self.right.postorder()
            if self.left:
                self.left.postorder()
            print(str(self.data))

    def inorder(self):
        if self:
            if self.left:
                self.left.inorder()
            print(str(self.data))
            if self.right:
                self.right.inorder()

    def __str__(self):
        if self.data is not None:
            return "Data: " + str(self.data)
        return "No data in this node."


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root:
            return self.root.insert(value)
        else:
            self.root = Node(value)
            return True

    def delete(self, value):
        # if tree is empty
        if self.root is None:
            return False

        # data is in root node
        elif self.root.data == value:
            # if there are no children
            if self.root.left is None and self.root.right is None:
                self.root = None
            # if only left child exists
            elif self.root.left and self.root.right is None:
                self.root = self.root.left
            # if only right child exists
            elif self.root.left is None and self.root.right:
                self.root = self.root.right
            # if both children exist
            elif self.root.left and self.root.right:
                parentNode = self.root
                nodeToDelete = self.root.right
                # find the lowest value in right sub-tree
                while nodeToDelete.left:
                    parentNode = nodeToDelete
                    nodeToDelete = nodeToDelete.left
                # copy the lowest value
                self.root.data = nodeToDelete.data

                # since it doesn't have any left child, it has right child only
                # delete the "nodeToDelete" by moving the right sub-tree upwards
                if nodeToDelete.right:
                    if parentNode.data > nodeToDelete.data:
                        parentNode.left = nodeToDelete.right
                    elif parentNode.data < nodeToDelete.data:
                        parentNode.right = nodeToDelete.right

                # it has no children
                else:
                    if nodeToDelete.data < parentNode.data:
                        parentNode.left = None
                    else:
                        parentNode.right = None

            print("Value: {} deleted.".format(value))
            return True

        # Data is not in the root node.

        parent = None
        node = self.root
        # here "node" is pointing to any node in the tree below root node.

        # find node to remove
        while node and node.data != value:
            parent = node
            if value < node.data:
                node = node.left
            elif value > node.data:
                node = node.right

        # if value doesn't exist in the tree
        if node is None or node.data != value:
            print("Cannot delete value: {} it doesn't exist".format(value))
            return False

        # if there are no children
        elif node.left is None and node.right is None:
            if value < parent.data:
                parent.left = None
            else:
                parent.right = None
            print("Value: {} deleted.".format(value))
            return True

        # if there is only left child
        elif node.left and node.right is None:
            if value < parent.data:
                parent.left = node.left
            else:
                parent.right = node.left
            print("Value: {} deleted.".format(value))
            return True

        # if there is only right child
        elif node.left is None and node.right:
            if value < parent.data:
                parent.left = node.right
            else:
                parent.right = node.right
            print("Value: {} deleted.".format(value))
            return True

        # if both children exist
        else:
            parentNode = node
            nodeToDelete = node.right

            # find the lowest value in right sub-tree
            while nodeToDelete.left:
                parentNode = nodeToDelete
                nodeToDelete = nodeToDelete.left
            # copy the lowest value
            node.value = nodeToDelete.data

            # since the "nodeToDelete" does't have a left child , it has a right child only
            if nodeToDelete.right:
                if parentNode.data > nodeToDelete.data:
                    parentNode.left = nodeToDelete.right
                elif parentNode.data < nodeToDelete.data:
                    parentNode.right = nodeToDelete.right

            # "nodeToDelete" doesn't have any child.
            else:
                if nodeToDelete.data < parentNode.data:
                    parentNode.left = None
                else:
                    parentNode.right = None
            print("Value: {} deleted.".format(value))

    def find(self, value):
        if self.root:

            return self.root.find(value)
        else:
            print("Value: {} NOT FOUND!".format(value))
            return False

    def preorder(self):
        print("Pre-Order:")
        if self.root:
            self.root.preorder()

    def postorder(self):
        print("Post-Order:")
        if self.root:
            self.root.postorder()

    def inorder(self):
        print("In-Order:")
        if self.root:
            self.root.inorder()


def main():

    # this will output an error
    # we are using getters and setters to make sure the entered data is valid

    # invalid left and right node
    test1 = Node(0, 5, "anything")
    print(test1)

    # invalid right node
    test2 = Node(0, None, None)

    # invalid data
    mynode1 = Node("5", test2, test2)

    # a proper node.
    mynode2 = Node(5, test2, test2)

    # we can print a Node instance directly, thanks to the __str__ magic method!
    print(mynode1)
    print(mynode2)

    # create our Binary Search Tree
    myBST = BST()

    # insert some values to the tree

    for i in range(5, 20):
        myBST.insert(i)

    myBST.preorder()
    myBST.postorder()
    myBST.inorder()

    # try inserting a duplicate
    duplicateValue = 14
    if myBST.insert(duplicateValue):
        print("Inserted: {}".format(duplicateValue))
    else:
        print("Insertion failed for {}".format(duplicateValue))

    myBST.delete(11)
    myBST.delete(6)
    myBST.delete(6)
    myBST.delete(5)
    myBST.find(9)
    myBST.find(5)
    myBST.preorder()
    print("End")


if __name__ == '__main__':
    main()
