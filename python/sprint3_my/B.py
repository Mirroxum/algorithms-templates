data_dict = {'2': 'abc',
             '3': 'def',
             '4': 'ghi',
             '5': 'jkl',
             '6': 'mno',
             '7': 'pqrs',
             '8': 'tuv',
             '9': 'wxyz'}


def get_combine(n, digits, prefix):
    if n == 0:
        print(prefix, end=' ')
    else:
        get_combine(n - 1, digits[1:], prefix + data_dict[digits[0]][0])
        get_combine(n - 1, digits[1:], prefix + data_dict[digits[0]][1])
        get_combine(n - 1, digits[1:], prefix + data_dict[digits[0]][2])
        if digits[0] in ['9', '7']:
            get_combine(n - 1, digits[1:], prefix + data_dict[digits[0]][3])


def read_data():
    return input()


def main():
    num = read_data()
    get_combine(len(num), num, '')


if __name__ == '__main__':
    main()
