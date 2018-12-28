class Queue(object):

    def __init__(self,capacity):
        self.queue = [None] * capacity
        self.size = 0
        self.capacity = capacity
        self.front = 0
        self.end = -1
    
    def enqueue(self, value):
        self.end +=1
        if self.end == self.capacity:
            temp = [None] * 2 * self.capacity
            for i in range(self.capacity):
                temp[i] = self.queue[i]
            self.capacity *= 2
            self.queue = temp
        self.queue[self.end]= value
        self.size +=1
    
    def dequeue(self):
        if self.isEmpty():
            return False
        if self.front < self.capacity :
            removed = self.queue[self.front]
            self.queue[self.front] = None
            self.front +=1
            self.size -=1
            if(self.isEmpty()):
                self.front = 0
                self.end = -1
            return removed

    def peak(self):
        if self.isEmpty():
            return False
        else:
            return self.queue[self.front]
    def isEmpty(self):
        return self.front > self.end
    
    def print(self):
        for i in range(self.front, self.end):
            print(self.queue[i], end = " ")
        print()
    

""" queue = Queue(7)
queue.enqueue(5)
queue.enqueue(6)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(2)
queue.enqueue(1)
queue.enqueue(0)
queue.print()
print(queue.dequeue())
print(queue.peak())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue()) """