# Fibonacci number

def find_Fibonacci(n):
    if n == 0 or n == 1:
        return 1
    return find_Fibonacci(n-1) + find_Fibonacci(n-2)


n_terms = int(input("enter your number"))
print(find_Fibonacci(n_terms))

for i in range(n_terms):
    print(find_Fibonacci(i))
