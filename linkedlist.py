from error import error


class node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class linked_list(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, value):
        if not self.tail:
            self.head = node(value)
            self.tail = self.head
        else:
            self.tail.next = node(value)
            self.tail = self.tail.next

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
            current.next = None
            return True
        else:
            while index:
                if not current:
                    return error("Out of bounds")
                index -= 1
                previous = current
                current = current.next
            previous.next = current.next
            current.next = None
            return True

    def print_list(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next


list = linked_list()
list.add(4)
list.add(5)
list.add(6)
print(list.get(2))
print(list.delete(8))
list.print_list()
