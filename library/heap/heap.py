from math import floor

class heap(object):

    def __init__(self):
        self.heap = []
        self.index = 0
    
    def insert(self,value):
        self.heap.append(value)
        
        self.heapifyAbove(self.index)
        self.index += 1
    
    def delete(self,value):
        deleteIndex = self.getDeleteIndex(value)
        if deleteIndex == -1:
            #Value to be deleted is not found
            return None
        else:
            #remove value by replacing with leftmost element of tree
            self.index -= 1
            self.heap[deleteIndex] = self.heap[self.index]
            self.heap[self.index] = None
            if deleteIndex > 0 and self.heap[deleteIndex] > self.heap[self.parent(deleteIndex)]:
                self.heapifyAbove(deleteIndex)
            elif (self.leftChildExists(deleteIndex) and \
                self.heap[deleteIndex] < self.heap[self.leftChild(deleteIndex)]) or \
                (self.rightChildIndexExists(deleteIndex) and \
                    self.heap[deleteIndex] < self.heap[self.rightChild(deleteIndex)]):
                self.heapifyBelowIndex(deleteIndex,self.index - 1)
            else:
                return
    
    def remove(self,index):
        if self.isEmpty():
            return
        deletedValue = self.heap[index]
        parentIndex = self.parent(index)
        self.heap[index] = self.heap[self.index - 1]
        self.heap[self.index - 1] = None
        if index == 0 or self.heap[index] < self.heap[parentIndex]:
            self.heapifyBelowIndex(index,self.index - 1)
        else:
            self.heapifyAbove(index)
        self.index -= 1
        return deletedValue

    def peak(self):
        if self.isEmpty():
            return
        else:
            return self.heap[0]

    def leftChildExists(self,index):
        return self.leftChild(index) < self.index and self.heap[self.leftChild(index)] != None
    
    def rightChildIndexExists(self,index):
        return self.rightChild(index) <  self.index and self.heap[self.rightChild(index)] != None

    def isEmpty(self):
        return self.index == 0

    def getDeleteIndex(self,value):
        currentIndex = 0
        while currentIndex < self.index:
            if self.heap[currentIndex] == value:
                return currentIndex
            currentIndex += 1
        return -1

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
    
    def heapifyBelowIndex(self,index,lastHeapIndex):
        while index < lastHeapIndex:
            leftChildIndex = self.leftChild(index)
            rightChildIndex = self.rightChild(index)
            if leftChildIndex < lastHeapIndex:
                if rightChildIndex < lastHeapIndex and self.heap[leftChildIndex] < self.heap[rightChildIndex]:
                    childToSwap = rightChildIndex
                else:
                    childToSwap = leftChildIndex
            else:
                break
            if self.heap[childToSwap] > self.heap[index]:
                tmp = self.heap[index]
                self.heap[index] = self.heap[childToSwap]
                self.heap[childToSwap] = tmp
            else :
                break
            index = childToSwap

    def heapifyBelow(self,index):
        value = self.heap[index]
        leftChildIndex = self.leftChild(index)
        rightChildIndex = self.rightChild(index)
        while (self.leftChildExists(index) and \
                value < self.heap[self.leftChild(index)]) or \
                (self.rightChildIndexExists(index) and \
                    value < self.heap[self.rightChild(index)]):
            if self.heap[leftChildIndex]  > self.heap[rightChildIndex]:
                self.heap[index] = self.heap[leftChildIndex]
                index = leftChildIndex
                leftChildIndex = self.leftChild(index)
                rightChildIndex = self.rightChild(index)
            else:
                self.heap[index] = self.heap[rightChildIndex]
                index = rightChildIndex
                rightChildIndex = self.rightChild(index)
                leftChildIndex = self.leftChild(index)
        self.heap[index] = value

    def swap(self, currentIndex, parentIndex):
        temp = self.heap[parentIndex]
        self.heap[parentIndex] = self.heap[currentIndex]
        self.heap[currentIndex] = temp
    
    def parent(self,currentIndex):
        return floor((currentIndex - 1) / 2)
    
    def leftChild(self, currentIndex):
        return 2*currentIndex + 1
    
    def rightChild(self, currentIndex):
        return 2*currentIndex + 2

data = heap()
data.insert(21)
data.insert(45)
data.insert(13)
data.insert(89)
data.insert(23)
data.insert(12)
data.insert(4)
data.insert(90)
data.insert(46)
print(data.peak())
data.insert(123)
data.insert(34)
data.insert(67)
data.remove(1)
print(data.peak())
print("done")