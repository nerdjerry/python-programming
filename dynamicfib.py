def fib(n, memo) :
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif memo[n] is None:
        memo[n] = fib(n-1, memo) + fib(n-2,memo)
    return memo[n]

print(fib(6,[None for i in range(7)]))