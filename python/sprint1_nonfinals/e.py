"""Самое длинное слово"""


def get_longest_word(line: str) -> str:
    arr = line.split(' ')
    result = arr[0]
    for i in arr[1:]:
        if len(i) > len(result):
            result = i
    return result


def read_input() -> str:
    _ = input()
    line = input().strip()
    return line


def print_result(result: str) -> None:
    print(result)
    print(len(result))


print_result(get_longest_word(read_input()))
