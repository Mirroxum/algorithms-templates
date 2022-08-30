"""Вечером ребята решили поиграть в игру «Большое число».
Даны числа. Нужно определить, какое самое большое число можно из них составить.

Формат ввода
В первой строке записано n — количество чисел. Оно не превосходит 100.
Во второй строке через пробел записаны n неотрицательных чисел, каждое из которых не превосходит 1000.

Формат вывода
Нужно вывести самое большое число, которое можно составить из данных чисел."""

def compator(number_1, number_2):
    if len(number_1) == len(number_2):
        return number_1 > number_2
    var1 = number_1 + number_2
    var2 = number_2 + number_1
    return var1 > var2

def max_number_summator(numbers_arr, comparator):
    """Сортировка вставкой"""
    for i in range(1, len(numbers_arr)):
        item_to_insert = numbers_arr[i]
        j = i
        while j > 0 and comparator(item_to_insert, numbers_arr[j-1]):
            numbers_arr[j] = numbers_arr[j-1]
            j-= 1
        numbers_arr[j] = item_to_insert
    return numbers_arr


def read_data():
    n = input()
    return input().split()


def main():
    data = read_data()
    result = max_number_summator(data, compator)
    for i in result:
        print(i, end='')


if __name__ == '__main__':
    main()
