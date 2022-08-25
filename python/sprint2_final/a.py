# ID 69756814	
class Deque:
    def __init__(self, size):
        self.queue = [None] * size
        self.max_size = size
        self.head = 1
        self.tail = 0
        self.len = 0

    def push_back(self, value):
        if self.len == self.max_size:
            raise AttributeError('Deque is full')
        self.tail = (self.tail + 1) % self.max_size
        self.queue[self.tail] = value
        self.len += 1

    def push_front(self, value):
        if self.len == self.max_size:
            raise AttributeError('Deque is full')
        self.head = (self.head - 1) % self.max_size
        self.queue[self.head] = value
        self.len += 1

    def pop_back(self):
        if self.len == 0:
            raise IndexError('Deque is empty')
        value = self.queue[self.tail]
        self.queue[self.tail] = None
        self.len -= 1
        self.tail = (self.tail - 1) % self.max_size
        return value

    def pop_front(self):
        if self.len == 0:
            raise IndexError('Deque is empty')
        value = self.queue[self.head]
        self.queue[self.head] = None
        self.len -= 1
        self.head = (self.head + 1) % self.max_size
        return value


def read_data():
    number_commands = int(input())
    size = int(input())
    return size, [input() for _ in range(number_commands)]


def read_commands(size, commands):
    deque = Deque(size)
    for command in commands:
        operation, *value = command.split(' ')
        try:
            result = getattr(deque, f'{operation}')(*value)
            if result:
                print(result)
        except Exception:
            print('error')


def main():
    size, commands = read_data()
    read_commands(size, commands)



if __name__ == '__main__':
    main()
