from Employee import Employee
from EmployeeNode import EmployeeNode

class DoublyLinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def insertAtStart(self, employee):
        newEmployeeNode = EmployeeNode(employee)
        if self.head != None:
            newEmployeeNode.setNext(self.head)
            newEmployeeNode.setPrev(None)
            self.head.setPrev(newEmployeeNode)
        else:
            self.tail = newEmployeeNode

        self.head = newEmployeeNode
        self.size +=1

    def insertAtEnd(self, employee):
        newEmployeeNode = EmployeeNode(employee)
        if self.tail != None:
            newEmployeeNode.setNext(None)
            newEmployeeNode.setPrev(self.tail)
            self.tail.setNext(newEmployeeNode)
        else:
            self.head = newEmployeeNode
        
        self.tail = newEmployeeNode
        self.size +=1

    def removeAtFront(self):
        if(self.isEmpty()):
            return None
        if(self.head.getNext() == None):
            self.tail = None
        removedNode = self.head
        self.head = removedNode.getNext()
        removedNode.setNext(None)
        self.size -=1
        return removedNode

    def removeAtEnd(self):
        if(self.isEmpty()):
            return None
        if(self.tail.getPrev() == None):
            self.head = None
        removedNode = self.tail
        self.tail = removedNode.getPrev()
        removedNode.setPrev(None)
        self.size -=1
        return removedNode
    def addBefore(self,newEmployee, employee):
        newEmployeeNode = EmployeeNode(newEmployee)
        current = self.head
        if self.isEmpty():
            return False
        if current.getEmployee() == employee:
            newEmployeeNode.setNext(current)
            current.setPrev(newEmployeeNode)
            self.head = newEmployeeNode
            self.size += 1
            return True
        while current.getNext() != None and current.getNext().getEmployee() != employee:
            current = current.getNext()
        if(current.getNext().getEmployee() == employee):
            newEmployeeNode.setNext(current.getNext())
            current.getNext().setPrev(newEmployeeNode)
            current.setNext(newEmployeeNode)
            newEmployeeNode.setPrev(current)
            self.size +=1
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

list = DoublyLinkedList()
list.insertAtEnd(charlie)
list.insertAtEnd(prateek)
list.insertAtEnd(sara)

list.print()
aditi = Employee("Aditi","Aggarwal",31)
list.addBefore(aditi,prateek)
list.print()
print(list.removeAtFront().getEmployee())

list.print()

print(list.getSize())
print(list.isEmpty())