def bubblesort(array):
    for sortedIndex in range(len(array)-1, 0, -1):
        for i in range(0, sortedIndex):
            if array[i] > array[i+1]:
                swap(array, i)

def swap(array, i):
    array[i] = array[i] + array[i+1]
    array[i+1] = array[i] - array[i+1]
    array[i] = array[i] - array[i+1]

array = [20, 35, -15, 7, 55, 1, -22]
bubblesort(array)
for i in range(len(array)):
    print(array[i])