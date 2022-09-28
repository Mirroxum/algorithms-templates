"""Сложение двоичных чисел"""

from typing import Tuple


def get_sum(first_number: str, second_number: str) -> str:
    lf = len(first_number)
    ls = len(second_number)
    different = max([lf, ls]) - min([lf, ls])
    if ls < lf:
        second_number = '0' * different + second_number
    else:
        first_number = '0' * different + first_number
    result = ''
    remainder = 0
    for i in range(-1, -len(first_number)-1, -1):
        if int(first_number[i]) + int(second_number[i]) + remainder == 3:
            result += '1'
            remainder = 1
        elif int(first_number[i]) + int(second_number[i]) + remainder == 2:
            result += '0'
            remainder = 1
        else:
            result += str(int(first_number[i]) +
                          int(second_number[i]) + remainder)
            remainder = 0
    if remainder:
        result += '1'
    return result[::-1]


def read_input() -> Tuple[str, str]:
    first_number = input().strip()
    second_number = input().strip()
    return first_number, second_number


first_number, second_number = read_input()
print(get_sum(first_number, second_number))
