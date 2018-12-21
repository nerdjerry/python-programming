from EmployeeNode import EmployeeNode
from Employee import Employee

class LinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0
    
    def insertAtStart(self,employee):
        newEmployeeNode = EmployeeNode(employee)
        if self.head != None:
            newEmployeeNode.setNext(self.head)
        self.head = newEmployeeNode
        self.size +=1

    def removeFromStart(self):
        if(self.isEmpty()):
            return None
        removedNode = self.head
        self.head = removedNode.getNext()
        removedNode.setNext(None)
        self.size -=1
        return removedNode
    
    def addBefore(self,newEmployee, employee):
        current = self.head
        newEmployeeNode = EmployeeNode(newEmployee)
        if self.isEmpty():
            return False
        if current.getEmployee() == employee:
            newEmployeeNode.setNext(current)
            self.head = newEmployeeNode
            return True
        while current.getNext().getEmployee() != employee:
            current = current.getNext()
        if current.getNext().getEmployee() == employee:    
            newEmployeeNode.setNext(current.getNext())
            current.setNext(newEmployeeNode)
            return True
        else:
            return False
    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.head == None
    
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
aditi = Employee("Aditi","Aggarwal",321)
list.addBefore(aditi,sara)
list.print()
print(list.removeFromStart().getEmployee())
print(list.removeFromStart().getEmployee())
print(list.removeFromStart().getEmployee())

list.print()

print(list.getSize())
print(list.isEmpty())