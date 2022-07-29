#ID 69525635
import sys


def main(n, data):
    data = data.replace('.', '')
    result_dict = {}
    for i in range(len(data)):
        if data[i] not in result_dict:
            result_dict[data[i]] = 1
        else:
            result_dict[data[i]] += 1
    return sum(j <= n*2 for j in result_dict.values())


def read_data():
    n = int(input())
    return n, ''.join(sys.stdin.readline().rstrip() for _ in range(4))


if __name__ == '__main__':
    n, data = read_data()
    print(main(n, data))
