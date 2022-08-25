# ID 69756768
import operator


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()


OPERATIONS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv
}


def calculate_polish_abstract(data, type=int):
    stack = Stack()
    for char in data:
        if char not in OPERATIONS:
            stack.push(type(char))
        else:
            right_operand, left_operand = stack.pop(), stack.pop()
            stack.push(OPERATIONS[char](left_operand, right_operand))
    return stack.pop()


def main():
    data = input().split(' ')
    print(calculate_polish_abstract(data))


if __name__ == '__main__':
    main()
