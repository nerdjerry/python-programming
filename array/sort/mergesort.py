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
    while i<=mid or j <=end:
        if i == mid + 1 :
            temp[tindex] = array[j]
            tindex = tindex + 1
            j = j + 1
        elif j == end + 1 :
            temp[tindex] = array[i]
            tindex = tindex + 1
            i = i + 1
        else:
            if array[i] <= array[j]:
                temp[tindex]  = array[i]
                i = i + 1
                tindex = tindex + 1
            else:
                temp[tindex] = array[j]
                j = j + 1
                tindex = tindex + 1
    
    aindex = end
    tindex = tindex - 1
    while aindex >= start :
        array[aindex] = temp[tindex]
        aindex = aindex - 1
        tindex = tindex - 1

test = [5,9,8,3,45,32,5,7]
mergesort(test,0,7)

for element in test:
    print(element)