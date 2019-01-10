from ..linkedlist.DoublyLinkedList import DoublyLinkedList
from .storedValue import storedValue

class hashchaining(object):

    def __init__(self,capacity):
        self.capacity = capacity
        self.table = [None] * self.capacity
    
    def put(self,key,value):
        hashedKey = self.hashkey(key)
        if self.table[hashedKey] == None : 
            self.table[hashedKey] = DoublyLinkedList()
        self.table[hashedKey].insertAtStart(storedValue(key,value))

    def get(self,key):
        hashedKey = self.hashkey(key)
        current = self.table[hashedKey].head
        while current != None:
            if current.getEmployee().key == key:
                return current.getEmployee().value
            current = current.getNext()
        return None
    
    def remove(self,key):
        hashedKey = self.hashkey(key)
        removed = None
        #This means element looking is not even in table based on hah
        if self.table[hashedKey] == None:
            return removed
        current = self.table[hashedKey].head
        index = 0
        while current != None:
            if current.getEmployee().key == key:
                removed = current.getEmployee().value
                self.table[hashedKey].remove(index)
                break
            index += 1
            current = current.getNext()
        return  removed
    
    def hashkey(self,key):
        return len(key) % self.capacity

    def print(self):
        for i in range(self.capacity):
            if self.table[i] != None:
                self.table[i].print()