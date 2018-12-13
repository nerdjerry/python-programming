class Employee(object):

    def __init__(self,firstName, lastName, id):
        self.firstName = firstName
        self.lastName = lastName
        self.id = id
    
    def getFirstName(self):
        return self.firstName
    
    def setFirstName(self,firstName):
        self.firstName = firstName
    
    def getLastName(self):
        return self.lastName
    
    def setLasName(self, lastName):
        self.lastName = lastName
    
    def getId(self):
        return self.id
    
    def setId(self, id):
        self.id = id
    
    def __str__(self):
        return str("Employee{" +
                "firstname='" + self.firstName + '\'' +
                ", lastname='" + self.lastName + '\'' +
                ", id=" + str(self.id) +
                '}')