#Fibonnaci number using dynamic programming

def fib(n, mem):
    if mem[n] != None :
        return mem[n]
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib(n-1,mem) + fib (n-2,mem)
        mem[n] = result
    return result

n = 310
mem = [None] * (n+1)
print(fib(n,mem))

def fib_bottom(n):
    mem = [None,1,1]
    for i in range(3,n+1):
        mem.append(mem[i-1]+mem[i-2])
    return mem[n]

print(fib_bottom(10))