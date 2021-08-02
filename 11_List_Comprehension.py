# better way of map and filter is there

items = [
    ("product", 10),
    ("mango", 29),
    ("Orange", 20),
    ("cucamber", 30)
]

prices = [item[1] for item in items]

filtered = [item for item in items if item[1] >= 20]

print(filtered)
