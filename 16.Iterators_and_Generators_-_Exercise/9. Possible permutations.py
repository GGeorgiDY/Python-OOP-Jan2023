# трябва да върнем всички възможни пермутации от даден лист
from itertools import permutations


def possible_permutations(lst):
    for el in list(permutations(lst)):
        yield list(el)


[print(n) for n in possible_permutations([1, 2, 3])]
# [1, 2, 3]
# [1, 3, 2]
# [2, 1, 3]
# [2, 3, 1]
# [3, 1, 2]
# [3, 2, 1]

[print(n) for n in possible_permutations([1])]
# [1]