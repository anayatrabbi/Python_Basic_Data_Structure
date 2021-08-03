from sys import getsizeof

values = [x*2 for x in range(5)]

for x in values:
    print(x)

# generator are iterable
# it don not store any values as list
# type generator has no len
values = (x*2 for x in range(5))
for i in values:
    print(i)

# check value

print(getsizeof(values))
