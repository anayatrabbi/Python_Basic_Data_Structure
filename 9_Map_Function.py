items = [
    ("product", 10),
    ("mango", 29),
    ("Orange", 20),
    ("cucamber", 30)
]

prices = []
for item in items:
    prices.append(item[1])

print(prices)

x = map(lambda item: item[1], items)
# here using map we made a iterable object
for item in x:
    print(item)

# we can pass any iterable in list function

x = list(map(lambda item: item[1], items))

print(x)
