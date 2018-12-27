class circularqueue(object):

    def __init__(self,capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.end = -1
    
    def add(self, value):
        #resize and straigten queue
        if self.size() == self.capacity:
            temp = [None] * 2 * self.capacity
            i = 0
            j = self.front
            while i < self.capacity:
                temp[i] = self.queue[j]
                j = (j + 1) % self.capacity
                i += 1
            self.queue = temp
            self.front = 0
            self.end = self.capacity - 1
            self.capacity *= 2
        self.end = (self.end + 1) % self.capacity
        self.queue[self.end] = value
    
    def remove(self):
        if self.isEmpty():
            return None
        removedElement = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        if self.isEmpty():
            self.front = 0
            self.end = -1
        return removedElement
    
    def peak(self):
        if self.isEmpty():
            return None
        return self.queue[self.front]
    
    def isEmpty(self):
        return self.size() == 0

    def size(self):
        if self.end == -1:
            return 0
        if self.end > self.front:
            return self.end - self.front + 1
        else:
            return self.end - self.front + self.capacity + 1
    
    def print(self):
        i = self.front
        count = 0 
        size = self.size()
        while count < size:
            print(self.queue[i], end = " ")
            i = (i + 1) % self.capacity
            count += 1

queue = circularqueue(5)
queue.add(5)
queue.add(4)
queue.add(3)
queue.add(2)
queue.add(3)
queue.remove()
queue.add(1)
queue.add(6)
queue.print()