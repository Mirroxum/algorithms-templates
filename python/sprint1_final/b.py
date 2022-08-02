#ID 69556020
def main(count, data):
    result_dict = {}
    for position in range(len(data)):
        result_dict.setdefault(data[position], 0)
        result_dict[data[position]] += 1
    return sum(j <= count*2 for j in result_dict.values())


def read_data():
    count = int(input())
    data = ''.join(input() for _ in range(4))
    return count, data.replace('.', '')


if __name__ == '__main__':
    count, data = read_data()
    print(main(count, data))
