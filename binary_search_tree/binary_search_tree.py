
class Node(object):
    """
    All data used in BST stored as object of Node class
    data : It is the value store in object
    left : it is left child of the object
    right : It is right child of the object
    """
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class bst(object):

    def __init__(self):
        # here root is root of our BST tree which is initially None
        self.root = None

    def insert_node(self, data):
        """
        Add Node in binary tree
        Time Complexity: O(Logn)average case and O(n) in worst case
        :param data:Node with value data will add in BST
        """
        iterator = self.root
        new_node = Node(data)
        if(self.root is None):
            self.root = new_node
        else:
            while iterator is not None:
                if iterator.data >= data:
                    if iterator.left is None:
                        iterator.left = new_node
                        break
                    else:
                        iterator = iterator.left
                else:
                    if iterator.right is None:
                        iterator.right = new_node
                        break
                    else:
                        iterator = iterator.right
        return

    def delete_node(self, data):
        """
        Delete element from binary tree
        Time Complexity: O(Logn)average case and O(n) in worst case
        :param data: Node with value of data will delete from bst
        Throws execption if node with value of data not found
        """
        if self.root.data == data:
            node = self.root
            if node.right is None and node.left is None:
                # if node has no child
                node = None
            elif node.right is None:
                # if node only has left child
                node = node.left
            elif node.left is None:
                # if node only has right child
                node = node.right
            else:
                # if node have both children
                if node.right.left is None:
                    node.right.left = node.left
                    node = node.right
                    self.root = node
                else:
                    to_replace = node.right
                    parent_to_replace = node
                    while to_replace.left is not None:
                        parent_to_replace = to_replace
                        to_replace = to_replace.left
                    node.data = to_replace.data
                    parent_to_replace.left = to_replace.right
                    self.root = node
        else:
            iterator = self.root
            while iterator is not None:
                if iterator.data >= data:
                    if iterator.left is None:
                        raise KeyError('Node does not found')
                    elif iterator.left.data == data:
                        node = iterator.left
                        parent_node = iterator
                        if node.right is None and node.left is None:
                            # if node  has no child
                            parent_node.left = None
                        elif node.right is None:
                            # if node only has left child
                            parent_node.left = node.left
                        elif node.left is None:
                            # if node only has right child
                            parent_node.left = node.right
                        else:
                            # if node have both children
                            if node.right.left is None:
                                node.right.left = node.left
                                parent_node.left = node.right
                            else:
                                to_replace = node.right
                                parent_to_replace = node
                                while to_replace.left is not None:
                                    parent_to_replace = to_replace
                                    to_replace = to_replace.left
                                parent_node.left.data = to_replace.data
                                parent_to_replace.left = to_replace.right
                        return
                    else:
                        iterator = iterator.left
                else:
                    if iterator.right is None:
                        raise KeyError('Node does not found')
                    elif iterator.right.data == data:
                        node = iterator.right
                        parent_node = iterator
                        if node.right is None and node.left is None:
                            # if node has no child
                            parent_node.right = None
                        elif node.right is None:
                            # if node only has left child
                            parent_node.right = node.left
                        elif node.left is None:
                            # if node only has right child
                            parent_node.right = node.right
                        else:
                            # if node have both chidren
                            if node.right.left is None:
                                node.right.left = node.left
                                parent_node.right = node.right
                            else:
                                to_replace = node.right
                                parent_to_replace = node
                                while to_replace.left is not None:
                                    parent_to_replace = to_replace
                                    to_replace = to_replace.left
                                parent_node.right.data = to_replace.data
                                parent_to_replace.left = to_replace.right
                        return
                    else:
                        iterator = iterator.right
        return

    def search_node(self, data):
        """
        search element in binary tree
        Time Complexity: O(Logn)average case and O(n) in worst case
        :param data: search data in bst
        :return : return True if node with value data exist else return False
        """
        if self.root.data == data:
            return True
        else:
            iterator = self.root
            while iterator is not None:
                if iterator.data == data:
                    return True
                elif iterator.data > data:
                    iterator = iterator.left
                else:
                    iterator = iterator.right
            return False

    def print_preorder(self, node):
        """
        Print all element of binary tree in preorder using recurtion
        """
        if node is None:
            return
        elif node.left is None and node.right is None:
            print(node.data, end = ' ')
        else:
            self.print_preorder(node.left)
            print(node.data, end = ' ')
            self.print_preorder(node.right)
            if self.root == node:
                print(' ')
            return


def main():
    inp = bst()
    inp.insert_node(4)
    inp.insert_node(8)
    inp.insert_node(6)
    inp.insert_node(5)
    inp.insert_node(3)
    inp.insert_node(7)
    inp.insert_node(1)
    inp.insert_node(0)
    inp.insert_node(32)
    inp.insert_node(21)
    inp.insert_node(2312)
    inp.insert_node(-1)
    inp.insert_node(-2)
    inp.insert_node(-3)
    inp.insert_node(-4)
    inp.insert_node(88)
    inp.insert_node(9)
    inp.insert_node(19)
    inp.insert_node(28)
    inp.insert_node(54)
    inp.insert_node(44)
    inp.insert_node(69)
    print(inp.search_node(4))
    print(inp.search_node(-1))
    print(inp.search_node(10))
    inp.print_preorder(inp.root)
    inp.delete_node(32)
    inp.delete_node(-4)
    inp.delete_node(4)  # delete root
    inp.print_preorder(inp.root)
    print(inp.root.data)  # check value of root
    inp.delete_node(2)  # just to throw exception


if __name__ == '__main__':
    main()
