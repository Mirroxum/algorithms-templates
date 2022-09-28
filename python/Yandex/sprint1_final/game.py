MAX_DISK = 8
towers = {'A': list(range(MAX_DISK+1)),
          'B': [0] * (MAX_DISK+1),
          'C': [0] * (MAX_DISK+1)}


def print_tower(towers):
    width = MAX_DISK+1
    for index in range(width):
        for key in towers:
            if towers[key][index] == 0:
                print(' ' * width + '|||' + ' ' * width, end=' ')
            else:
                half_disk = ' ' * (width-towers[key][index]) + '@' * towers[key][index]
                print(half_disk +
                      f' {towers[key][index]} ' + ''.join(reversed(half_disk)), end=' ')
        print()
    for key in towers:
        print(' ' * width + f' {key} ' + ' ' * width, end=' ')
    print()


def read_input():
    start, end = input('> ').upper().strip()
    return start, end


def move(start, end):
    for level in range(MAX_DISK+1):
        if towers[start][level] != 0:
            disk = towers[start][level]
            towers[start][level] = 0
            break
    for level in range(MAX_DISK, 0, -1):
        print(f'{disk} {level}')
        if towers[end][level] == 0:
            towers[end][level] = disk
            break
    # print(towers)


def main():
    while True:
        print_tower(towers)
        start, end = read_input()
        move(start, end)


if __name__ == '__main__':
    main()
