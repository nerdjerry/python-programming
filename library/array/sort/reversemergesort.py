def mergeSort(array, start, end):
    if not end - start < 2:
        mid = (start+end)//2
        mergeSort(array,start, mid)
        mergeSort(array,mid,end)
        merge(array,start,mid,end)

def merge(array, start, mid, end):
    if array[mid-1] >=  array[mid]:
        return
    tempLength = end - start
    i = start
    j = mid
    tindex = 0
    temp = [None] * tempLength
    while i < mid and j < end :
        if array[i] >= array[j]:
            temp[tindex] = array[i]
            tindex +=1
            i +=1
        else:
            temp[tindex] = array[j]
            tindex +=1
            j +=1
    
    arrayCopy(array,array,i, start+tindex, mid - i)
    arrayCopy(temp,array,0,start, tindex)

def arrayCopy(source, dest, sourceStart, destStart, count):
    i = sourceStart
    j = destStart

    while count > 0 :
        dest[j] = source[i]
        j +=1
        i +=1
        count -= 1

test = [5,9,8,3,45,32,5,7]
mergeSort(test,0,7)

for element in test:
    print(element)