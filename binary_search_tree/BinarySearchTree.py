class BST:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def __str__(self):
        return "[%s, %s, %s]" % (self.left, str(self.val), self.right)

    def isEmpty(self):
        return self.left == self.right == self.val == None

    def insert(self, val):
        if self.isEmpty():
            self.val = val
        elif val < self.val:
            if self.left is None:
                self.left = BST(val)
            else:
                self.left.insert(val)
        else:
            if self.right is None:
                self.right = BST(val)
            else:
                self.right.insert(val)

a = BST(1)
a.insert(2)
a.insert(3)
a.insert(0)
print a
