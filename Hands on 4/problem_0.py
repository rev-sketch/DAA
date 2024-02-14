'''Problem 0 :Implemented the fibonacci sequence'''

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def print_fib(n):
    result = fib(n)
    print(f"fib({n}) = {result}")
    

n = int(input("Input a value for Fibonacci calculation(n) :"))
print_fib(n)