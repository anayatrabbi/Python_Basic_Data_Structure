# collection of key value pairs
#

point = {"x": 1, "y": 2}
list()
set()
tuple()

point = dict(x=1, y=2, z=4)

# add new value to
point["a"] = 4

print(point)
# delete a key value

# check a value with
del point["a"]
if "a" in point:
    print(point["a"])

# iteration over
for key in point:
    print(key)

for key, value in point.items():
    print(f"{key} {value}")
