from linkedlist import *
from queue import queue
from queue_array import queue

# #LinkedList
# list = linked_list()
# list.add(4)
# list.add(5)
# list.add(6)
# print(list.get(2))
# print(list.delete(8))
# list.print_list()

# #queue
# coffee_line = queue()
# coffee_line.enqueue("Bob")
# coffee_line.enqueue("Sandra")
# coffee_line.enqueue("Flash")
# coffee_line.enqueue("Iris")
# print(coffee_line.deqeue())
# coffee_line.print_queue()

#array Queue
coffee_line = queue()
coffee_line.enqueue("Bob")
coffee_line.enqueue("Sandra")
coffee_line.enqueue("Flash")
coffee_line.enqueue("Iris")
coffee_line.enqueue("Sandra")
coffee_line.enqueue("Flash")
coffee_line.enqueue("Iris")
coffee_line.enqueue("Sandra")
coffee_line.enqueue("Flash")
coffee_line.enqueue("Iris")
coffee_line.enqueue("Sandra")
coffee_line.enqueue("Flash")
coffee_line.enqueue("Iris")
print(coffee_line.dequeue())
print(coffee_line.dequeue())
print(coffee_line.dequeue())
print(coffee_line.dequeue())
print(coffee_line.dequeue())
print(coffee_line.print_queue())
