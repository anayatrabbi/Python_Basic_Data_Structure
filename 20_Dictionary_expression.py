# list
values = [x*2 for x in range(5)]
values = []
for x in range(5):
    values.append(x*2)

# set
values = {x*2 for x in range(5)}

# dictionary

values = {}  # declaring a dictionary
for x in range(5):
    values[x] = x*2

values = {x: x*2 for x in range(5)}
