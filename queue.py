from error import error
from linkedlist import linked_list

class queue(object):
    
    def __init__(self):
        self.list = linked_list()
    
    def enqueue(self, value):
        self.list.add(value)
    
    def deqeue(self):
        return self.list.delete(0)
    
    def print_queue(self):
        self.list.print_list()