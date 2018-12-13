from EmployeeNode import EmployeeNode
from Employee import Employee

class LinkedList(object):

    def __init__(self):
        self.head = None
    
    def insertAtStart(self,employee):
        newEmployeeNode = EmployeeNode(employee)
        if self.head != None:
            newEmployeeNode.setNext(self.head)
        self.head = newEmployeeNode

    def removeFromStart(self):
        removedNode = self.head
        self.head = removedNode.getNext()
        removedNode.setNext(None)
        return removedNode
    
    def print(self):
        currentNode = self.head
        while currentNode != None:
            print(currentNode.getEmployee(), end = " ")
            print("->", end = " ")
            currentNode = currentNode.getNext()
        print("None")

charlie = Employee("Charlie","Man",121)
prateek = Employee("Prateek","Singhal",1212)
sara = Employee("Sara","Khan",12121)

list = LinkedList()
list.insertAtStart(charlie)
list.insertAtStart(prateek)
list.insertAtStart(sara)

list.print()

print(list.removeFromStart().getEmployee())

list.print()