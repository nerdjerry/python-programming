class IntNode(object):

    def __init__(self, value):
        self.data = value
        self.next = None
    
    def getData(self):
        return self.data
    
    def setData(self, value):
        self.data = value
    
    def getNext(self):
        return self.next
    
    def setNext(self, next):
        self.next = next