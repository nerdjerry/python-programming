dictionary = {
        'a' : 0,
        'b' : 1,
        'c' : 2,
        'd' : 3,
        'e' : 4,
        'f' : 5,
        'g' : 6,
        'h' : 7,
        'i' : 8,
        'j' : 9,
        'k' : 10,
        'l' : 11,
        'm' : 12,
        'n' : 13,
        'o' : 14,
        'p' : 15,
        'q' : 16,
        'r' : 17,
        's' : 18,
        't' : 19,
        'u' : 20,
        'v' : 21,
        'w' : 22,
        'x' : 23,
        'y' : 24,
        'z' : 25,
    }
def radixSort(array, width, radix):
    for i in range(width):
        sort(array,i,radix,width)

def sort(array, position, radix,width):
    count = [0] * radix
    temp = [None] * len(array)
    for i in range(len(array)):
        count[dictionary[array[i][width - position - 1]]] += 1
    for i in range(1,len(count)):
        count[i] += count[i-1]
    for i in range(len(array)-1, -1, -1):
        temp[count[dictionary[array[i][width - position - 1]]] - 1] = array[i]
        count[dictionary[array[i][width - position - 1]]] -= 1
    for i in range(len(array)):
        array[i] = temp[i]

array = ['bcdef','dbaqc','abcde','omadd','bbbbb']
radixSort(array, 5, 26)
for i in array:
    print(i)