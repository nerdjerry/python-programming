def countSort(array, min, max):
    length = max - min + 1
    countArray = [0] * length
    for i in range(len(array)):
        countArray[array[i] - min]+=1
    
    for i in range (1,length):
        countArray[i] += countArray[i-1]
    
    temp = [None] * len(array)
    for i in range(len(array)-1, -1, -1):
        temp[countArray[array[i]-min]-1] = array[i]
        countArray[array[i]-min]-=1
    
    for i in range(len(temp)):
        array[i] = temp[i]
        i+=1


test = [2,9,2,4,2,6,5,9,3]
countSort(test,2,9)

for i in test:
    print(i)