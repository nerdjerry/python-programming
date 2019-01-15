from insertionsort import sort
class ArrayList(object):
    
    def __init__(self,capacity):
        self.capacity = capacity
        self.array = [None] * self.capacity
        self.top = 0
        self.end = 0
    
    def add(self,value):
        self.array[self.end] = value
        self.end += 1

    def hasNext(self):
        isNotNext = self.array[self.top] != None
        if not isNotNext:
            self.top = 0
            self.end = 0 
        return isNotNext

    def get(self):
        returnValue = self.array[self.top]
        self.array[self.top] = None
        self.top += 1
        return returnValue
    
    def sort(self):
        sort(self.array,self.end)

def bucketsort(input):
    table = [None] * 10
    for i in range(len(input)):
        #Scattering
        hashedKey = hash(input[i])
        if table[hashedKey] == None:
            table[hashedKey] = ArrayList(len(input))
        table[hashedKey].add(input[i])
    
    #sorting
    for i in range(len(table)):
        if table[i] != None:
            table[i].sort()
    
    #Gathering
    j = 0
    for i in range(len(table)):
        if table[i] != None:
            while table[i].hasNext():
                input[j] = table[i].get()
                j += 1

def hash(value):
    return value // 10

input = [54, 46, 83, 66, 95, 92, 43]
bucketsort(input)
for i in range(len(input)):
    print(input[i])