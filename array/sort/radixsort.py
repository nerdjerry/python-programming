def getDigit(num, position, radix):
    return num // (10**position) % radix

def radixSort(array, radix, width):
    temp = [None] * len(array)
    for i in range(width):
        count = [0] * radix
        #Count integers in array
        for j in range(len(array)):
            count[getDigit(array[j],i,radix)] +=1
        
        #Adjust counts
        for j in range(1, len(count)):
            count[j] += count[j-1]
        
        #Place elements at their location in temp based on count
        for j in range(len(array)-1, -1,-1):
            temp[count[getDigit(array[j],i,radix)]-1] = array[j]
            count[getDigit(array[j],i,radix)] -=1
        
        #Copy elements back to array
        for j in range(len(temp)):
            array[j] = temp[j]

test = [1236,3213,1113,5674,4321,6543,7658]
radixSort(test,10,4)

for i in test:
    print(i)
