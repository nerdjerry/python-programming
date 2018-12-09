from math import floor
def mergesort(array, start, end):
    if start < end:
        mid = floor((start+end)/2)
        mergesort(array, start, mid)
        mergesort(array, mid+1, end)
        merge(array,start,mid,end)

def merge(array, start, mid, end):
    """
    Optimization 1: If last element of left subarray is less than
    equal to first element of right subarray then we need not do any comparison
    as left and right subarrays will already be sorted in themselves.
    So just merge two
    """
    if array[mid] <= array[mid+1]:
        return
    n = end - start +1
    temp = [None] * n
    tindex = 0
    i = start
    j = mid + 1
    
    while i < mid + 1 and j < end + 1 :
        if array[i] <= array[j]:
            temp[tindex] = array[i]
            tindex +=1
            i +=1
        else:
            temp[tindex] = array[j]
            tindex+=1
            j+=1
    
    """
    Optimisation 2: No need to copy right subarray elements into temp and then back to array 
    as they are already in correct position if you have finished elements in left subarray
    Also, left subarray elements can be directly copied into array at their correct location
    """
    arrayCopy(array,array,i,start+tindex,mid-i+1)
    arrayCopy(temp,array,0,start,tindex)

def arrayCopy(source,dest,sourceStart, destStart, count):
    i = sourceStart
    j = destStart
    while count > 0:
        dest[j] = source[i]
        i+=1
        j+=1
        count-=1

test = [7658,6543,4321,5674,1113,3213,1236]
mergesort(test,0,6)

for element in test:
    print(element)