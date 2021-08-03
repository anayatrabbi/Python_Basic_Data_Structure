numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numbers)

# it is like spread operator (...) in javascript

print(*numbers)

values = [*range(5), *"hello world", *numbers]

print(values)

# unpack dictionary

first = dict(x=2, d=3, h=4)
second = dict(x=1, d=2, h=6)

# unpack
# if u have multiple value 2nd will be appear
new_values = {**first, **second}

print(new_values)
