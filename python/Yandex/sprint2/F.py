class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items == []:
            print('error')
        else:
            self.items.pop()
    
    def get_max(self):
        if self.items == []:
            print(None)
        else:
            print(max(self.items))

def read_data():
    n = int(input())
    return [input() for _ in range(n)]

def main():
    command = read_data()
    stack_iter = Stack()
    for iterate in command:
        if iterate == 'get_max':
            stack_iter.get_max()
        if iterate == 'pop':
            stack_iter.pop()
        if 'push' in iterate:
            _, value = iterate.split(' ')
            stack_iter.push(int(value))

if __name__ == '__main__':
    main()
