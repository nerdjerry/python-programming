def sort(array):
    gap = len(array)//2
    while gap > 0 :
        i = gap
        while i < len(array):
            newElement = array[i]
            j = i
            while j >= gap and array[j-gap] > newElement :
                array[j] = array[j-gap]
                j = j - gap
            array[j] = newElement
            i = i + 1
        gap = gap // 2

array = [20,35,-15,7,55,1,-22,-16]
sort(array)
for i in range(len(array)):
    print(array[i])