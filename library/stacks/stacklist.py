from LinkedList import LinkedList
from Employee import Employee

class StackList(object):

    def __init__(self):
        self.stack = LinkedList()
    
    def push(self,value):
        self.stack.insertAtStart(value)
    
    def pop(self):
        return self.stack.removeFromStart()
    
    def peak(self):
        return self.stack.head.employee
    
stack = StackList()
charlie = Employee("Charlie","Man",121)
prateek = Employee("Prateek","Singhal",1212)
sara = Employee("Sara","Khan",12121)
stack.push(charlie)
stack.push(prateek)
stack.push(sara)
print(stack.peak())
stack.pop()
stack.pop()