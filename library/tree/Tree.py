from TreeNode import TreeNode

class Tree(object):
    
    def __init__(self):
        self.root = None
    
    def insert(self,value):
        if self.root == None:
            self.root = TreeNode(value)
        else:
            self.root.insert(value)

tree = Tree()
tree.insert(25)
tree.insert(20)
tree.insert(13)
tree.insert(27)
tree.insert(30)