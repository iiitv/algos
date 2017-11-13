# Node for Binary Search Tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Function for find the left side right most node in binary search tree
def find_leftside_rightmost(node):
    left_side_rightmost = node.left
    prev_node = node
    while left_side_rightmost.right is not None:
        prev_node = left_side_rightmost
        left_side_rightmost = left_side_rightmost.right
    return left_side_rightmost, prev_node


class BST:
    def __init__(self):

        self.root = None  # Root for Binary Search Tree
        self.count = None  # Size of Binary Search Tree

    def insert(self, data):

        new_node = Node(data)  # Create a node for the new entry

        if self.root is None:
            self.root = new_node

        else:

            cur_node = self.root
            prev_node = None

            while cur_node is not None:

                prev_node = cur_node
                if data <= cur_node.data:
                    cur_node = cur_node.left
                else:
                    cur_node = cur_node.right

            if data <= prev_node.data:
                prev_node.left = new_node
            else:
                prev_node.right = new_node

    # Print a statement according to the search result
    def search(self, data):

        cur_node = self.root
        while cur_node is not None and data != cur_node.data:
            if data < cur_node.data:
                cur_node = cur_node.left
            else:
                cur_node = cur_node.right

        # if node found, cur_node not to be None
        if cur_node is None:
            print("Invalid Search")
        else:
            print("Node was found successfully.")

    # Function for deleting node using parent node
    def delete_node(self, del_node, parent_node):

        # True if node is in left side of the parent, else it's in right side
        isLeft = False

        if parent_node is None:  # For root node deleting

            # Root hasn't children
            if del_node.left is None and del_node.right is None:
                self.root = None

            # Root has a child
            elif del_node.left is None or del_node.right is None:
                if del_node.left is None:
                    self.root = del_node.right
                else:
                    self.root = del_node.left

            # Root has 2 children
            else:
                LHS_rightmost, prev_node = find_leftside_rightmost(del_node)
                self.root.data = LHS_rightmost.data
                if del_node == prev_node:
                    prev_node.left = None
                else:
                    prev_node.right = None

        else:  # For deleting a node except root

            if del_node.data <= parent_node.data:
                isLeft = True

            # Deleting node hasn't children
            if del_node.left is None and del_node.right is None:
                if isLeft:
                    parent_node.left = None
                else:  # isLeft is False
                    parent_node.right = None

            # Deleting node has a child
            elif del_node.left is None or del_node.right is None:
                if del_node.left is None:
                    parent_node.left = del_node.right
                else:
                    parent_node.left = del_node.left

            # Deleting node has 2 children
            else:
                LHS_rightmost, prev_node = find_leftside_rightmost(del_node)
                del_node.data = LHS_rightmost.data
                if del_node == prev_node:
                    prev_node.left = None
                else:
                    prev_node.right = None

    # Finalized delete function
    def delete(self, data):

        cur_node = self.root
        parent = None  # Parent node to the deleting node
        while cur_node is not None and data != cur_node.data:
            parent = cur_node
            if data < cur_node.data:
                cur_node = cur_node.left
            else:
                cur_node = cur_node.right

        # if node found, cur_node not to be None
        if cur_node is not None:
            self.delete_node(cur_node, parent)
        else:
            print("Cannot delete, Node not present.")

    # Print nodes in in-order using root
    def printInOrder(self):
        self.in_order(self.root)

    def in_order(self, subtree):
        if subtree is not None:
            self.in_order(subtree.left)
            print(subtree.data)
            self.in_order(subtree.right)


def main():
    # Created an empty tree
    tree = BST()
    # Adding a few test entries
    tree.insert(10)
    tree.insert(9)
    tree.insert(3)
    tree.insert(12)
    tree.insert(14)
    tree.insert(7)
    tree.insert(6)
    tree.insert(11)
    tree.insert(1)
    tree.insert(2)
    # Test printing
    tree.printInOrder()
    # Deleting a valid node
    tree.delete(9)
    # Print again
    tree.printInOrder()
    # Searching a valid node
    tree.search(12)
    # Searching an invalid node
    tree.search(4)
    # Deleting a invalid node
    tree.delete(9)


if __name__ == '__main__':
    main()
