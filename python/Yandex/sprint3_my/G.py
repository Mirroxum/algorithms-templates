"""Рита решила оставить у себя одежду только трёх цветов: розового, 
жёлтого и малинового. После того как вещи других расцветок были убраны, 
Рита захотела отсортировать свой новый гардероб по цветам. Сначала должны 
идти вещи розового цвета, потом —– жёлтого, и в конце —– малинового. 
Помогите Рите справиться с этой задачей.
Примечание: попробуйте решить задачу за один проход по массиву!
https://contest.yandex.ru/contest/24734/problems/G/"""

def count_sort(array):
    result = []
    counting = [0] * 3
    for i in array:
        counting[int(i)] += 1
    for j in range(len(counting)):
        result += [j] * counting[j]
    return result


def read_data():
    input()
    return input().split()


def main():
    data = read_data()
    print(*count_sort(data))


if __name__ == '__main__':
    main()
