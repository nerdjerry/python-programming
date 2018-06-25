from error import error


class node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class linked_list(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = -1

    #Add at the end of linked list in O(1)
    def add(self, value):
        newNode = node(value)
        if not self.tail:
            self.head = newNode
        else:
            self.tail.next = newNode
        self.tail = newNode
        self.size+=1

    def addAtHead(self,value):
        newNode = node(value)
        
        if not self.head:
            self.head = newNode
        else:
            current = self.head
            self.head = newNode
            self.head.next = current
    
    def addAtIndex(self,value,index):
        newNode = node(value)
        current = self.head
        while index != 1:
            index -=1
            if current :
                current = current.next
        nextNode = current.next
        current.next = newNode
        newNode.next = nextNode
        self.size +=1

    def get(self, index):
        current = self.head
        while index:
            if not current:
                return None
            index -= 1
            current = current.next
        return current.value

    def delete(self, index):
        current = self.head
        previous = None
        if index < 0:
            return error("Operation not supported")
        elif index is 0:
            self.head = current.next
            value = current.value
            current.next = None
            self.size-=1
            return value
        else:
            while index:
                if not current:
                    return error("Out of bounds")
                index -= 1
                previous = current
                current = current.next
            previous.next = current.next
            value = current.value
            current.next = None
            self.size-=1
            return value

    def get_size(self):
        return self.size
 
    def print_list(self):
        current = self.head
        while current:
            print(current.value, end='->')
            current = current.next
        print()
    
    def reverse(self):
        current = self.head
        prev = None
        next = None
        if self.head:
            if self.head.next:
                next = current.next
                self.head.next = None
            while next:
                prev = current
                current = next
                next = current.next
                current.next = prev
        self.head = current

#pass head of two lists to compare
def compare_lists(llist1, llist2):
    list1_current = llist1
    list2_current = llist2
    while list1_current and list2_current:
        if list1_current.value != list2_current.value:
            return 0
        list1_current =list1_current.next
        list2_current = list2_current.next
    if list1_current != list2_current:
        return 0
    return 1