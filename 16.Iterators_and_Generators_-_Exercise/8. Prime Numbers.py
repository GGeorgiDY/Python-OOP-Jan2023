from typing import List


def get_primes(lst: List[int]):
    for num in lst:
        if num <= 1:
            continue

        for i in range(2, num):
            if num % i == 0:
                break
        else: # ако никога не сработи, ще се изпълни елс
            yield num


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))