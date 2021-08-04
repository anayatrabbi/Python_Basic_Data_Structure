# Python program to calculate the value of 'a' to the power 'b'.

def power(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    elif a == 0:
        return 0
    elif a == 1:
        return 1
    else:
        return a * power(a, b-1)


print(power(3, 2))
