import math
import itertools


def count_find_num(primesL, limit):
    new_c = list()
    new_c = primesL.copy()
    new_c.append(0)
    count = 0
    count = math.floor(math.log(limit, min(primesL)))

    combinations = [x for x in list(itertools.combinations_with_replacement(new_c, count))]
    combinations = [tuple(x for x in sublist if x != 0) for sublist in combinations]

    answer = []
    count = 0
    max_mult = math.prod(combinations[0])

    for combo in combinations:
        if combo.count(0) != 6 and all((i in combo) for i in primesL) and math.prod(combo) <= limit:
            count += 1
            if max_mult < math.prod(combo):
                max_mult = math.prod(combo)
            answer.append(combo)
    if count == 0:
        return []
    return [count, max_mult]


primesL = [2, 3]
limit = 200
assert count_find_num(primesL, limit) == [13, 192]

primesL = [2, 5]
limit = 200
assert count_find_num(primesL, limit) == [8, 200]

primesL = [2, 3, 5]
limit = 500
assert count_find_num(primesL, limit) == [12, 480]

primesL = [2, 3, 5]
limit = 1000
assert count_find_num(primesL, limit) == [19, 960]

primesL = [2, 3, 47]
limit = 200
assert count_find_num(primesL, limit) == []
