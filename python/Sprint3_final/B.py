# id 69871586
def quick_sort(candidate):

    def partition(candidate, left, right):
        pivot = (candidate[left])
        new_left = left + 1
        new_right = right - 1
        while new_left < new_right or new_left == new_right:
            if pivot < candidate[new_right]:
                new_right -= 1
            elif candidate[new_left] < pivot:
                new_left += 1
            else:
                (candidate[new_left],
                 candidate[new_right]) = (candidate[new_right],
                                          candidate[new_left])
        (candidate[left],
         candidate[new_right]) = (candidate[new_right],
                                  candidate[left])
        return new_right

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
