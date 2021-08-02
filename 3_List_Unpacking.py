numbers = [1, 2, 3, 4, 4, 4, 4, 4, 4, 4]

first, second, third, fourth, *other = numbers

print(other)

# we uses this esteric for input multiple value in python


def multiply(*numbers):
    print(numbers)
