# ID 69870248
def broken_search(numbers, target) -> int:
    left, right = 0, len(numbers) - 1
    while left < right or left == right:
        middle = (left + right) // 2
        middle_numbers = numbers[middle]
        if middle_numbers == target:
            return middle
        if (numbers[left] < middle_numbers
            or numbers[left] == middle_numbers):
            if (numbers[left] < target < middle_numbers
                or target == numbers[left]):
                right = middle - 1
            else:
                left = middle + 1
        elif (middle_numbers < target < numbers[right]
              or target == numbers[right]):
            left = middle + 1
        else:
            right = middle - 1
    return -1
