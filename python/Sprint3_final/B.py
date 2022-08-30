# id 69846885
def partition(candidate, left, right):
    pivot = (candidate[left])
    new_left = left + 1
    new_right = right - 1
    while True:
        if (new_left <= new_right and candidate[new_right] > pivot):
            new_right -= 1
        elif (new_left <= new_right and candidate[new_left] < pivot):
            new_left += 1
        if new_left <= new_right:
            (candidate[new_left],
             candidate[new_right]) = (candidate[new_right],
                                      candidate[new_left])
        else:
            (candidate[left],
             candidate[new_right]) = (candidate[new_right],
                                      candidate[left])
            return new_right


def quick_sort(candidate, left, right):
    if ((right - left) > 1):
        middle = partition(candidate, left, right)
        quick_sort(candidate, left, middle)
        quick_sort(candidate, middle + 1, right)
    else:
        return


def transformation(candidate):
    candidate[1] = - int(candidate[1])
    candidate[2] = int(candidate[2])
    return [candidate[1], candidate[2], candidate[0]]


def main():
    number = int(input())
    candidate = [transformation(input().split()) for _ in range(number)]
    quick_sort(candidate, 0, len(candidate))
    print(*(list(zip(*candidate))[2]), sep="\n")


if __name__ == '__main__':
    main()
