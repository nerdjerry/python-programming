def sort(array):
    for firstUnsortedIndex in range (1, len(array)):
        newElement = array[firstUnsortedIndex]
        i = firstUnsortedIndex
        while i > 0 and array[i-1] > newElement:
            array[i] = array[i-1]
            i = i - 1
        array[i] = newElement

array = [20, 35, -15, 7, 55, 1, -22]
sort(array)
for i in range(len(array)):
    print(array[i])
