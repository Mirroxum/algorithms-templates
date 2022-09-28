def max_student(n, data, k):
    count_dict = {}
    result = []
    for id in data:
        count_dict.setdefault(id, 0)
        count_dict[id] += 1
    for _ in range(int(k)):
        max_count = max(count_dict.values())
        for j in count_dict:
            if count_dict[j] == max_count:
                result.append(j)
                del count_dict[j]
                break
    return result

def read_data():
    n = input()
    data = input().split()
    k = input()
    return n, data, k


def main():
    n, data, k = read_data()
    print(*max_student(n, data, k))

if __name__ == '__main__':
    main()