class StackArray(object):

    def __init__(self):
        self.head = -1
        self.length = 10
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

stack = StackArray()
stack.push(5)
stack.push(6)
stack.push(9)
stack.push(8)
stack.push(1)
stack.push(5)
stack.push(21)
stack.push(12)
stack.push(23)
stack.push(13)
stack.push(123)
stack.push(1235)
stack.push(21)
stack.print()
print(stack.peak())
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.print()
