# ID 69682649
def main(count_finger, data, players=2):
    return sum(
        data.count(str(number)) <= count_finger * players
        for number in set(data)
    )


def read_data():
    count_finger = int(input())
    data = ''.join(input() for _ in range(4))
    return count_finger, data.replace('.', '')


if __name__ == '__main__':
    count_finger, data = read_data()
    print(main(count_finger, data))
