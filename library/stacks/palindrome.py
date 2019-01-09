from stackarray import StackArray
def checkPalindrome(input):
    input = input.lower()
    input = removePuntuation(input)
    inputLength = len(input)
    stack = StackArray(inputLength//2)
    for i in range(inputLength//2):
        stack.push(input[i])
    isPalindrome = True
    for i in range(inputLength//2, inputLength):
        if(input[i] != stack.pop()):
            isPalindrome = False
            return isPalindrome
    return isPalindrome

def removePuntuation(input):
    temp = ""
    puntuation = ",.!;:? "
    for i in range(len(input)):
        if not input[i] in puntuation:
            temp += input[i]
    return temp

print(checkPalindrome("I did, did I?"))