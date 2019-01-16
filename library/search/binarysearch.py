def binarySearch(input, value):
    return search(input,value,0,len(input))

def search(input, value, start, end):
    midpoint = (start + end) // 2
    if start >= end :
        return -1
    if input[midpoint] == value:
        return midpoint
    elif input[midpoint] > value : 
        return search(input,value,start,midpoint)
    elif input[midpoint] < value :
        return search(input,value,midpoint+1, end)


input = [12,34,56,67,89,90]
print(binarySearch(input,56))
print(binarySearch(input,45))