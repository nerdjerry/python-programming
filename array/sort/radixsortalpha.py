def getIndex(letter, position):
    return ord(letter[position]) - ord('a')
def radixSort(array, width, radix):
    for i in range(width-1, -1, -1):
        sort(array,i,radix)

def sort(array, position, radix):
    count = [0] * radix
    temp = [None] * len(array)
    for i in range(len(array)):
        count[getIndex(array[i],position)] += 1
    for i in range(1,len(count)):
        count[i] += count[i-1]
    for i in range(len(array)-1, -1, -1):
        temp[count[getIndex(array[i],position)] - 1] = array[i]
        count[getIndex(array[i],position)] -= 1
    for i in range(len(array)):
        array[i] = temp[i]

array = ['bcdef','dbaqc','abcde','omadd','bbbbb']
radixSort(array, 5, 26)
for i in array:
    print(i)