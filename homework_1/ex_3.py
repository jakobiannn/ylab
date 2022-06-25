def zeros(num):
    res = 0
    while num > 0:
        num //= 5
        res += num
    return res


assert zeros(0) == 0
assert zeros(6) == 1
assert zeros(30) == 7
