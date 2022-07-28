"""Палиндром"""

import re


def is_palindrome(line: str) -> bool:
    line = line.lower()
    reg = r'[\d\w]'
    left = 0
    right = len(line) - 1
    while left < right:
        if re.match(reg, line[left]) is None:
            left += 1
            continue
        if re.match(reg, line[right]) is None:
            right -= 1
            continue
        if line[left] != line[right]:
            return False
        left += 1
        right -= 1
    return True

print(is_palindrome(input().strip()))

pal=''
for i in s:
    if i.isalnum() :
        pal += i.lower()
return pal == pal[::-1]




# def is_palindrome(line: str) -> bool:
#     pal = ''
#     for i in line:
#         if i.isalnum():
#             pal += i.lower()
#     return pal == pal[::-1]

# print(is_palindrome(input().strip()))