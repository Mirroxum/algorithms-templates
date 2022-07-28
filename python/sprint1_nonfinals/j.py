"""Факторизация числа"""

from typing import List

def is_prime(n):
    """Проверка на натуральное число"""
    if n == 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i = i + 1
    return True

def factorize(number: int) -> List[int]:
    result = []
    for i in range(2,number):
        if is_prime(i):
            while number % i == 0:
                number /= i
                result.append(i)
    if not result:
        result.append(number)
    return result

result = factorize(int(input()))
print(" ".join(map(str, result)))
