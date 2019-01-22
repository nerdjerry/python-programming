from TreeNode import TreeNode

class Tree(object):
    
    def __init__(self):
        self.root = None
    
    def insert(self,value):
        if self.root == None:
            self.root = TreeNode(value)
        else:
            self.root.insert(value)

    def traverseInOrder(self):
        if self.root != None:
            self.root.traverseInOrder()
        else:
            print("Empty Tree") 
    
    def traversePostOrder(self):
        if self.root != None:
            self.root.traversePostOrder()
        else:
            print("Empty Tree")
    
    def traversePreOrder(self):
        if self.root != None:
            self.root.traversePreOrder()
        else:
            print("Empty Tree")
    
tree = Tree()
tree.insert(25)
tree.insert(20)
tree.insert(13)
tree.insert(27)
tree.insert(30)
tree.traversePostOrder()
print("In Order")
tree.traverseInOrder()
print("Pre Order")
tree.traversePreOrder()