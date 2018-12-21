from IntNode import IntNode
class LinkedListInt(object):

    def __init__(self):
        self.head = None

    def insertSorted(self, value):
        newNode = IntNode(value)
        if self.isEmpty():
            self.head = newNode
            return
        current = self.head
        if current.getData() > value:
            newNode.setNext(current)
            self.head = newNode
            return
        while current.getNext() != None and current.getNext().getData() < value :
            current = current.getNext()
        newNode.setNext(current.getNext())
        current.setNext(newNode)
        return
    
    def print(self):
        current = self.head
        while current.getNext() != None:
            print(current.getData(), end = "->")
            current = current.getNext()
        print("None")

    def isEmpty(self):
        return self.head == None


list = LinkedListInt()
list.insertSorted(4)
list.insertSorted(1)
list.insertSorted(8)
list.insertSorted(7)
list.insertSorted(9)
list.insertSorted(2)

list.print()