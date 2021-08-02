items = [
    ("product", 10),
    ("mango", 29),
    ("Orange", 20),
    ("cucamber", 30)
]

items.sort(key=lambda items: items[1])
print(items)

# we are passong a annoynymus function as lambda expression
# better way of sorting
