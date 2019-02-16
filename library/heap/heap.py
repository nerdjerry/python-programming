from math import floor

class heap(object):

    def __init__(self):
        self.heap = []
        self.index = 0
    
    def insert(self,value):
        self.heap.append(value)
        self.index += 1
        currentIndex = self.index - 1
        parentIndex = self.parent(currentIndex)
        while parentIndex >= 0 and self.heap[currentIndex] > self.heap[parentIndex] :
            self.swap(currentIndex,parentIndex)
            currentIndex = parentIndex
            parentIndex = self.parent(currentIndex)
    
    def swap(self, currentIndex, parentIndex):
        temp = self.heap[parentIndex]
        self.heap[parentIndex] = self.heap[currentIndex]
        self.heap[currentIndex] = temp
    
    def parent(self,currentIndex):
        return floor((currentIndex - 1) / 2)

data = heap()
data.insert(21)
data.insert(45)
data.insert(13)
data.insert(89)
data.insert(23)
data.insert(12)
data.insert(4)
data.insert(90)
print("done")