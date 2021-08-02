numbers = [1, 1, 2, 3, 45, 5, 6, 6, ]

uniques = set(numbers)

print(uniques)

second = {1, 4}
second.add(5)
second.remove(4)

# mathmetical operation

print(uniques & second)  # intersection
print(uniques | second)  # union
print(uniques - second)
print(uniques ^ second)

print(type(uniques))

# set object does not support index

# print(second[1])

# but we check existence number in set

if 4 in second:
    print("exist")
