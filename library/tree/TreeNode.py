class TreeNode(object):

    def __init__(self,value):
        self.data = value
        self.leftChild = None
        self.rightChild = None
    
    def insert(self, value):
        if self.data == value:
            return
        if self.data > value :
            if self.leftChild == None:
                self.leftChild = TreeNode(value)
            else:
                self.leftChild.insert(value)
        else:
            if self.rightChild == None:
                self.rightChild = TreeNode(value)
            else:
                self.rightChild.insert(value)

    def traversePreOrder(self):
        print(self.data)
        if self.leftChild != None:
            self.leftChild.traversePreOrder()
        if self.rightChild != None:
            self.rightChild.traversePreOrder()
    
    def traverseInOrder(self):
        if self.leftChild != None:
            self.leftChild.traverseInOrder()
        print(self.data)
        if self.rightChild != None:
            self.rightChild.traverseInOrder()

    def traversePostOrder(self):
        if self.leftChild != None:
            self.leftChild.traversePostOrder()
        if self.rightChild != None:
            self.rightChild.traversePostOrder()
        print(self.data)

    def get(self, value):
        if self.data == value:
            return self.data
        elif self.data < value:
            if self.rightChild != None:
                return self.rightChild.get(value)
        else:
            if self.leftChild != None:
                return self.leftChild.get(value)
        return None
    
    def min(self):
        if self.leftChild != None:
            return self.leftChild.min()
        else:
            return self.data
    
    def max(self):
        if self.rightChild != None:
            return self.rightChild.max()
        else:
            return self.data
        
    def getData(self):
        return self.data
    
    def setData(self,value):
        self.data = value
    
    def getLeftChild(self):
        return self.leftChild
    
    def setLeftChild(self,leftChild):
        self.leftChild = leftChild
    
    def getRightChild(self):
        return self.rightChild
    
    def setRightChild(self,rightChild):
        self.rightChild = rightChild
