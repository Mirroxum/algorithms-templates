def main(count_house, data):
    result = [float('inf')] * count_house
    count = 0
    position_zero = 0
    for position in range(count_house):
        if data[position] == 0:
            result[position] = 0
            count = 1
            if position_zero is None:
                position_zero = position
            if position != 0:
                for pos in range(position-1, position - (position-position_zero)//2-1, -1):
                    result[pos] = count
                    print(result)
                    count += 1
                count = 1
            position_zero = position
            continue
        if count:
            result[position] = count
            print(result)
            count += 1
    return result


def read_data():
    return int(input()), [int(num) for num in input().split()]


if __name__ == '__main__':
    count_house, data = read_data()
    [print(number, end=' ') for number in main(count_house, data)]