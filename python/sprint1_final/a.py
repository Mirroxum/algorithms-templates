#ID 69525576
import sys


def main(data):
    result = [1000000 for _ in range(len(data))]
    count = 0
    for i in range(len(data)):
        if int(data[i]) == 0:
            result[i] = 0
            count = 1
            continue
        if count:
            result[i] = count
            count += 1
    for i in range(-1, -len(data)-1, -1):
        if int(result[i]) == 0:
            count = 1
            continue
        if count < int(result[i]):
            result[i] = count
            count += 1
    return result


def read_data():
    n = int(input())
    return sys.stdin.readline().rstrip().split()


if __name__ == '__main__':
    data = read_data()
    print(" ".join(map(str, main(data))))
