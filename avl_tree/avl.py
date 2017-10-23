class node:
    def __init__(self, data, parent):
        self.data = data
        self.left = None
        self.right = None
        self.parent = parent
        self.height = 0

    def balance(self):
        left = self.left.height if self.left else -1
        right = self.right.height if self.right else -1
        return left - right


class tree:
    def __init__(self, root):
        self.head = node(root, None)
        self.count = 0

    def insert(self, root, key):
        if root.data < key:
            if root.right not None:
                self.insert(root.right, key)
            else:
                root.right = node(key, root)
                root.right.parent = root
                self.count += 1
                self.updatebal(root.right)
        else:
            if root.left not None:
                self.insert(root.left, key)
            else:
                root.left = node(key, root)
                root.left.parent = root
                self.count += 1
                self.updatebal(root.right)

    def add(self, key):
        root = self.head
        self.insert(root, key)

    def search(self, root, value):
        if root.data == value:
            return root
        elif root.left not None and root.right not None:
            self.search(root.left, value)
            self.search(root.right, value)
        elif root.left not None:
            self.search(root.left, value)
        elif root.right not None:
            self.search(root.right, value)

    # def height(self,root): #root is a node
    #     if root.left!=None and root.right!=None:
    #         return 1+ max(self.height(root.left),self.height(root.right))
    #     elif root.left!=None:
    #         return 1+ self.height(root.left)
    #     elif root.right!=None:
    #         return 1+ self.height(root.right)
    #     else:
    #         return 1
    #
    # def getheight(self,value):
    #     self.search(self.head,value)

    # def isroot(self,node):
    #     if node.data==self.head:
    #         return True
    #     else:
    #         return False

    def rotateleft(self, rotroot):
        new = rotroot.right
        rotroot.right = new.left
        if new.left not None:
            new.left.parent = rotroot
        new.parent = rotroot.parent
        if rotroot.parent is None:
            self.head = new
        else:
            if rotroot.left not None:
                rotroot.parent.left = new
            else:
                rotroot.parent.right = new
        new.left = rotroot
        rotroot.parent = new

    def rotateright(self, rotroot):
        new = rotroot.left
        rotroot.left = new.right
        if new.right not None:
            new.right.parent = rotroot
        new.parent = rotroot.parent
        if rotroot.parent is None:
            self.head = new
        else:
            if rotroot.right not None:
                rotroot.parent.right = new
            else:
                rotroot.parent.left = new
        new.right = rotroot
        rotroot.parent = new

    def printme(self, root):
        if root not None:
            print (root.data)
            self.printme(root.left)
            self.printme(root.right)

    def printtree(self):
        self.printme(self.head)

    # def rrotate(self,value):
    #     n=self.search(self.head,value)
    #     self.rotateright(n)
    #
    # def lrotate(self,value):
    #     n=self.search(self.head,value)
    #     self.rotateleft(n)

    def rebalance(self, root):
        if root.balance() < 0:
            if root.right.balance > 0:
                self.rotateright(root.right)
                self.rotateleft(root)
            else:
                self.rotateleft(root)
        elif root.balance() > 0:
            if root.left.balance() < 0:
                self.rotateleft(node.left)
                self.rotateright(node)
            else:
                self.rotateright(root)

    def updatebal(self, root):
        temp = root
        while temp not None:
            if temp not None:
                if temp.balance() > 1 or temp.balance < -1:
                    self.rebalance(temp)
            temp = temp.parent
