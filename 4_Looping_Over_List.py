letters = ["a", "b", "c", "d", "e"]

for letter in letters:
    print(letter)

# if we want index we should use enumerate which will return iterable object
# which is tuple and we can insert any item in tuple

for letter in enumerate(letters):
    print(letter)

# we can unpack tuple as we did for our list

for index, letter in enumerate(letters):
    print(index, letter)
