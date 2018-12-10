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

test = [4,5,7,1,2,6,12]
insertionsort(test)

for i in test:
    print(i)