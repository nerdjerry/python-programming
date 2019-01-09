class StackArray(object):

    def __init__(self,capacity):
        self.head = -1
        self.length = capacity
        self.data = [None] * self.length
    
    def push(self,value):
        if self.head >= self.length - 1:
            temp = [None] * 2 * self.length
            for i in range(self.length):
                temp[i] = self.data[i]
            self.data = temp
            self.length *= 2
        self.head += 1
        self.data[self.head] = value
    
    def pop(self):
        if self.head > -1:
            pop = self.data[self.head]
            self.head -= 1
            return pop
        else:
            print("Underflow")

    def peak(self):
        if self.head > -1:
            return self.data[self.head]
    
    def print(self):
        for i in range(self.head, -1, -1):
            print(self.data[i])