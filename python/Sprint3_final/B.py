# id 69916965
def quick_sort(candidate):

    def partition(candidate, left, right):
        pivot = candidate[left]
        start = left + 1
        end = right - 1
        while start <= end:
            if pivot < candidate[end]:
                end -= 1
                continue
            elif candidate[start] < pivot:
                start += 1
                continue
            else:
                (candidate[start],
                 candidate[end]) = (candidate[end],
                                    candidate[start])
        (candidate[left],
         candidate[end]) = (candidate[end],
                            candidate[left])
        return end

    def quick_sort_into(candidate, left, right):
        if right - left > 1:
            middle = partition(candidate, left, right)
            quick_sort_into(candidate, left, middle)
            quick_sort_into(candidate, middle + 1, right)

    quick_sort_into(candidate, 0, len(candidate))


if __name__ == '__main__':
    def transformation(candidate):
        candidate[1] = - int(candidate[1])
        candidate[2] = int(candidate[2])
        return [candidate[1], candidate[2], candidate[0]]

    number = int(input())
    candidates = [transformation(input().split()) for _ in range(number)]
    quick_sort(candidates)
    print(*[candidate[2] for candidate in candidates], sep="\n")
