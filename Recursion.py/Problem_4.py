# add this list [1, 2, [3, 4], [5, 6]]

def recursive_list_sum(data_list):
    total = 0
    for data in data_list:
        if type(data) == type([]):
            total = total + recursive_list_sum(data)
        else:
            total = total + data
    return total


print(recursive_list_sum([1, 2, [3, 4], [5, 6]]))
