# tuple is a read only list
# can not modify add
# immutable

point1 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# or
point2 = 2, 3, 4, 5, 6, 7, 8

print(type(point2))

# multipicaion operator uses in tuple

point3 = (1, 2) * 2

# unpack tuple

point3 = (2, 3, 4)
x, y, z = point3

# check existence value in tuple

if 10 in point1:
    print("exist")

# immutable

point1[0] = 2
# throw an error

# convert list to tuple

point4 = tuple([1, 2, 3])

# as list

point2[0:3]
