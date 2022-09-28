def binarySearch(data, price, left, right):
    if (right <= left and left != 0):
        return -1
    mid = (left + right) // 2
    if (data[mid] >= price and (data[mid-1] < price or mid == 0)):
        return mid+1
    elif price <= data[mid]:
        return binarySearch(data, price, left, mid)
    else:
        return binarySearch(data, price, mid+1, right)


def read_data():
    len_data = int(input())
    data = [int(i) for i in input().split(' ')]
    price = int(input())
    return len_data, data, price


def main():
    len_data, data, price = read_data()
    print(binarySearch(data, price, 0, len_data), end=' ')
    print(binarySearch(data, price*2, 0, len_data))


if __name__ == '__main__':
    main()
