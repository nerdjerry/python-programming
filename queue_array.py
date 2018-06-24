from error import error

class queue(object):

    def __init__(self):
        self.insert = -1
        self.delete = -1
        self.arr = []
    
    def enqueue(self,value):
        self.insert +=1
        self.arr.append(value)
        return True
    
    def dequeue(self):
        if not self.isEmpty():
            self.delete +=1
            result = self.arr[self.delete]
            self.arr[self.delete] = None
            return result
        else:
            return error("List is empty")
    
    def isFull(self):
        return self.insert == len(self.arr)-1
    
    def isEmpty(self):
        return self.insert == self.delete
    
    def print_queue(self):
        return self.arr