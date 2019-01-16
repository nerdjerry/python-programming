def search(input, value):
    for i in range(len(input)):
        if input[i] == value:
            return i
    return -1

input = [34,65,12,34,76,-90,12]
print(search(input,12))
print(search(input,45))