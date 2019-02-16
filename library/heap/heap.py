from math import floor

class heap(object):

    def __init__(self):
        self.heap = []
        self.index = 0
    
    def insert(self,value):
        self.heap.append(value)
        
        self.heapifyAbove(self.index)
        self.index += 1
    
    def heapifyAbove(self,index):
        newValue = self.heap[index]
        parentIndex = self.parent(index)
        while index > 0 and newValue > self.heap[parentIndex]:
            #bring parent down
            self.heap[index] = self.heap[parentIndex]
            index = parentIndex
            parentIndex = self.parent(index)
        #heapified value above
        self.heap[index] = newValue

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