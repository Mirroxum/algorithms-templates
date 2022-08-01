#ID 69546427
def main(data):
    result = [float('inf')] * len(data)
    count = 0
    for position in range(len(data)):
        if int(data[position]) == 0:
            result[position] = 0
            count = 1
            if position != 0:
                position -= 1
                while (position != -1
                       and result[position] > count):
                    result[position] = count
                    position -= 1
                    count += 1
                count = 1
            continue
        if count:
            result[position] = count
            count += 1
    return result


def read_data():
    n = int(input())
    return input().split()


if __name__ == '__main__':
    data = read_data()
    [print(number, end=' ') for number in main(data)]
