"""Факторизация числа"""

from typing import List

def factorize(number: int) -> List[int]:
    result = []
    for i in range(number-1,1,-1):
        if number % i == 0:
            number = i
            result

    return result


result = factorize(int(input()))
print(" ".join(map(str, result)))
