from error import error
from linkedlist import *

class queue(object):
    
    def __init__(self):
        self.list = linked_list()
    
    def enqueue(self, value):
        self.list.add(value)
    
    def deqeue(self):
        return self.list.delete(0)