class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        new_max = max(item, self.items[-1]) if self.items else item
        self.items.append(new_max)

    def pop(self):
        if self.items == []:
            print('error')
        else:
            self.items.pop()
    
    def get_max(self):
        return None if self.items == [] else self.items[-1]

def read_data():
    n = int(input())
    return [input() for _ in range(n)]

def main():
    command = read_data()
    stack_iter = Stack()
    for iterate in command:
        if iterate == 'get_max':
            print(stack_iter.get_max())
        if iterate == 'pop':
            stack_iter.pop()
        if 'push' in iterate:
            _, value = iterate.split(' ')
            stack_iter.push(int(value))

if __name__ == '__main__':
    main()
