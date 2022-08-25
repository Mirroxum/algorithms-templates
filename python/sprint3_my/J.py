def bubble_sort(number, source_array):
    flag = 1
    for i in range(number - 1):
        for j in range(number - i - 1):
            if source_array[j] > source_array[j + 1]:
                source_array[j], source_array[j + 1] = source_array[j + 1], source_array[j]
                flag = True
        if flag:
            print(*source_array)
            flag = False

if __name__ == '__main__':
    number = int(input())
    source_array = [int(num) for num in input().split(' ')]
    bubble_sort(number, source_array)