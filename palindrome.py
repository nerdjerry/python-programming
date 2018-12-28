from queues.queue import Queue
from stacks.stackarray import StackArray
import sys
import os
sys.path.append(os.path.abspath('.'))
print(sys.path)
def checkPalindrome(input):
	input = input.lower()
	input = removepuntuation(input)
	inputLength = len(input)
	stacks = StackArray(inputLength)
	queues = Queue(inputLength)
	for i in range(inputLength):
		stacks.push(input[i])
		queues.enqueue(input[i])
	i = 0
	while i < inputLength:
		if not stacks.pop() == queues.dequeue():
			return False
		i += 1
	return True
   

def removepuntuation(input):
    puntuation = ".,/?;:! "
    temp = ""
    for i in range(len(input)):
        if not input[i] in puntuation:
            temp += input[i]
    return temp


print(checkPalindrome("Racecare"))