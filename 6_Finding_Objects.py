letters = ["a", "b", "c", "d", "e"]

letters.index("a")
letters.index("z")
# it will provide value type error different language provide diffrent result

# so we  will use

if "z" in letters:
    print(letters.index("z"))

letters.count("a")
# it will provide number of ocurance in the list
