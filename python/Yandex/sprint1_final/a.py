# ID 69682650
def distance_zero(count_house, data):
    result = [0] * count_house
    zeroes_index = [
        index for index in range(count_house) if data[index] == 0
    ]
    for index in range(zeroes_index[0]):
        result[index] = zeroes_index[0] - index
    for index in range(len(zeroes_index) - 1):
        start = zeroes_index[index]
        end = zeroes_index[index + 1]
        for position in range(start + 1, end):
            result[position] = min(
                position - start,
                end - position)
    for index in range(zeroes_index[-1] + 1, count_house):
        result[index] = index - zeroes_index[-1]
    return result


def read_data():
    return int(input()), [int(number) for number in input().split()]


if __name__ == '__main__':
    count_house, data = read_data()
    print(*distance_zero(count_house, data))
