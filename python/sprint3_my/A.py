def psn_generate(control, n1, n2, prefix):
    if n2 == 0:
        print(prefix)
    else:
        if n1 > 0:
            psn_generate(control + 1, n1 - 1, n2, f'{prefix}(')
        if control > 0:
            psn_generate(control - 1, n1, n2 - 1, f'{prefix})')


def read_data():
    return int(input())


def main():
    n = read_data()
    psn_generate(0, n, n, '')


if __name__ == '__main__':
    main()
