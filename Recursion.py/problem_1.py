# adding a series of number
# 1+2+3+.....+8

def find_sum(n):
    if n == 1:
        return 1
    return n + find_sum(n-1)


print(find_sum(8))
