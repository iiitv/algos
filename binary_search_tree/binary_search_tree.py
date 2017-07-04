import sys


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
        Throws execption if node with value of data not exist
        """
        try:
            parent_node = self.search_node(data)
            if parent_node is None:
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
                if (parent_node.left is not None and
                        parent_node.left.data is data):
                    node = parent_node.left
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
                    node = parent_node.right
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
        except LookupError as e:
            print('sorry,%s' % (e))

    def search_node(self, data):
        """
        search element in binary tree
        Time Complexity: O(Logn)average case and O(n) in worst case
        :param data: search node of value data in bst
        :return : parent of the node whose value is data or raise exception
        """
        parent_node = None
        if self.root is None:
            raise LookupError('Cannot delete anything, BST is empty')
        elif self.root.data == data:
            return parent_node
        else:
            iterator = self.root
            while iterator is not None:
                if iterator.data == data:
                    return parent_node
                elif iterator.data > data:
                    parent_node = iterator
                    iterator = iterator.left
                else:
                    parent_node = iterator
                    iterator = iterator.right
            raise LookupError('Node does not exist')

    def print_preorder(self, node):
        """
        Print all element of binary tree in preorder using recurtion
        """
        if node is None:
            return
        elif node.left is None and node.right is None:
            sys.stdout.write(str(node.data) + ' ')
        else:
            self.print_preorder(node.left)
            sys.stdout.write(str(node.data) + ' ')
            self.print_preorder(node.right)
            if self.root == node:
                sys.stdout.write('\n')
            return


def main():
    inp = bst()
    inp.delete_node(2)  # try to delete node in empty try
    inp.insert_node(4)
    inp.insert_node(8)
    inp.insert_node(6)
    inp.insert_node(5)
    inp.insert_node(44)
    inp.insert_node(69)
    inp.print_preorder(inp.root)
    inp.delete_node(69)
    inp.delete_node(5)
    inp.delete_node(4)  # delete root
    inp.print_preorder(inp.root)
    print(inp.root.data)  # check value of root
    inp.delete_node(2)  # just to throw exception


if __name__ == '__main__':
    main()
