def mergeSort(array, start, end):
    if start < end:
        mid = (start+end)//2
        mergeSort(array,start, mid)
        mergeSort(array,mid+1,end)
        merge(array,start,mid,end)

def merge(array, start, mid, end):
    if array[mid] >=  array[mid+1]:
        return
    tempLength = end - start + 1
    i = start
    j = mid+1
    tindex = 0
    temp = [None] * tempLength
    while i < mid + 1 and j < end + 1:
        if array[i] >= array[j]:
            temp[tindex] = array[i]
            tindex +=1
            i +=1
        else:
            temp[tindex] = array[j]
            tindex +=1
            j +=1
    
    arrayCopy(array,array,i, start+tindex, mid - i +1)
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