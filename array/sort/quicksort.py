def quicksort(array, start, end):
    if start < end : 
        position = partition(array, start, end)
        quicksort(array, start, position)
        quicksort(array, position+1, end)

def partition(array, start, end):
    i = start
    j = end
    pivot = array[start]
    j = j - 1
    
    while i < j :
        while array[j] > pivot and i < j:
            j = j - 1
        if i < j:
            array[i] = array[j]
            i = i + 1
       
        while array[i] <= pivot and i < j:
            i = i + 1
        if i < j:
            array[j] = array[i]
            j = j - 1
    array[i] = pivot
    return i

test = [5,9,8,3,45,32,6,7]
quicksort(test,0,8)

for element in test:
    print(element)