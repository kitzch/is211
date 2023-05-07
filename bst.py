# write a bst with the input: 11 14 15 18 19 21 25 28 30 32

class TreeNode:

    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.value)
        if self.right:
            self.right.inorder()

    def preorder(self):
        print(self.value)
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.value)

    def find(self, value):
        if value < self.value:
            if self.left is None:
                return False
            else:
                self.left.find(value)
        elif value > self.value:
            if self.right is None:
                return False
            else:
                self.right.find(value)
        else:
            return True

#adding the parent node
tree = TreeNode(21)

#adding child nodes
tree.insert(14)
tree.insert(28)
tree.insert(11)
tree.insert(18)
tree.insert(15)
tree.insert(19)
tree.insert(25)
tree.insert(32)
tree.insert(30)

tree.inorder()

