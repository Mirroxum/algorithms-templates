"""Перевод из 10ной в двоичную"""


def to_binary(number: int) -> str:
    result = ''
    while True:
        result += str(number % 2)
        number = number // 2
        if number // 2 == 0:
            result += str(number)
            break
    return result[::-1]


def read_input() -> int:
    return int(input().strip())


print(to_binary(read_input()))
