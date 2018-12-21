from EmployeeNode import EmployeeNode
from Employee import Employee
class CircularLinkedList(object):

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
    
    def addFront(self,employee):
        newNode = EmployeeNode(employee)
        if self.isEmpty():
            self._tail = newNode
        newNode.setNext(self._head)
        self._head = newNode
        self._tail.setNext(self._head)
        self._size += 1
    
    def removeFront(self):
        if self.isEmpty():
            return None
        elif self._head.getNext() == self._head:
            removedNode = self._head
            self._tail = None
            self._head = None
        else : 
            removedNode = self._head
            self._head = self._head.getNext()
            self._tail.setNext(self._head)
        self._size -= 1
        return removedNode

    def isEmpty(self):
        return self._head == None
    
    def getSize(self):
        return self._size
    
    def print(self):
        current = self._head
        print(current.getEmployee(), end = "")
        current = current.getNext()
        while(current != self._head):
            print(current.getEmployee(), end = "")
            current = current.getNext()
        print()

charlie = Employee("Charlie","Man",121)
prateek = Employee("Prateek","Singhal",1212)
sara = Employee("Sara","Khan",12121)

list = CircularLinkedList()
list.addFront(charlie)
list.addFront(prateek)
list.addFront(sara)
list.print()

print(list.removeFront().getEmployee())
print(list.removeFront().getEmployee())
list.print()
print(list.removeFront().getEmployee())
list.print
print(list.getSize())
print(list.isEmpty())
        
    