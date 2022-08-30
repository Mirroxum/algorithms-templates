import operator


class Stack:
    def __init__(self):
        self.__items = []

    def push(self, item):
        return self.__items.append(item)

    def pop(self):
        try:
            return self.__items.pop()
        except IndexError as e:
            raise IndexError('Stack is empty') from e


OPERATIONS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv
}


def calculate_polish_abstract(data, conversion=int, operations=OPERATIONS):
    stack = Stack()
    for char in data:
        if char not in operations:
            try:
                stack.push(conversion(char))
            except ValueError as e:
                raise ValueError(
                    f'Failed to convert {char} to {conversion} type') from e
        else:
            right, left = stack.pop(), stack.pop()
            stack.push(operations[char](left, right))
    return stack.pop()


def main():
    data = input().split()
    print(calculate_polish_abstract(data))


if __name__ == '__main__':
    main()
