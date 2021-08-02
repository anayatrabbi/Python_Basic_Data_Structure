items = [
    ("product", 10),
    ("mango", 29),
    ("Orange", 20),
    ("cucamber", 30)
]

x = filter(lambda item: item[1] >= 20, items)

for item in x:
    print(item)
# or make a list

y = list(filter(lambda item: item[1] >= 20, items))
print(y)
