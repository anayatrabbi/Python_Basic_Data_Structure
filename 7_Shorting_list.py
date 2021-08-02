numbers = [4, 1, 8, 5, 6]

numbers.sort()
numbers.sort(reverse=True)

print(sorted(numbers, reverse=True))
# it will not change the main element

items = [
    ("product", 10),
    ("mango", 29),
    ("Orange", 20),
    ("cucamber", 30)
]


def sort_item(items):
    return items[1]


# items.sort(sort_item)
# print(items)

# we can sort only key value

items.sort(key=sort_item, reverse=True)
print(items)
