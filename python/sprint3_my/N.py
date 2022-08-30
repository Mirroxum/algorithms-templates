"""
Клумбы (segmentsunion.py)
Алла захотела, чтобы у неё под окном были узкие клумбы с тюльпанами. На схеме земельного участка клумбы обозначаются просто горизонтальными отрезками, лежащими на одной прямой. Для ландшафтных работы было нанято n садовников. Каждый из них обрабатывал какой-то отрезок на схеме. Процесс был организован не очень хорошо, иногда один и тот же отрезок или его часть могли быть обработаны сразу несколькими садовниками. Таким образом, отрезки, обрабатываемые двумя разными садовниками, сливаются в один. Непрерывный обработанный отрезок затем станет клумбой. Нужно определить границы будущих клумб. Рассмотрим примеры.
Примеры
4
7 8
7 8
2 3
6 10
2 3
6 10
4
2 3
5 6
3 4
3 4
2 4
5 6
6
1 3
3 5
4 6
5 6
2 4
7 10
1 6
7 10
"""
def segmentsUnion(data):
    data.sort()
    newData = []
    start = data[0][0]
    end = data[0][1]
    for i in range(len(data)-1):
        if end < data[i+1][0]:
            newData.append(f'{start} {end}')
            start = data[i+1][0]
            end = data[i+1][1]
        elif data[i+1][1] > end:
            end = data[i+1][1]
    newData.append(f'{start} {end}')
    return newData


def read_data():
    n = int(input())
    return [tuple(int(x) for x in input().split()) for _ in range(n)]


def main():
    data = read_data()
    print('\n'.join(segmentsUnion(data)), end='')


if __name__ == '__main__':
    main()
