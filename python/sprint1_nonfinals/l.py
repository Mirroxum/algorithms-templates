"""Пересечение строк"""
from typing import Tuple


def get_excessive_letter(shorter: str, longer: str) -> str:
    list_short = list(shorter)
    list_longer = list(longer)
    for i in list_longer:
        if i in list_short:
            list_short.remove(i)
        else:
            return i


def read_input() -> Tuple[str, str]:
    shorter = input().strip()
    longer = input().strip()
    return shorter, longer


shorter, longer = read_input()
print(get_excessive_letter(shorter, longer))
