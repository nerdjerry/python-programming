from linkedlist import *
from queue import *

#LinkedList
list = linked_list()
list.add(4)
list.add(5)
list.add(6)
print(list.get(2))
print(list.delete(8))
list.print_list()

#queue
coffee_line = queue()
coffee_line.enqueue("Bob")
coffee_line.enqueue("Sandra")
print(coffee_line.deqeue())