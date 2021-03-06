def selectionSort(data):
    largestElemenetIndex = 0
    for lastSortedIndex in range(len(data)-1,0,-1):
        for i in range(1,lastSortedIndex+1):
            if data[i] > data[largestElemenetIndex]:
                largestElemenetIndex = i
        swap(data,largestElemenetIndex,lastSortedIndex)
        largestElemenetIndex = 0

def swap(data,largestElemenetIndex,lastSortedIndex):
    temp = data[largestElemenetIndex]
    data[largestElemenetIndex] = data[lastSortedIndex]
    data[lastSortedIndex] = temp

array = [20, 35, -15, 7, 55, 1, -22]
selectionSort(array)
for i in range(len(array)):
    print(array[i])
