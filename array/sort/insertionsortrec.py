def insertionsort(array):
    for i in range(1, len(array)):
        newElement = array[i]
        shift(array,newElement,i)

def shift(array,newElement,i):
    if not (i > 0 and array[i-1] > newElement):
        return
    
    array[i] = array[i-1]
    array[i-1] = newElement
    shift(array,newElement,i-1)


def insertionRecurssion(array, num):
    if num < 2:
        return 
    
    insertionRecurssion(array, num - 1)

    newElement = array[num]
    j = num
    while ( j > 0 and array[j-1]>newElement):
        array[j] = array[j-1]
        j -=1
    array[j] = newElement


test = [4,5,7,1,2,6,12]
insertionRecurssion(test,6)

for i in test:
    print(i)