# ID 69916951
def broken_search(numbers, target) -> int:
    left, right = 0, len(numbers) - 1
    while left <= right:
        middle = (left + right) // 2
        middle_number = numbers[middle]
        for index in [middle, left, right]:
            if numbers[index] == target:
                return index
        if numbers[left] < middle_number:
            if numbers[left] < target < middle_number:
                right = middle - 1
            else:
                left = middle + 1
        elif middle_number < target < numbers[right]:
            left = middle + 1
        else:
            right = middle - 1
    return -1
