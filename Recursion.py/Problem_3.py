# factorial problem using recursive

def func_factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * func_factorial(n-1)


n_time = 5
print(func_factorial(n_time))
