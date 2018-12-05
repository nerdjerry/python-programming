def countsort(array,upper,lower):
    length = upper - lower + 2
    count = [0] * length
    count[0] = None

    for i in range(len(array)):
        count[array[i]] = count[array[i]] + 1
    
    j = 0 
    
    for i in range(length):
        if count[i] == None:
            continue
        while count[i] > 0 :
            array[j] = i
            count[i] = count[i] - 1
            j = j + 1

test = [2,9,2,4,2,6,5,9,3]
countsort(test,9,1)

for i in test:
    print(i)
