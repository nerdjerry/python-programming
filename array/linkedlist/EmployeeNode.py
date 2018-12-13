class EmployeeNode(object):

    def __init__(self, employee):
        self.employee = employee
        self.next = None
    
    def getNext(self):
        return self.next
    
    def setNext(self, employee):
        self.next = employee
    
    def getEmployee(self):
        return self.employee
    
    def setEmployee(self, employee):
        self.employee = employee